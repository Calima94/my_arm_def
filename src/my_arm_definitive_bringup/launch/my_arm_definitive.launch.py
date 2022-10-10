import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = LaunchDescription()
    config = os.path.join(
        get_package_share_directory('my_arm_definitive_bringup'),
        'config',
        'params.yaml'
        )

    spawn_arm_node = Node(
        package="my_arm_def_py_pkg",
        executable="spawn_arm",
    )

    arm_controller_node = Node(
        package="my_arm_def_py_pkg",
        executable="arm_controller",
        parameters=[config]
    )

    myo_raw_node = Node(
       package="my_arm_def_py_pkg",
      executable="myo_raw",
    )

    capture_braco_pos_node = Node(package="my_arm_def_py_pkg",
                                  executable="capture_braco_pos")
    
    #ld.add_action(ExecuteProcess(cmd=['gazebo','-s','libgazebo_ros_factory.so'],output='screen'))
    #ld.add_action(ExecuteProcess( cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'], output='screen'))
    ld.add_action(ExecuteProcess( cmd=['gazebo', '-s', 'libgazebo_ros_factory.so'], output='screen'))
    ld.add_action(spawn_arm_node)
    ld.add_action(arm_controller_node)
    ld.add_action(myo_raw_node)
    ld.add_action(capture_braco_pos_node)

    return ld