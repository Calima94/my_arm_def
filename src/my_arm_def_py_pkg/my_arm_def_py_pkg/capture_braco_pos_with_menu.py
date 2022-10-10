import PySimpleGUI as sg
import rclpy
import threading
from functools import partial
from rclpy.node import Node
from example_interfaces.msg import Float64
from my_robot_interfaces.srv import SendPosition
import threading
position_wanted = 0.0
position_wanted_1 = 0.0
position_wanted_2 = 0.0
position_wanted_3 = 0.0

actual_position = 0.0
actual_position_1 = 0.0
actual_position_2 = 0.0
actual_position_3 = 0.0


class PanelNode(Node):
    def __init__(self):
        super().__init__("panel")
        self.check_frequency_ = 10
        self.last_pos_send_ = 0.0
        self.last_pos_send_1 = 0.0
        self.last_pos_send_2 = 0.0
        # self.velocity_publisher_ = self.create_publisher(
        # Float64, "reach_pos", 10)

        self.position_subscriber_ = self.create_subscription(
            Float64, "joint_states", self.callback_position, 10)

        self.position_subscriber_1 = self.create_subscription(
            Float64, "joint_states_1", self.callback_position_1, 10)

        self.position_subscriber_2 = self.create_subscription(
            Float64, "joint_states_2", self.callback_position_2, 10)

        self.position_subscriber_3 = self.create_subscription(
            Float64, "joint_states_3", self.callback_position_3, 10)

        # self.msg_timer = self.create_timer(1.0,self.publish_pos)
        self.position_check_timer_ = self.create_timer(
            1.0 / self.check_frequency_, self.check_for_updates)
        self.position_check_timer_1 = self.create_timer(
            1.0 / self.check_frequency_, self.check_for_updates_1)
        self.position_check_timer_2 = self.create_timer(
            1.0 / self.check_frequency_, self.check_for_updates_2)

        self.get_logger().info("Panel Node has been started")

    def check_for_updates(self):
        global position_wanted
        if (self.last_pos_send_ != position_wanted):
            self.call_send_position_wanted(position_wanted)
            self.last_pos_send_ = position_wanted
        else:
            pass

    def call_send_position_wanted(self, a):
        client = self.create_client(SendPosition, "pos_reach")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Pos Reach...")

        request = SendPosition.Request()
        request.position = a
        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_Send_Target_Position, a=a))

    def callback_Send_Target_Position(self, future, a):
        try:
            responses = future.success
            responsem = future.msg
            self.get_logger().info("The menssage send was " + str(responses) +
                                   " " + responsem + " at position: " + str(a))
        except:
            pass

    def check_for_updates_1(self):
        global position_wanted_1
        if (self.last_pos_send_1 != position_wanted_1):
            self.call_send_position_wanted_1(position_wanted_1)
            self.last_pos_send_1 = position_wanted_1
        else:
            pass

    def call_send_position_wanted_1(self, a):
        client = self.create_client(SendPosition, "pos_reach_1")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Pos Reach...")

        request = SendPosition.Request()
        request.position = a
        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_Send_Target_Position_1, a=a))

    def callback_Send_Target_Position_1(self, future, a):
        try:
            responses = future.success
            responsem = future.msg
            self.get_logger().info("The menssage send was " + str(responses) +
                                   " " + responsem + " at position: " + str(a))
        except:
            pass

    def check_for_updates_2(self):
        global position_wanted_2
        if (self.last_pos_send_2 != position_wanted_2):
            self.call_send_position_wanted_2(position_wanted_2)
            self.call_send_position_wanted_3(-position_wanted_2)
            self.last_pos_send_2 = position_wanted_2
        else:
            pass

    def call_send_position_wanted_2(self, a):
        client = self.create_client(SendPosition, "pos_reach_2")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Pos Reach...")

        request = SendPosition.Request()
        request.position = a
        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_Send_Target_Position_2, a=a))

    def callback_Send_Target_Position_2(self, future, a):
        try:
            responses = future.success
            responsem = future.msg
            self.get_logger().info("The menssage send was " + str(responses) +
                                   " " + responsem + " at position: " + str(a))
        except:
            pass

    def call_send_position_wanted_3(self, a):
        client = self.create_client(SendPosition, "pos_reach_3")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Pos Reach...")

        request = SendPosition.Request()
        request.position = a
        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_Send_Target_Position_3, a=a))

    def callback_Send_Target_Position_3(self, future, a):
        try:
            responses = future.success
            responsem = future.msg
            self.get_logger().info("The menssage send was " + str(responses) +
                                   " " + responsem + " at position: " + str(a))
        except:
            pass

    def callback_position(self, msg):
        global actual_position
        actual_position = msg

    def callback_position_1(self, msg):
        global actual_position_1
        actual_position_1 = msg

    #def callback_position_2(self, msg):
    #    global actual_position_2
    #    actual_position_2 = msg

    #def callback_position_3(self, msg):
    #    global actual_position_3
    #    actual_position_3 = msg

    # def publish_pos (self):
    #new_msg = Float64()
    #global position_wanted
    # new_msg.data = position_wanted
    # self.velocity_publisher_.publish(new_msg)





def main(args=None):
    threading.Thread(target=ros2).start()
    threading.Thread(target=simple_panel).start()


def ros2(args=None):
    rclpy.init(args=args)
    node = PanelNode()
    rclpy.spin(node)
    rclpy.shutdown()


def simple_panel(args=None):
    tela = TelaPython()
    position = tela.Iniciar()


if __name__ == "__main__":
    main()
