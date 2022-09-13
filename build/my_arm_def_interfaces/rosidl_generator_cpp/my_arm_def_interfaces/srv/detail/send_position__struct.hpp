// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_arm_def_interfaces:srv/SendPosition.idl
// generated code does not contain a copyright notice

#ifndef MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__STRUCT_HPP_
#define MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__my_arm_def_interfaces__srv__SendPosition_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_arm_def_interfaces__srv__SendPosition_Request __declspec(deprecated)
#endif

namespace my_arm_def_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SendPosition_Request_
{
  using Type = SendPosition_Request_<ContainerAllocator>;

  explicit SendPosition_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->position = 0.0;
    }
  }

  explicit SendPosition_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->position = 0.0;
    }
  }

  // field types and members
  using _position_type =
    double;
  _position_type position;

  // setters for named parameter idiom
  Type & set__position(
    const double & _arg)
  {
    this->position = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_arm_def_interfaces__srv__SendPosition_Request
    std::shared_ptr<my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_arm_def_interfaces__srv__SendPosition_Request
    std::shared_ptr<my_arm_def_interfaces::srv::SendPosition_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SendPosition_Request_ & other) const
  {
    if (this->position != other.position) {
      return false;
    }
    return true;
  }
  bool operator!=(const SendPosition_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SendPosition_Request_

// alias to use template instance with default allocator
using SendPosition_Request =
  my_arm_def_interfaces::srv::SendPosition_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_arm_def_interfaces


#ifndef _WIN32
# define DEPRECATED__my_arm_def_interfaces__srv__SendPosition_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_arm_def_interfaces__srv__SendPosition_Response __declspec(deprecated)
#endif

namespace my_arm_def_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SendPosition_Response_
{
  using Type = SendPosition_Response_<ContainerAllocator>;

  explicit SendPosition_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->msg = "";
    }
  }

  explicit SendPosition_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : msg(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->msg = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _msg_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _msg_type msg;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__msg(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->msg = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_arm_def_interfaces__srv__SendPosition_Response
    std::shared_ptr<my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_arm_def_interfaces__srv__SendPosition_Response
    std::shared_ptr<my_arm_def_interfaces::srv::SendPosition_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SendPosition_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->msg != other.msg) {
      return false;
    }
    return true;
  }
  bool operator!=(const SendPosition_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SendPosition_Response_

// alias to use template instance with default allocator
using SendPosition_Response =
  my_arm_def_interfaces::srv::SendPosition_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_arm_def_interfaces

namespace my_arm_def_interfaces
{

namespace srv
{

struct SendPosition
{
  using Request = my_arm_def_interfaces::srv::SendPosition_Request;
  using Response = my_arm_def_interfaces::srv::SendPosition_Response;
};

}  // namespace srv

}  // namespace my_arm_def_interfaces

#endif  // MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__STRUCT_HPP_
