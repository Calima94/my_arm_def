from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess


def generate_launch_description():
    ld = LaunchDescription()

    spawn_arm_node = Node(
        package="my_arm_def_py_pkg",
        executable="spawn_arm",
    )

    arm_controller_node = Node(
        package="my_arm_def_py_pkg",
        executable="arm_controller",
    )

    myo_raw_node = Node(
       package="my_arm_def_py_pkg",
      executable="myo_raw",
    )

    capture_braco_pos_node = Node(package="my_arm_def_py_pkg",
                                  executable="capture_braco_pos")

    ld.add_action(spawn_arm_node)
    ld.add_action(arm_controller_node)
    ld.add_action(myo_raw_node)
    ld.add_action(capture_braco_pos_node)

    return ld