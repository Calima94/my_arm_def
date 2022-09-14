import os
import sys
import rclpy
from ament_index_python.packages import get_package_share_directory
from gazebo_msgs.srv import SpawnEntity


def main():
    """ Main for spwaning turtlebot node """
    # Get input arguments from user

    #argv = sys.argv[1:]

    # Start node
    rclpy.init()
    node = rclpy.create_node("spawn_arm")
    
    #Declare parameters
    node.declare_parameter("name", "braco_antebraco_garra")
    node.declare_parameter("namespace", "")
    node.declare_parameter("pos_init_x", 0.0)
    node.declare_parameter("pos_init_y", 0.0)
    node.declare_parameter("pos_init_z", 0.0)

    node.name_ = node.get_parameter("name").value
    node.namespace_ = node.get_parameter("namespace").value
    node.pos_x_ = node.get_parameter("pos_init_x").value
    node.pos_y_ = node.get_parameter("pos_init_y").value
    node.pos_z_ = node.get_parameter("pos_init_z").value

    node.get_logger().info(
        'Creating Service client to connect to `/spawn_entity`')
    client = node.create_client(SpawnEntity, "/spawn_entity")

    node.get_logger().info("Connecting to `/spawn_entity` service...")
    if not client.service_is_ready():
        client.wait_for_service()
        node.get_logger().info("...connected!")

    # Get path to the turtlebot3 burgerbot
    #sdf_file_path = "/home/caio/ros2_ws/src/my_arm/models/model.sdf"
    #sdf_file_path = "/home/caio/ros2_ws/src/my_arm/models/braco_e_antebraco_2.sdf"
    sdf_file_path = "/home/caio/my_arm_def/src/my_arm_def_cpp_pkg/models/braco_antebraco_garra.sdf"
    # Set data for request
    request = SpawnEntity.Request()
    #request.name = argv[0]
    request.name = node.name_
    request.xml = open(sdf_file_path, 'r').read()
    #request.robot_namespace = argv[1]
    request.robot_namespace = node.namespace_
    #request.initial_pose.position.x = float(argv[2])
    request.initial_pose.position.x = node.pos_x_
    #request.initial_pose.position.y = float(argv[3])
    request.initial_pose.position.y = node.pos_y_
    #request.initial_pose.position.z = float(argv[4])
    request.initial_pose.position.z = node.pos_z_

    node.get_logger().info("Sending service request to `/spawn_entity`")
    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)
    if future.result() is not None:
        print('response: %r' % future.result())
    else:
        raise RuntimeError('exception while calling service: %r' %
                           future.exception())

    node.get_logger().info("Done! Shutting down node.")
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
