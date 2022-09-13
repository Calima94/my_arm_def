// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_arm_def_interfaces:srv/SendPosition.idl
// generated code does not contain a copyright notice

#ifndef MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__BUILDER_HPP_
#define MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__BUILDER_HPP_

#include "my_arm_def_interfaces/srv/detail/send_position__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace my_arm_def_interfaces
{

namespace srv
{

namespace builder
{

class Init_SendPosition_Request_position
{
public:
  Init_SendPosition_Request_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_arm_def_interfaces::srv::SendPosition_Request position(::my_arm_def_interfaces::srv::SendPosition_Request::_position_type arg)
  {
    msg_.position = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_arm_def_interfaces::srv::SendPosition_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_arm_def_interfaces::srv::SendPosition_Request>()
{
  return my_arm_def_interfaces::srv::builder::Init_SendPosition_Request_position();
}

}  // namespace my_arm_def_interfaces


namespace my_arm_def_interfaces
{

namespace srv
{

namespace builder
{

class Init_SendPosition_Response_msg
{
public:
  explicit Init_SendPosition_Response_msg(::my_arm_def_interfaces::srv::SendPosition_Response & msg)
  : msg_(msg)
  {}
  ::my_arm_def_interfaces::srv::SendPosition_Response msg(::my_arm_def_interfaces::srv::SendPosition_Response::_msg_type arg)
  {
    msg_.msg = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_arm_def_interfaces::srv::SendPosition_Response msg_;
};

class Init_SendPosition_Response_success
{
public:
  Init_SendPosition_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SendPosition_Response_msg success(::my_arm_def_interfaces::srv::SendPosition_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_SendPosition_Response_msg(msg_);
  }

private:
  ::my_arm_def_interfaces::srv::SendPosition_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_arm_def_interfaces::srv::SendPosition_Response>()
{
  return my_arm_def_interfaces::srv::builder::Init_SendPosition_Response_success();
}

}  // namespace my_arm_def_interfaces

#endif  // MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__BUILDER_HPP_
