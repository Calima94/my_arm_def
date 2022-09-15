// Copyright 2018 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <gazebo/common/Events.hh>
#include <gazebo/common/Time.hh>
#include <gazebo/physics/Joint.hh>
#include <gazebo/physics/Model.hh>
#include <gazebo/physics/World.hh>
#include <gazebo_plugins/gazebo_ros_joint_command.hpp>
#include <gazebo_ros/conversions/builtin_interfaces.hpp>
#include <gazebo_ros/node.hpp>
#include <rclcpp/rclcpp.hpp>
//#include <sensor_msgs/msg/joint_state.hpp>
#include <geometry_msgs/msg/vector3.hpp>
#include <example_interfaces/msg/float64.hpp>

#include <memory>
#include <string>
#include <vector>

namespace gazebo_plugins
{
/// Class to hold private data members (PIMPL pattern)
class GazeboRosJointCommandPrivate
{
public:


            ///Functions in general

  /// Callback to be called at every simulation iteration.
  // \param[in] info Updated simulation info.
  void OnUpdate(const gazebo::common::UpdateInfo & info);

  void callbackNumber(const example_interfaces::msg::Float64::SharedPtr msg);

  void callbackNumber_1(const example_interfaces::msg::Float64::SharedPtr msg);

  void callbackNumber_2(const example_interfaces::msg::Float64::SharedPtr msg);

  void callbackNumber_3(const example_interfaces::msg::Float64::SharedPtr msg);


  ///ROS stuff (node, publishers, subscribers, services, server)

  /// Node for ROS communication.
  gazebo_ros::Node::SharedPtr ros_node_;

  /// Joint state publisher.
  rclcpp::Publisher<example_interfaces::msg::Float64>::SharedPtr joint_state_pub_;

  rclcpp::Publisher<example_interfaces::msg::Float64>::SharedPtr joint_state_pub_1;

  rclcpp::Publisher<example_interfaces::msg::Float64>::SharedPtr joint_state_pub_2;

  rclcpp::Publisher<example_interfaces::msg::Float64>::SharedPtr joint_state_pub_3;

  /// Joint velocity publisher.
  rclcpp::Publisher<example_interfaces::msg::Float64>::SharedPtr joint_inst_vel_;

  rclcpp::Publisher<example_interfaces::msg::Float64>::SharedPtr joint_inst_vel_1;

  rclcpp::Publisher<example_interfaces::msg::Float64>::SharedPtr joint_inst_vel_2;

  rclcpp::Publisher<example_interfaces::msg::Float64>::SharedPtr joint_inst_vel_3;


  /// Joint Subscription
  rclcpp::Subscription<example_interfaces::msg::Float64>::SharedPtr joint_state_subs_;

  rclcpp::Subscription<example_interfaces::msg::Float64>::SharedPtr joint_state_subs_1;

  rclcpp::Subscription<example_interfaces::msg::Float64>::SharedPtr joint_state_subs_2;

  rclcpp::Subscription<example_interfaces::msg::Float64>::SharedPtr joint_state_subs_3;

  ///Gazebo stuff (joints, updates, connections)

  /// Joints being tracked.
  std::vector<gazebo::physics::JointPtr> joints_;

  /// Keep last time an update was published
  gazebo::common::Time last_update_time_;

  /// Connection to world update event. Callback is called while this is alive.
  gazebo::event::ConnectionPtr update_connection_;

            ///Variables

  /// Period in seconds
  double update_period_;

  ///Velocity of the joint
  double vel_;
  
  double vel_1;

  double vel_2;

  double vel_3;

  double inst_vel_;

  double inst_vel_1;

  double inst_vel_2;

  double inst_vel_3;


};

            ///Constructor

GazeboRosJointCommand::GazeboRosJointCommand()
: impl_(std::make_unique<GazeboRosJointCommandPrivate>())
{
}

        ///Deconstructor

GazeboRosJointCommand::~GazeboRosJointCommand()
{
}

        ///Load Function

void GazeboRosJointCommand::Load(gazebo::physics::ModelPtr model, sdf::ElementPtr sdf)
{
  // Create a GazeboRos node instead of a common ROS node.
  // Pass it SDF parameters so common options like namespace and remapping
  // can be handled.
  impl_->ros_node_ = gazebo_ros::Node::Get(sdf);


  // Make sure the joint_name parameter is avaliable in plugin
  // Joints
  if (!sdf->HasElement("joint_name")) {
    RCLCPP_ERROR(impl_->ros_node_->get_logger(), "Plugin missing <joint_name>s");
    impl_->ros_node_.reset();
    return;
  }

  //Make sure that the joint exists
  sdf::ElementPtr joint_elem = sdf->GetElement("joint_name");
  while (joint_elem) {
    auto joint_name = joint_elem->Get<std::string>();

    auto joint = model->GetJoint(joint_name);
    if (!joint) {
      RCLCPP_ERROR(impl_->ros_node_->get_logger(), "Joint %s does not exist!", joint_name.c_str());
    } else {
      impl_->joints_.push_back(joint);
      RCLCPP_INFO(impl_->ros_node_->get_logger(), "Going to publish joint [%s]",
        joint_name.c_str() );
    }

    joint_elem = joint_elem->GetNextElement("joint_name");
  }

  //If there is no joints the plugin ends
  if (impl_->joints_.empty()) {
    RCLCPP_ERROR(impl_->ros_node_->get_logger(), "No joints found.");
    impl_->ros_node_.reset();
    return;
  }

    // Update rate
  double update_rate = 1000.0;
  if (!sdf->HasElement("update_rate")) {
    RCLCPP_INFO(impl_->ros_node_->get_logger(), "Missing <update_rate>, defaults to %f",
      update_rate);
  } else {
    update_rate = sdf->GetElement("update_rate")->Get<double>();
  }

  if (update_rate > 0.0) {
    impl_->update_period_ = 1.0 / update_rate;
  } else {
    impl_->update_period_ = 0.0;
  }
  
  //Update the SimTime in Gazebo
  impl_->last_update_time_ = model->GetWorld()->SimTime();


  //declare the default velocity of the joint
  impl_->vel_ = 0.0;

  // Define the joint_state_publisher
  impl_->joint_state_pub_ = impl_->ros_node_->create_publisher<example_interfaces::msg::Float64>(
    "joint_states", 1000);

  impl_->joint_state_pub_1 = impl_->ros_node_->create_publisher<example_interfaces::msg::Float64>(
    "joint_states_1", 1000);
  
  impl_->joint_state_pub_2 = impl_->ros_node_->create_publisher<example_interfaces::msg::Float64>(
    "joint_states_2", 1000);
  
  impl_->joint_state_pub_3 = impl_->ros_node_->create_publisher<example_interfaces::msg::Float64>(
    "joint_states_3", 1000);

  //Publish velocity of the robot

  impl_->joint_inst_vel_ = impl_->ros_node_->create_publisher<example_interfaces::msg::Float64>(
    "inst_vel", 1000);

  impl_->joint_inst_vel_1 = impl_->ros_node_->create_publisher<example_interfaces::msg::Float64>(
    "inst_vel_1", 1000);
  
  impl_->joint_inst_vel_2 = impl_->ros_node_->create_publisher<example_interfaces::msg::Float64>(
    "inst_vel_2", 1000);
  
  impl_->joint_inst_vel_3 = impl_->ros_node_->create_publisher<example_interfaces::msg::Float64>(
    "inst_vel_3", 1000);

  //Define the joint_state_subscriber
  impl_->joint_state_subs_ = impl_->ros_node_->create_subscription<example_interfaces::msg::Float64>(
    "number",10,std::bind(&GazeboRosJointCommandPrivate::callbackNumber, impl_.get(), std::placeholders::_1));

  impl_->joint_state_subs_1 = impl_->ros_node_->create_subscription<example_interfaces::msg::Float64>(
    "number_1",10,std::bind(&GazeboRosJointCommandPrivate::callbackNumber_1, impl_.get(), std::placeholders::_1));

  impl_->joint_state_subs_2 = impl_->ros_node_->create_subscription<example_interfaces::msg::Float64>(
    "number_2",10,std::bind(&GazeboRosJointCommandPrivate::callbackNumber_2, impl_.get(), std::placeholders::_1));

  impl_->joint_state_subs_3 = impl_->ros_node_->create_subscription<example_interfaces::msg::Float64>(
   "number_3",10,std::bind(&GazeboRosJointCommandPrivate::callbackNumber_3, impl_.get(), std::placeholders::_1));

  // Create a connection so the OnUpdate function is called at every simulation
  // iteration. Remove this call, the connection and the callback if not needed.
  impl_->update_connection_ = gazebo::event::Events::ConnectWorldUpdateBegin(
    std::bind(&GazeboRosJointCommandPrivate::OnUpdate, impl_.get(), std::placeholders::_1));

  // The model pointer gives you direct access to the physics object,
  // for example:
  RCLCPP_INFO(impl_->ros_node_->get_logger(),"The robot %s has been started", model->GetName().c_str());
}

// Define Callbacks functions
void GazeboRosJointCommandPrivate::callbackNumber (const example_interfaces::msg::Float64::SharedPtr msg)
{
  vel_ = msg->data;

}

void GazeboRosJointCommandPrivate::callbackNumber_1 (const example_interfaces::msg::Float64::SharedPtr msg)
{
  vel_1 = msg->data;

}

void GazeboRosJointCommandPrivate::callbackNumber_2 (const example_interfaces::msg::Float64::SharedPtr msg)
{
  vel_2 = msg->data;

}

void GazeboRosJointCommandPrivate::callbackNumber_3 (const example_interfaces::msg::Float64::SharedPtr msg)
{
 vel_3 = msg->data;

}

void GazeboRosJointCommandPrivate::OnUpdate(const gazebo::common::UpdateInfo & info)
{
  gazebo::common::Time current_time = info.simTime;

  // If the world is reset, for example
  if (current_time < last_update_time_) {
    RCLCPP_INFO(ros_node_->get_logger(), "Negative sim time difference detected.");
    last_update_time_ = current_time;
  }

  // Check period
  double seconds_since_last_update = (current_time - last_update_time_).Double();

  if (seconds_since_last_update < update_period_) {
    return;
  }

  // Populate message
  auto msg = example_interfaces::msg::Float64();
  msg.data = joints_[0]->Position(0);
  auto msg_1 = example_interfaces::msg::Float64();
  msg_1.data = joints_[1]->Position(0);
  auto msg_2 = example_interfaces::msg::Float64();
  msg_2.data = joints_[2]->Position(0);
  auto msg_3 = example_interfaces::msg::Float64();
  msg_3.data = joints_[3]->Position(0);

  auto msg_vel = example_interfaces::msg::Float64();
  msg_vel.data = joints_[0]->GetVelocity(0);
  auto msg_vel_1 = example_interfaces::msg::Float64();
  msg_vel_1.data = joints_[1]->GetVelocity(0);
  auto msg_vel_2 = example_interfaces::msg::Float64();
  msg_vel_2.data = joints_[2]->GetForce(0);
  auto msg_vel_3 = example_interfaces::msg::Float64();
  msg_vel_3.data = joints_[3]->GetForce(0);


  // Publish
  joint_state_pub_->publish(msg);
  joint_state_pub_1->publish(msg_1);
  joint_state_pub_2->publish(msg_2);
  joint_state_pub_3->publish(msg_3);

 

  joint_inst_vel_->publish(msg_vel);
  joint_inst_vel_1->publish(msg_vel_1);
  joint_inst_vel_2->publish(msg_vel_2);
  joint_inst_vel_3->publish(msg_vel_3);

  joints_[0]->SetVelocity(0,vel_);
  joints_[1]->SetVelocity(0,vel_1);
  joints_[2]->SetVelocity(0,vel_2);
  joints_[3]->SetVelocity(0,vel_3);


  //joints_[0]->SetForce(0,0.0);



  // Update time
  last_update_time_ = current_time;
}

// Register this plumgin with the simulator
GZ_REGISTER_MODEL_PLUGIN(GazeboRosJointCommand)
}  // namespace gazebo_plugins