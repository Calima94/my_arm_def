#!/usr/bin/env python3
import rclpy
import time
from rclpy.node import Node
from example_interfaces.msg import Float64
from my_arm_def_interfaces.srv import SendPosition
#import pandas as pd


class ArmControllerNode(Node):
    def __init__(self):
        super().__init__("arm_controller")
        self.pos_ = 0.0
        self.vel_ = 0.0
        self.vel_atual_ = 0.0
        self.dest_ = 0.0
        self.dist_to_go_ = 0.0
        self.kd_ = 0.1
        self.kp_ = 10.0

        self.pos_1 = 0.0
        self.vel_1 = 0.0
        self.vel_atual_1 = 0.0
        self.dest_1 = 0.0
        self.dist_to_go_1 = 0.0
        self.kd_1 = 0.1
        self.kp_1 = 1.0

        self.pos_2 = 0.0
        self.vel_2 = 0.0
        self.vel_atual_2 = 0.0
        self.dest_2 = 0.0
        self.dist_to_go_2 = 0.0
        self.kd_2 = 0.1
        self.kp_2 = 10.0

        self.pos_3 = 0.0
        self.vel_3 = 0.0
        self.vel_atual_3 = 0.0
        self.dest_3 = 0.0
        self.dist_to_go_3 = 0.0
        self.kd_3 = 0.1
        self.kp_3 = 10.0

        self.data_now_to_pub = []

        self.first_time = time.time()

        #self.publish_frequency_ = 1000.00
        #self.timer_to_pub_ = self.create_timer(0.1,self.pub_infs_)

        self.velocity_publisher_ = self.create_publisher(Float64, "number", 10)

        self.velocity_publisher_1 = self.create_publisher(
            Float64, "number_1", 10)

        self.velocity_publisher_2 = self.create_publisher(
            Float64, "number_2", 10)

        self.velocity_publisher_3 = self.create_publisher(
            Float64, "number_3", 10)

        self.position_server = self.create_service(SendPosition, "pos_reach",
                                                   self.callbackPos_Reach)

        self.position_server_1 = self.create_service(SendPosition,
                                                     "pos_reach_1",
                                                     self.callbackPos_Reach_1)

        self.position_server_2 = self.create_service(SendPosition,
                                                     "pos_reach_2",
                                                     self.callbackPos_Reach_2)

        self.position_server_3 = self.create_service(SendPosition,
                                                     "pos_reach_3",
                                                     self.callbackPos_Reach_3)

        self.position_subscriber_ = self.create_subscription(
            Float64, "joint_states", self.callback_position, 10)

        self.position_subscriber_1 = self.create_subscription(
            Float64, "joint_states_1", self.callback_position_1, 10)

        self.position_subscriber_2 = self.create_subscription(
            Float64, "joint_states_2", self.callback_position_2, 10)

        self.position_subscriber_3 = self.create_subscription(
            Float64, "joint_states_3", self.callback_position_3, 10)

        self.velocity_subscriber_ = self.create_subscription(
            Float64, "inst_vel", self.callback_velocity, 10)

        self.velocity_subscriber_1 = self.create_subscription(
            Float64, "inst_vel_1", self.callback_velocity_1, 10)

        self.velocity_subscriber_2 = self.create_subscription(
            Float64, "inst_vel_2", self.callback_velocity_2, 10)

        self.velocity_subscriber_3 = self.create_subscription(
            Float64, "inst_vel_3", self.callback_velocity_3, 10)

        self.get_logger().info("Arm controller has been started.")

    #def pub_infs_(self):
    #time_now = time.time()
    #diff_time = time_now - self.first_time
    #data_now = [diff_time,self.pos_,self.pos_1,self.vel_atual_,self.vel_atual_1]
    #self.data_now_to_pub.append(data_now)

    #if (len(self.data_now_to_pub) == 1200):
    #   df = pd.DataFrame(self.data_now_to_pub)
    #  df.columns = ['time', 'joint1','joint2','vel_joint1','vel_joint2']
    # df.to_excel("dados_teste_juntas.xlsx")
    #self.get_logger().info("Dados salvos")

    def callback_velocity(self, msg):
        self.vel_atual_ = msg.data

    def callback_velocity_1(self, msg):
        self.vel_atual_1 = msg.data

    def callback_velocity_2(self, msg):
        self.vel_atual_2 = msg.data

    def callback_velocity_3(self, msg):
        self.vel_atual_3 = msg.data

    def callbackPos_Reach(self, request, response):
        self.dest_ = request.position
        # self.get_logger().info(str(request.position))
        response.success = True
        response.msg = "The position was send successfully"
        return response

    def callbackPos_Reach_1(self, request, response):
        self.dest_1 = request.position
        # self.get_logger().info(str(request.position))
        response.success = True
        response.msg = "The position was send successfully"
        return response

    def callbackPos_Reach_2(self, request, response):
        self.dest_2 = request.position
        # self.get_logger().info(str(request.position))
        response.success = True
        response.msg = "The position was send successfully"
        return response

    def callbackPos_Reach_3(self, request, response):
        self.dest_3 = request.position
        # self.get_logger().info(str(request.position))
        response.success = True
        response.msg = "The position was send successfully"
        return response

    def callback_position(self, msg):
        self.pos_ = msg.data
        self.dist_to_go_ = self.dest_ - self.pos_
        self.vel_ = self.kp_ * self.dist_to_go_ + self.vel_atual_ * self.kd_ * self.dist_to_go_
        #self.publish_velocity(self.vel_)
        self.publish_velocity(self.dist_to_go_)
        #self.dest_ = panel.main()

    def callback_position_1(self, msg):
        self.pos_1 = msg.data
        self.dist_to_go_1 = self.dest_1 - self.pos_1
        self.vel_1 = self.kp_1 * self.dist_to_go_1 + self.vel_atual_1 * self.kd_1 * self.dist_to_go_1
        self.publish_velocity_1(self.vel_1)

    def callback_position_2(self, msg):
        self.pos_2 = msg.data
        self.dist_to_go_2 = self.dest_2 - self.pos_2
        self.vel_2 = self.kp_2 * self.dist_to_go_2 + self.vel_atual_2 * self.kd_2 * self.dist_to_go_2
        #self.vel_2 = self.kp_2 * self.dist_to_go_2
        self.publish_velocity_2(self.vel_2)
        #self.publish_velocity_2(self.dest_2)
        #self.publish_velocity_3(-self.dest_2*10.00)

    def callback_position_3(self, msg):
        self.pos_3 = msg.data
        self.dist_to_go_3 = self.dest_3 - self.pos_3
        self.vel_3 = self.kp_3 * self.dist_to_go_3 + self.vel_atual_3 * self.kd_3 * self.dist_to_go_3
        #self.vel_3 = self.kp_3 * self.dist_to_go_3
        self.publish_velocity_3(self.vel_3)
        #self.publish_velocity_3(self.dest_3)

    def publish_velocity(self, vel_to_publish):
        msg = Float64()
        msg.data = vel_to_publish
        self.velocity_publisher_.publish(msg)

    def publish_velocity_1(self, vel_to_publish):
        msg = Float64()
        msg.data = vel_to_publish
        self.velocity_publisher_1.publish(msg)

    def publish_velocity_2(self, vel_to_publish):
        msg = Float64()
        #msg1 = Float64()
        msg.data = vel_to_publish
        #msg1.data = -vel_to_publish
        self.velocity_publisher_2.publish(msg)
        #self.velocity_publisher_3.publish(msg1)

    def publish_velocity_3(self, vel_to_publish):
        msg = Float64()
        msg.data = vel_to_publish
        self.velocity_publisher_3.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = ArmControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
