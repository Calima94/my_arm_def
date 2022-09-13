// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_arm_def_interfaces:msg/HardwareStatus.idl
// generated code does not contain a copyright notice

#ifndef MY_ARM_DEF_INTERFACES__MSG__DETAIL__HARDWARE_STATUS__TRAITS_HPP_
#define MY_ARM_DEF_INTERFACES__MSG__DETAIL__HARDWARE_STATUS__TRAITS_HPP_

#include "my_arm_def_interfaces/msg/detail/hardware_status__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_arm_def_interfaces::msg::HardwareStatus>()
{
  return "my_arm_def_interfaces::msg::HardwareStatus";
}

template<>
inline const char * name<my_arm_def_interfaces::msg::HardwareStatus>()
{
  return "my_arm_def_interfaces/msg/HardwareStatus";
}

template<>
struct has_fixed_size<my_arm_def_interfaces::msg::HardwareStatus>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<my_arm_def_interfaces::msg::HardwareStatus>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<my_arm_def_interfaces::msg::HardwareStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MY_ARM_DEF_INTERFACES__MSG__DETAIL__HARDWARE_STATUS__TRAITS_HPP_
