cmake_minimum_required(VERSION 3.5)
project(my_arm_def_cpp_pkg)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  # we dont use add_compile_options with pedantic in message packages
  # because the Python C extensions dont comply with it
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")
endif()


find_package(ament_cmake REQUIRED)
find_package(gazebo_dev REQUIRED)
find_package(gazebo_msgs REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)

include_directories(include
  ${gazebo_dev_INCLUDE_DIRS}
  ${gazebo_ros_INCLUDE_DIRS}
  ${geometry_msgs_INCLUDE_DIRS}
  ${sensor_msgs_INCLUDE_DIRS}
  ${sensor_msgs_INCLUDE_DIRS}
  ${example_interfaces_INCLUDE_DIRS}
)

link_directories(${gazebo_dev_LIBRARY_DIRS})

# gazebo_ros_joint_state_publisher
add_library(arm_control SHARED
  src/arm_control.cpp
)
ament_target_dependencies(arm_control
  "gazebo_dev"
  "gazebo_ros"
  "rclcpp"
  "sensor_msgs"
  "example_interfaces"
)

ament_export_libraries(arm_control)


install(DIRECTORY include/
        DESTINATION include)


install(TARGETS
  arm_control
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

install(DIRECTORY
  worlds
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
