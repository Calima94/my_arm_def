'''
	Original by dzhu
		https://github.com/dzhu/myo-raw

	Edited by Fernando Cosentino
		http://www.fernandocosentino.net/pyoconnect
'''

import rclpy
import time
import math
from functools import partial
from rclpy.node import Node
from example_interfaces.msg import Float64
from my_robot_interfaces.srv import SendPosition


class MyoRawNode(Node):
    def __init__(self):
        super().__init__("myo_raw")
        self.positions_to_use = [0.0, 90.0, 120.0, 135.0, 150.0]
        self.braco_pos = 0.0
        self.antebraco_pos = 0.0
        self.first_time = 0
        self.braco_first_position = 0.0

        self.position_braco_subscriber = self.create_subscription(
            Float64, "braco_pos_publisher", self.callback_braco_pos, 10)

        self.position_antebraco_subscriber = self.create_subscription(
            Float64, "antebraco_pos_publisher", self.callback_antebraco_pos,
            10)

        self.get_logger().info("Myo raw node has been started")

    def callback_braco_pos(self, msg):
        self.braco_pos = msg.data
        #self.get_logger().info("The position of arm is " + str(self.braco_pos))
        if (self.first_time == 0 and self.braco_pos != 0.0):
            self.braco_first_position = self.braco_pos
            self.get_logger().info('A posicao do braco eh: nao iniciada ')
            self.first_time += 1
        elif (self.first_time != 0):
            new_pos = self.braco_pos
            pos_atual_braco = new_pos - self.braco_first_position
            #print("braco_pos" + str(pos_atual_braco))
            pos_braco_degree = math.degrees(pos_atual_braco)
            self.get_logger().info('A posicao do braco eh: ' +
                                   str(pos_braco_degree) + 'graus')
            self.call_send_position_wanted(pos_atual_braco)

    def callback_antebraco_pos(self, msg):
        self.antebraco_pos = msg.data
        pos_antebraco_degree = self.positions_to_use[int(msg.data)]
        pos_antebraco_rad = math.radians(pos_antebraco_degree)
        self.get_logger().info('A posicao do antebraco eh: ' +
                                   str(pos_antebraco_degree) + 'graus')
        self.call_send_position_wanted_1(pos_antebraco_rad)


    def call_send_position_wanted(self, a):
        client = self.create_client(SendPosition, "pos_reach")
        while not client.wait_for_service(1.0):
            #self.get_logger().warn("Waiting for Server Pos Reach...")
            pass
        request = SendPosition.Request()
        request.position = a
        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_Send_Target_Position, a=a))

    def callback_Send_Target_Position(self, future, a):
        try:
            responses = future.success
            responsem = future.msg
            #self.get_logger().info("The menssage send was " + str(responses) + " " +
            #responsem + " at position: " + str(a))
        except:
            pass

    def call_send_position_wanted_1(self, a):
        client = self.create_client(SendPosition, "pos_reach_1")
        while not client.wait_for_service(1.0):
            #self.get_logger().warn("Waiting for Server Pos Reach...")
            pass
        request = SendPosition.Request()
        request.position = a
        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_Send_Target_Position_1, a=a))

    def callback_Send_Target_Position_1(self, future, a):
        try:
            responses = future.success
            responsem = future.msg
            #self.get_logger().info("The menssage send was " + str(responses) + " " +
            #responsem + " at position: " + str(a))
        except:
            pass

    def call_send_position_wanted_2(self, a):
        client = self.create_client(SendPosition, "pos_reach_2")
        while not client.wait_for_service(1.0):
            #self.get_logger().warn("Waiting for Server Pos Reach...")
            pass
        request = SendPosition.Request()
        request.position = a
        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_Send_Target_Position_2, a=a))

    def callback_Send_Target_Position_2(self, future, a):
        try:
            responses = future.success
            responsem = future.msg
            #self.get_logger().info("The menssage send was " + str(responses) + " " + responsem + " at position: " + str(a))
        except:
            pass

    def call_send_position_wanted_3(self, a):
        client = self.create_client(SendPosition, "pos_reach_3")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Pos Reach...")
            pass
        request = SendPosition.Request()
        request.position = a
        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_Send_Target_Position_3, a=a))

    def callback_Send_Target_Position_3(self, future, a):
        try:
            responses = future.success
            responsem = future.msg
            #self.get_logger().info("The menssage send was " + str(responses) + " " + responsem + " at position: " + str(a))
        except:
            pass


def main(args=None):
    rclpy.init(args=None)
    node = MyoRawNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
