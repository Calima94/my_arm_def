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
import numpy as np

##########################################################################################################################
#positions_to_use = [180.0, 90.0, 60.0, 45.0, 30.0]
antebraco = None
braco_pos = None
##############################################################################################################################
Emg_total = []
data_to_class = []
quartenion = []
old_EMG = []
new_emg_ = []
emg_ = None
running = 0

#################################################################################################################
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
            if c in [0x00, 0x80, 0x08, 0x88]:
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
        #self.imu_handlers = []
        #self.arm_handlers = []
        #self.pose_handlers = []

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
        #print('firmware version: %d.%d.%d.%d' % (v0, v1, v2, v3))

        name = self.read_attr(0x03)
        #print('device name: %s' % name.payload)

        # enable IMU data
        self.write_attr(0x1d, b'\x01\x00')
        # enable on/off arm notifications
        self.write_attr(0x24, b'\x02\x00')

        self.write_attr(0x19, b'\x01\x03\x00\x01\x01')
        
        self.start_raw()
        
        self.write_attr(0x12, b'\x01\x10')

        # add data handlers
        def calc_quat(quat_vec):
            q0, q1, q2, q3 = quat_vec
            q0 = q0 / 16384.0
            q1 = q1 / 16384.0
            q2 = q2 / 16384.0
            q3 = q3 / 16384.0
            current_pitch = -math.asin(
                max(-1.0, min(1.0, 2.0 * (q0 * q2 - q3 * q1))))
            return current_pitch

        def catch_position(quat_):
            angle_pitch = 0.0
            if (len(quat_) != 0):
                angle_pitch = calc_quat(quat_)
            return angle_pitch
    
        
        def handle_data(p):
            if (p.cls, p.cmd) != (4, 5):
                return

            c, attr, typ = unpack('BHB', p.payload[:4])
            pay = p.payload[5:]
            #global quartenion
            #global list_emg
            global Emg_total
            global quartenion
            global braco_pos

            if attr == 0x27:
                vals = unpack('8HB', pay)
                # not entirely sure what the last byte is, but it's a bitmask that
                # seems to indicate which sensors think they're being moved around or
                # something
                #global emg
                emg = vals[:8]
                moving = vals[8]
                list_emg = list(emg)
                
                if (len(Emg_total) < 50 and len(list_emg)==8):
                   Emg_total.append(list_emg)
                
                elif (len(Emg_total) == 50):
                    braco_pos = catch_position(quartenion)
                    
                
                self.on_emg(emg_, moving)

            elif attr == 0x1c:
                vals = unpack('10h', pay)
                quat = vals[:4]
                #acc = vals[4:7],
                #gyro = vals[7:10]
                
                quartenion = list(quat)
                #braco_pos = catch_position(quartenion_)
                #self.on_imu(quat, acc, gyro)
            elif attr == 0x23:
                typ, val, xdir, _, _, _ = unpack('6B', pay)

                #if typ == 1:  # on arm
                 #   self.on_arm(Arm(val), XDirection(xdir))
                #elif typ == 2:  # removed from arm
                    #self.on_arm(Arm.UNKNOWN, XDirection.UNKNOWN)
                #elif typ == 3:  # pose
                    #self.on_pose(Pose(val))
                    #global position_arm_
                    #position_arm_ = val
                    #print(f'A posicao no submodulo e: {val}')
                    #return val
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

    def start_raw(self):
        '''Sending this sequence for v1.0 firmware seems to enable both raw data and
        pose notifications.
        '''

        self.write_attr(0x28, b'\x01\x00')
        self.write_attr(0x19, b'\x01\x03\x01\x01\x00')
        self.write_attr(0x19, b'\x01\x03\x01\x01\x01')

    def mc_start_collection(self):
        '''Myo Connect sends this sequence (or a reordering) when starting data
        collection for v1.0 firmware; this enables raw data but disables arm and
        pose notifications.
        '''

        self.write_attr(0x28, b'\x01\x00')
        self.write_attr(0x1d, b'\x01\x00')
        self.write_attr(0x24, b'\x02\x00')
        self.write_attr(0x19, b'\x01\x03\x01\x01\x01')
        self.write_attr(0x28, b'\x01\x00')
        self.write_attr(0x1d, b'\x01\x00')
        self.write_attr(0x19, b'\x09\x01\x01\x00\x00')
        self.write_attr(0x1d, b'\x01\x00')
        self.write_attr(0x19, b'\x01\x03\x00\x01\x00')
        self.write_attr(0x28, b'\x01\x00')
        self.write_attr(0x1d, b'\x01\x00')
        self.write_attr(0x19, b'\x01\x03\x01\x01\x00')

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

    #def vibrate(self, length):
        #if length in range(1, 4):
            # first byte tells it to vibrate; purpose of second byte is unknown
            #self.write_attr(0x19, pack('3B', 3, 1, length))

    def add_emg_handler(self, h):
        self.emg_handlers.append(h)

    #def add_imu_handler(self, h):
        #self.imu_handlers.append(h)

    #def add_pose_handler(self, h):
       # self.pose_handlers.append(h)

    def add_arm_handler(self, h):
        self.arm_handlers.append(h)

    def on_emg(self, emg, moving):
        for h in self.emg_handlers:
            h(emg, moving)

    #def on_imu(self, quat, acc, gyro):
        #for h in self.imu_handlers:
            #h(quat, acc, gyro)

    #def on_pose(self, p):
        #for h in self.pose_handlers:
            #h(p)

    #def on_arm(self, arm, xdir):
       # for h in self.arm_handlers:
          #  h(arm, xdir)



######################################################################################################
def myo_thread():
    #global running
    m = MyoRaw(None)
    m.connect()
    try:
        while True:
            m.run(1)

    except KeyboardInterrupt:
        pass
    finally:
        #print()
        print("Disconnecting...")
        m.disconnect()
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
        
        self.time_to_pub_ = self.create_timer(1.0, self.send_positions)

        self.get_logger().info("capture_braco_position_node has been started")

    #def callback_position(self, msg):
    def send_positions(self):
        braco_to_pub = Float64()
        antebraco_to_pub = Float64()
        global braco_pos
        global Emg_total
        global old_EMG
        global emg_
        global quartenion
        if old_EMG != Emg_total:
            if len(Emg_total) == 50:
                if braco_pos is None:
                    pass
                else:
                    old_EMG = Emg_total
                    #np.savetxt("foo_teste_2.csv", Emg_total, delimiter=",")
                    #self.get_logger().info("Total EMG is: " + str(Emg_total))
                    antebraco_pos = css.main(new_data=Emg_total)
                    Emg_total = []
                    antebraco_to_pub.data = antebraco_pos
                    braco_to_pub.data = braco_pos
                    self.get_logger().info("capture_antebraco_position is: " + str(antebraco_pos))
                    self.position_fo_the_arm_publisher_.publish(braco_to_pub)
                    self.antebraco_pos_publisher_.publish(antebraco_to_pub)

def main(args=None):
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
