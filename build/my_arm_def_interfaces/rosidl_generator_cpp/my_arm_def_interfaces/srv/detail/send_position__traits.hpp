// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_arm_def_interfaces:srv/SendPosition.idl
// generated code does not contain a copyright notice

#ifndef MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__TRAITS_HPP_
#define MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__TRAITS_HPP_

#include "my_arm_def_interfaces/srv/detail/send_position__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_arm_def_interfaces::srv::SendPosition_Request>()
{
  return "my_arm_def_interfaces::srv::SendPosition_Request";
}

template<>
inline const char * name<my_arm_def_interfaces::srv::SendPosition_Request>()
{
  return "my_arm_def_interfaces/srv/SendPosition_Request";
}

template<>
struct has_fixed_size<my_arm_def_interfaces::srv::SendPosition_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_arm_def_interfaces::srv::SendPosition_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_arm_def_interfaces::srv::SendPosition_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_arm_def_interfaces::srv::SendPosition_Response>()
{
  return "my_arm_def_interfaces::srv::SendPosition_Response";
}

template<>
inline const char * name<my_arm_def_interfaces::srv::SendPosition_Response>()
{
  return "my_arm_def_interfaces/srv/SendPosition_Response";
}

template<>
struct has_fixed_size<my_arm_def_interfaces::srv::SendPosition_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<my_arm_def_interfaces::srv::SendPosition_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<my_arm_def_interfaces::srv::SendPosition_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_arm_def_interfaces::srv::SendPosition>()
{
  return "my_arm_def_interfaces::srv::SendPosition";
}

template<>
inline const char * name<my_arm_def_interfaces::srv::SendPosition>()
{
  return "my_arm_def_interfaces/srv/SendPosition";
}

template<>
struct has_fixed_size<my_arm_def_interfaces::srv::SendPosition>
  : std::integral_constant<
    bool,
    has_fixed_size<my_arm_def_interfaces::srv::SendPosition_Request>::value &&
    has_fixed_size<my_arm_def_interfaces::srv::SendPosition_Response>::value
  >
{
};

template<>
struct has_bounded_size<my_arm_def_interfaces::srv::SendPosition>
  : std::integral_constant<
    bool,
    has_bounded_size<my_arm_def_interfaces::srv::SendPosition_Request>::value &&
    has_bounded_size<my_arm_def_interfaces::srv::SendPosition_Response>::value
  >
{
};

template<>
struct is_service<my_arm_def_interfaces::srv::SendPosition>
  : std::true_type
{
};

template<>
struct is_service_request<my_arm_def_interfaces::srv::SendPosition_Request>
  : std::true_type
{
};

template<>
struct is_service_response<my_arm_def_interfaces::srv::SendPosition_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__TRAITS_HPP_
