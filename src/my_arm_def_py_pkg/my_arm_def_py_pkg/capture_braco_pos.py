# https://github.com/roboTJ101/ros_myo/blob/master/scripts/myo-rawNode.py



from __future__ import print_function

import argparse
import enum
import re
import struct
import sys
import threading
import time
import math
import serial
from serial.tools.list_ports import comports
from common import *
##################################################################################
import pandas as pd
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64
from my_arm_def_py_pkg import capture_simple_sample as css
from my_arm_def_py_pkg import capture_EMG_sample as cem
from time import perf_counter
from collections import Counter
import numpy as np


##########################################################################################################################
#positions_to_use = [180.0, 90.0, 60.0, 45.0, 30.0]
antebraco = None
pos_braco = None
##############################################################################################################################
Emg_total = []
data_to_class = []
quartenion = []
old_EMG = []
new_emg_ = []
emg_ = None
running = 0
finish_classification = True

'''
    Original by dzhu
        https://github.com/dzhu/myo-raw

    Edited by Fernando Cosentino
        http://www.fernandocosentino.net/pyoconnect

    Edited by Alvaro Villoslada (Alvipe)
        https://github.com/Alvipe/myo-raw
        
    Edited by Caio Lima
        https://github.com/Calima94/Capture_EMG_Data.git
'''
##############################################################################
def multichr(ords):
    if sys.version_info[0] >= 3:
        return bytes(ords)
    else:
        return ''.join(map(chr, ords))


def multiord(b):
    if sys.version_info[0] >= 3:
        return list(b)
    else:
        return map(ord, b)


class Arm(enum.Enum):
    UNKNOWN = 0
    RIGHT = 1
    LEFT = 2


class XDirection(enum.Enum):
    UNKNOWN = 0
    X_TOWARD_WRIST = 1
    X_TOWARD_ELBOW = 2


class Pose(enum.Enum):
    REST = 0
    FIST = 1
    WAVE_IN = 2
    WAVE_OUT = 3
    FINGERS_SPREAD = 4
    THUMB_TO_PINKY = 5
    UNKNOWN = 255


class Packet(object):
    def __init__(self, ords):
        self.typ = ords[0]
        self.cls = ords[2]
        self.cmd = ords[3]
        self.payload = multichr(ords[4:])

    def __repr__(self):
        return 'Packet(%02X, %02X, %02X, [%s])' % \
            (self.typ, self.cls, self.cmd,
             ' '.join('%02X' % b for b in multiord(self.payload)))


class BT(object):
    '''Implements the non-Myo-specific details of the Bluetooth protocol.'''
    def __init__(self, tty):
        self.ser = serial.Serial(port=tty, baudrate=9600, dsrdtr=1)
        self.buf = []
        self.lock = threading.Lock()
        self.handlers = []

    # internal data-handling methods
    def recv_packet(self, timeout=None):
        t0 = time.time()
        self.ser.timeout = None
        while timeout is None or time.time() < t0 + timeout:
            if timeout is not None:
                self.ser.timeout = t0 + timeout - time.time()
            c = self.ser.read()
            if not c:
                return None

            ret = self.proc_byte(ord(c))
            if ret:
                if ret.typ == 0x80:
                    self.handle_event(ret)
                return ret

    def recv_packets(self, timeout=.5):
        res = []
        t0 = time.time()
        while time.time() < t0 + timeout:
            p = self.recv_packet(t0 + timeout - time.time())
            if not p:
                return res
            res.append(p)
        return res

    def proc_byte(self, c):
        if not self.buf:
            if c in [0x00, 0x80, 0x08, 0x88]:  # [BLE response pkt, BLE event pkt, wifi response pkt, wifi event pkt]
                self.buf.append(c)
            return None
        elif len(self.buf) == 1:
            self.buf.append(c)
            self.packet_len = 4 + (self.buf[0] & 0x07) + self.buf[1]
            return None
        else:
            self.buf.append(c)

        if self.packet_len and len(self.buf) == self.packet_len:
            p = Packet(self.buf)
            self.buf = []
            return p
        return None

    def handle_event(self, p):
        for h in self.handlers:
            h(p)

    def add_handler(self, h):
        self.handlers.append(h)

    def remove_handler(self, h):
        try:
            self.handlers.remove(h)
        except ValueError:
            pass

    def wait_event(self, cls, cmd):
        res = [None]

        def h(p):
            if p.cls == cls and p.cmd == cmd:
                res[0] = p
        self.add_handler(h)
        while res[0] is None:
            self.recv_packet()
        self.remove_handler(h)
        return res[0]

    # specific BLE commands
    def connect(self, addr):
        return self.send_command(6, 3, pack('6sBHHHH', multichr(addr), 0, 6, 6, 64, 0))

    def get_connections(self):
        return self.send_command(0, 6)

    def discover(self):
        return self.send_command(6, 2, b'\x01')

    def end_scan(self):
        return self.send_command(6, 4)

    def disconnect(self, h):
        return self.send_command(3, 0, pack('B', h))

    def read_attr(self, con, attr):
        self.send_command(4, 4, pack('BH', con, attr))
        return self.wait_event(4, 5)

    def write_attr(self, con, attr, val):
        self.send_command(4, 5, pack('BHB', con, attr, len(val)) + val)
        return self.wait_event(4, 1)

    def send_command(self, cls, cmd, payload=b'', wait_resp=True):
        s = pack('4B', 0, len(payload), cls, cmd) + payload
        self.ser.write(s)

        while True:
            p = self.recv_packet()
            # no timeout, so p won't be None
            if p.typ == 0:
                return p
            # not a response: must be an event
            self.handle_event(p)


class MyoRaw(object):
    '''Implements the Myo-specific communication protocol.'''

    def __init__(self, tty=None):
        if tty is None:
            tty = self.detect_tty()
        if tty is None:
            raise ValueError('Myo dongle not found!')

        self.bt = BT(tty)
        self.conn = None
        self.emg_handlers = []
        self.imu_handlers = []
        self.arm_handlers = []
        self.pose_handlers = []
        self.battery_handlers = []

    def detect_tty(self):
        for p in comports():
            if re.search(r'PID=2458:0*1', p[2]):
                print('using device:', p[0])
                return p[0]

        return None

    def run(self, timeout=None):
        self.bt.recv_packet(timeout)

    def connect(self):
        # stop everything from before
        self.bt.end_scan()
        self.bt.disconnect(0)
        self.bt.disconnect(1)
        self.bt.disconnect(2)

        # start scanning
        print('scanning...')
        self.bt.discover()
        while True:
            p = self.bt.recv_packet()
            print('scan response:', p)

            if p.payload.endswith(b'\x06\x42\x48\x12\x4A\x7F\x2C\x48\x47\xB9\xDE\x04\xA9\x01\x00\x06\xD5'):
                addr = list(multiord(p.payload[2:8]))
                break
        self.bt.end_scan()

        # connect and wait for status event
        conn_pkt = self.bt.connect(addr)
        self.conn = multiord(conn_pkt.payload)[-1]
        self.bt.wait_event(3, 0)

        # get firmware version
        fw = self.read_attr(0x17)
        _, _, _, _, v0, v1, v2, v3 = unpack('BHBBHHHH', fw.payload)
        print('firmware version: %d.%d.%d.%d' % (v0, v1, v2, v3))

        self.old = (v0 == 0)

        if self.old:
            # don't know what these do; Myo Connect sends them, though we get data
            # fine without them
            self.write_attr(0x19, b'\x01\x02\x00\x00')
            # Subscribe for notifications from 4 EMG data channels
            self.write_attr(0x2f, b'\x01\x00')
            self.write_attr(0x2c, b'\x01\x00')
            self.write_attr(0x32, b'\x01\x00')
            self.write_attr(0x35, b'\x01\x00')

            # enable EMG data
            self.write_attr(0x28, b'\x01\x00')
            # enable IMU data
            self.write_attr(0x1d, b'\x01\x00')

            # Sampling rate of the underlying EMG sensor, capped to 1000. If it's
            # less than 1000, emg_hz is correct. If it is greater, the actual
            # framerate starts dropping inversely. Also, if this is much less than
            # 1000, EMG data becomes slower to respond to changes. In conclusion,
            # 1000 is probably a good value.
            C = 1000
            emg_hz = 50
            # strength of low-pass filtering of EMG data
            emg_smooth = 100

            imu_hz = 50

            # send sensor parameters, or we don't get any data
            self.write_attr(0x19, pack('BBBBHBBBBB', 2, 9, 2, 1, C, emg_smooth, C // emg_hz, imu_hz, 0, 0))

        else:
            name = self.read_attr(0x03)
            print('device name: %s' % name.payload)

            # enable IMU data
            self.write_attr(0x1d, b'\x01\x00')
            # enable on/off arm notifications
            self.write_attr(0x24, b'\x02\x00')
            # enable EMG notifications
            self.start_raw()
            # enable battery notifications
            self.write_attr(0x12, b'\x01\x10')

        # add data handlers
        def handle_data(p):
            if (p.cls, p.cmd) != (4, 5):
                return

            c, attr, typ = unpack('BHB', p.payload[:4])
            pay = p.payload[5:]

            if attr == 0x27:
                # Unpack a 17 byte array, first 16 are 8 unsigned shorts, last one an unsigned char
                vals = unpack('8HB', pay)
                # not entirely sure what the last byte is, but it's a bitmask that
                # seems to indicate which sensors think they're being moved around or
                # something
                emg = vals[:8]
                moving = vals[8]
                self.on_emg(emg, moving)
            # Read notification handles corresponding to the for EMG characteristics
            elif attr == 0x2b or attr == 0x2e or attr == 0x31 or attr == 0x34:
                '''According to http://developerblog.myo.com/myocraft-emg-in-the-bluetooth-protocol/
                each characteristic sends two secuential readings in each update,
                so the received payload is split in two samples. According to the
                Myo BLE specification, the data type of the EMG samples is int8_t.
                '''
                emg1 = struct.unpack('<8b', pay[:8])
                emg2 = struct.unpack('<8b', pay[8:])
                self.on_emg(emg1, 0)
                self.on_emg(emg2, 0)
            # Read IMU characteristic handle
            elif attr == 0x1c:
                vals = unpack('10h', pay)
                quat = vals[:4]
                acc = vals[4:7]
                gyro = vals[7:10]
                self.on_imu(quat, acc, gyro)
            # Read classifier characteristic handle
            elif attr == 0x23:
                typ, val, xdir, _, _, _ = unpack('6B', pay)

                if typ == 1:  # on arm
                    self.on_arm(Arm(val), XDirection(xdir))
                elif typ == 2:  # removed from arm
                    self.on_arm(Arm.UNKNOWN, XDirection.UNKNOWN)
                elif typ == 3:  # pose
                    self.on_pose(Pose(val))
            # Read battery characteristic handle
            elif attr == 0x11:
                battery_level = ord(pay)
                self.on_battery(battery_level)
            else:
                print('data with unknown attr: %02X %s' % (attr, p))

        self.bt.add_handler(handle_data)

    def write_attr(self, attr, val):
        if self.conn is not None:
            self.bt.write_attr(self.conn, attr, val)

    def read_attr(self, attr):
        if self.conn is not None:
            return self.bt.read_attr(self.conn, attr)
        return None

    def disconnect(self):
        if self.conn is not None:
            self.bt.disconnect(self.conn)

    def sleep_mode(self, mode):
        self.write_attr(0x19, pack('3B', 9, 1, mode))

    def power_off(self):
        self.write_attr(0x19, b'\x04\x00')

    def start_raw(self):

        ''' To get raw EMG signals, we subscribe to the four EMG notification
        characteristics by writing a 0x0100 command to the corresponding handles.
        '''
        self.write_attr(0x2c, b'\x01\x00')  # Suscribe to EmgData0Characteristic
        self.write_attr(0x2f, b'\x01\x00')  # Suscribe to EmgData1Characteristic
        self.write_attr(0x32, b'\x01\x00')  # Suscribe to EmgData2Characteristic
        self.write_attr(0x35, b'\x01\x00')  # Suscribe to EmgData3Characteristic

        '''Bytes sent to handle 0x19 (command characteristic) have the following
        format: [command, payload_size, EMG mode, IMU mode, classifier mode]
        According to the Myo BLE specification, the commands are:
            0x01 -> set EMG and IMU
            0x03 -> 3 bytes of payload
            0x02 -> send 50Hz filtered signals
            0x01 -> send IMU data streams
            0x01 -> send classifier events
        '''
        self.write_attr(0x19, b'\x01\x03\x02\x01\x01')

        '''Sending this sequence for v1.0 firmware seems to enable both raw data and
        pose notifications.
        '''

        '''By writting a 0x0100 command to handle 0x28, some kind of "hidden" EMG
        notification characteristic is activated. This characteristic is not
        listed on the Myo services of the offical BLE specification from Thalmic
        Labs. Also, in the second line where we tell the Myo to enable EMG and
        IMU data streams and classifier events, the 0x01 command wich corresponds
        to the EMG mode is not listed on the myohw_emg_mode_t struct of the Myo
        BLE specification.
        These two lines, besides enabling the IMU and the classifier, enable the
        transmission of a stream of low-pass filtered EMG signals from the eight
        sensor pods of the Myo armband (the "hidden" mode I mentioned above).
        Instead of getting the raw EMG signals, we get rectified and smoothed
        signals, a measure of the amplitude of the EMG (which is useful to have
        a measure of muscle strength, but are not as useful as a truly raw signal).
        '''

        # self.write_attr(0x28, b'\x01\x00')  # Not needed for raw signals
        # self.write_attr(0x19, b'\x01\x03\x01\x01\x01')

    def mc_start_collection(self):
        '''Myo Connect sends this sequence (or a reordering) when starting data
        collection for v1.0 firmware; this enables raw data but disables arm and
        pose notifications.
        '''

        self.write_attr(0x28, b'\x01\x00')  # Suscribe to EMG notifications
        self.write_attr(0x1d, b'\x01\x00')  # Suscribe to IMU notifications
        self.write_attr(0x24, b'\x02\x00')  # Suscribe to classifier indications
        self.write_attr(0x19, b'\x01\x03\x01\x01\x01')  # Set EMG and IMU, payload size = 3, EMG on, IMU on, classifier on
        self.write_attr(0x28, b'\x01\x00')  # Suscribe to EMG notifications
        self.write_attr(0x1d, b'\x01\x00')  # Suscribe to IMU notifications
        self.write_attr(0x19, b'\x09\x01\x01\x00\x00')  # Set sleep mode, payload size = 1, never go to sleep, don't know, don't know
        self.write_attr(0x1d, b'\x01\x00')  # Suscribe to IMU notifications
        self.write_attr(0x19, b'\x01\x03\x00\x01\x00')  # Set EMG and IMU, payload size = 3, EMG off, IMU on, classifier off
        self.write_attr(0x28, b'\x01\x00')  # Suscribe to EMG notifications
        self.write_attr(0x1d, b'\x01\x00')  # Suscribe to IMU notifications
        self.write_attr(0x19, b'\x01\x03\x01\x01\x00')  # Set EMG and IMU, payload size = 3, EMG on, IMU on, classifier off

    def mc_end_collection(self):
        '''Myo Connect sends this sequence (or a reordering) when ending data collection
        for v1.0 firmware; this reenables arm and pose notifications, but
        doesn't disable raw data.
        '''

        self.write_attr(0x28, b'\x01\x00')
        self.write_attr(0x1d, b'\x01\x00')
        self.write_attr(0x24, b'\x02\x00')
        self.write_attr(0x19, b'\x01\x03\x01\x01\x01')
        self.write_attr(0x19, b'\x09\x01\x00\x00\x00')
        self.write_attr(0x1d, b'\x01\x00')
        self.write_attr(0x24, b'\x02\x00')
        self.write_attr(0x19, b'\x01\x03\x00\x01\x01')
        self.write_attr(0x28, b'\x01\x00')
        self.write_attr(0x1d, b'\x01\x00')
        self.write_attr(0x24, b'\x02\x00')
        self.write_attr(0x19, b'\x01\x03\x01\x01\x01')

    def vibrate(self, length):
            # first byte tells it to vibrate; purpose of second byte is unknown (payload size?)
            self.write_attr(0x19, pack('3B', 3, 1, length))

    def set_leds(self, logo, line):
        self.write_attr(0x19, pack('8B', 6, 6, *(logo + line)))

    # def get_battery_level(self):
    #     battery_level = self.read_attr(0x11)
    #     return ord(battery_level.payload[5])

    def add_emg_handler(self, h):
        self.emg_handlers.append(h)

    def add_imu_handler(self, h):
        self.imu_handlers.append(h)

    def add_pose_handler(self, h):
        self.pose_handlers.append(h)

    def add_arm_handler(self, h):
        self.arm_handlers.append(h)

    def add_battery_handler(self, h):
        self.battery_handlers.append(h)

    def on_emg(self, emg, moving):
        for h in self.emg_handlers:
            h(emg, moving)

    def on_imu(self, quat, acc, gyro):
        for h in self.imu_handlers:
            h(quat, acc, gyro)

    def on_pose(self, p):
        for h in self.pose_handlers:
            h(p)

    def on_arm(self, arm, xdir):
        for h in self.arm_handlers:
            h(arm, xdir)

    def on_battery(self, battery_level):
        for h in self.battery_handlers:
            h(battery_level)



######################################################################################################
def myo_thread():
    #global running
    global Emg_total
    global pos_braco

# Start new program here
########################################################################################

    #last_vals = None
    m = MyoRaw(None)
    
    def calc_quat(quat_vec):
        """
        This function calculate the angle of the arm with the shoulder, receiving quartenion information

        Args:
            quat_vec (list): list of four (4) values containing a quartenion regarding the position of the arm  

        Returns:
            current_pitch -> float : return the angle of the arm
        """        
        q0, q1, q2, q3 = quat_vec
        q0 = q0 / 16384.0
        q1 = q1 / 16384.0
        q2 = q2 / 16384.0
        q3 = q3 / 16384.0
        current_pitch = -math.asin(max(-1.0, min(1.0, 2.0 * (q0 * q2 - q3 * q1))))
        return current_pitch
    
    def catch_position(quat, acc, gyro):
        """
        This function receive the Myo information of the imu data quaternion, acceleration and Gyro
        then it calculate the angle of the arm and store the value in a global variable pos_braco

        Args:
            quat (list): list of quartenion of the arm position
            acc (list):  list of the aceleration of the arm
            gyro (list): gyro information of the arm
        """        
        global pos_braco
        angle_pitch = calc_quat(quat)
        pos_braco = angle_pitch


    def proc_emg(emg, moving, times=[]):
        """
        This function receives raw EMG information and store the values if all the channel captures
        the signals and the numper of samples is not completed

        Args:
            emg (list): receive a list with raw emg information
            moving (list): moving information of the Myo -> not used
            times (list, optional): _description_. Defaults to [].
        """        
        global Emg_total
        emg_list_ = list(emg)
        if len(emg_list_) == 8 and len(Emg_total) < 50 :
            Emg_total.append(emg_list_)


    def proc_battery(battery_level):
        """
        This function recives the charge of the battery and set it to red
        if the battery is less than 5%, otherwise it set it to blue

        Args:
            battery_level (int): Charge level of the battery_
        """        
        
        print("Battery level: %d" % battery_level)
        if battery_level < 5:
            m.set_leds([255, 0, 0], [255, 0, 0])
        else:
            m.set_leds([128, 128, 255], [128, 128, 255])

    m.add_emg_handler(proc_emg)
    #m.add_battery_handler(proc_battery)
    m.connect()

    #m.add_arm_handler(lambda arm, xdir: print('arm', arm, 'xdir', xdir))
    # m.add_pose_handler(lambda p: print('pose', p))
    m.add_imu_handler(catch_position)
    #m.add_imu_handler(lambda quat, acc, gyro: print('quaternion', quat))
    #m.sleep_mode(1)
    #m.set_leds([128, 128, 255], [128, 128, 255])  # purple logo and bar LEDs
    #m.vibrate(1)
    Emg_total = []
    try:
        while True:
            m.run(1)

    except KeyboardInterrupt:
        pass
    finally:
            # m.power_off()
            # print("Power off")
        m.disconnect()
        print("Disconnected")
    
    
  
        #print()
            #break
  
# ROS Program starts here
################################################################################################################################################################

class CaptureBracoPositionNode(Node):
    def __init__(self):
        super().__init__("capture_braco_pos")

        self.position_fo_the_arm_publisher_ = self.create_publisher(
            Float64, "braco_pos_publisher", 10)
        self.antebraco_pos_publisher_ = self.create_publisher(
            Float64, "antebraco_pos_publisher", 10)
        
        self.time_to_pub_ = self.create_timer(0.1, self.send_positions)

        self.get_logger().info("capture_braco_position_node has been started")

    #def callback_position(self, msg):
    def send_positions(self):
        """_
        This function create the publishers to send the angles of the arm and the upper-arm
        """        
        braco_to_pub = Float64()
        antebraco_to_pub = Float64()
        global pos_Braco
        global Emg_total
        global emg_
        global quartenion
        global finish_classification
        if len(Emg_total) == 50:
            if pos_braco is None:
                pass
            elif finish_classification:
                finish_classification = False
                antebraco_pos, finish_classification = css.main(new_data=Emg_total)                
                Emg_total = []
                antebraco_to_pub.data = antebraco_pos
                braco_to_pub.data = pos_braco
                #self.get_logger().info("capture_antebraco_position is: " + str(antebraco_pos))
                self.position_fo_the_arm_publisher_.publish(braco_to_pub)
                self.antebraco_pos_publisher_.publish(antebraco_to_pub)

def main(args=None):
    """
    This function create two threads,
    one for capturing the sEMG signals (myo_thread) and the other
    for send the positions of the arm and upper arm (ros2_thread)
    """    
    threading.Thread(target=ros2_thread).start()
    threading.Thread(target=myo_thread).start()

###################################################################################################################################
# Threads
def ros2_thread(args=None):
    rclpy.init(args=args)
    node = CaptureBracoPositionNode()
    rclpy.spin(node)
    rclpy.shutdown()

##############################################################################################################3

if __name__ == "__main__":
    main()
