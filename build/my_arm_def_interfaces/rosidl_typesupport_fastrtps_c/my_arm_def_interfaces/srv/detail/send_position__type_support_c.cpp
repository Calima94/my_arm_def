// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from my_arm_def_interfaces:srv/SendPosition.idl
// generated code does not contain a copyright notice
#include "my_arm_def_interfaces/srv/detail/send_position__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "my_arm_def_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "my_arm_def_interfaces/srv/detail/send_position__struct.h"
#include "my_arm_def_interfaces/srv/detail/send_position__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _SendPosition_Request__ros_msg_type = my_arm_def_interfaces__srv__SendPosition_Request;

static bool _SendPosition_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _SendPosition_Request__ros_msg_type * ros_message = static_cast<const _SendPosition_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: position
  {
    cdr << ros_message->position;
  }

  return true;
}

static bool _SendPosition_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _SendPosition_Request__ros_msg_type * ros_message = static_cast<_SendPosition_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: position
  {
    cdr >> ros_message->position;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_arm_def_interfaces
size_t get_serialized_size_my_arm_def_interfaces__srv__SendPosition_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _SendPosition_Request__ros_msg_type * ros_message = static_cast<const _SendPosition_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name position
  {
    size_t item_size = sizeof(ros_message->position);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _SendPosition_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_my_arm_def_interfaces__srv__SendPosition_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_arm_def_interfaces
size_t max_serialized_size_my_arm_def_interfaces__srv__SendPosition_Request(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: position
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _SendPosition_Request__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_my_arm_def_interfaces__srv__SendPosition_Request(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_SendPosition_Request = {
  "my_arm_def_interfaces::srv",
  "SendPosition_Request",
  _SendPosition_Request__cdr_serialize,
  _SendPosition_Request__cdr_deserialize,
  _SendPosition_Request__get_serialized_size,
  _SendPosition_Request__max_serialized_size
};

static rosidl_message_type_support_t _SendPosition_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_SendPosition_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, my_arm_def_interfaces, srv, SendPosition_Request)() {
  return &_SendPosition_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "my_arm_def_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "my_arm_def_interfaces/srv/detail/send_position__struct.h"
// already included above
// #include "my_arm_def_interfaces/srv/detail/send_position__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // msg
#include "rosidl_runtime_c/string_functions.h"  // msg

// forward declare type support functions


using _SendPosition_Response__ros_msg_type = my_arm_def_interfaces__srv__SendPosition_Response;

static bool _SendPosition_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _SendPosition_Response__ros_msg_type * ros_message = static_cast<const _SendPosition_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    cdr << (ros_message->success ? true : false);
  }

  // Field name: msg
  {
    const rosidl_runtime_c__String * str = &ros_message->msg;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _SendPosition_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _SendPosition_Response__ros_msg_type * ros_message = static_cast<_SendPosition_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->success = tmp ? true : false;
  }

  // Field name: msg
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->msg.data) {
      rosidl_runtime_c__String__init(&ros_message->msg);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->msg,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'msg'\n");
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_arm_def_interfaces
size_t get_serialized_size_my_arm_def_interfaces__srv__SendPosition_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _SendPosition_Response__ros_msg_type * ros_message = static_cast<const _SendPosition_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name success
  {
    size_t item_size = sizeof(ros_message->success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name msg
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->msg.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _SendPosition_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_my_arm_def_interfaces__srv__SendPosition_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_arm_def_interfaces
size_t max_serialized_size_my_arm_def_interfaces__srv__SendPosition_Response(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: success
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: msg
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _SendPosition_Response__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_my_arm_def_interfaces__srv__SendPosition_Response(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_SendPosition_Response = {
  "my_arm_def_interfaces::srv",
  "SendPosition_Response",
  _SendPosition_Response__cdr_serialize,
  _SendPosition_Response__cdr_deserialize,
  _SendPosition_Response__get_serialized_size,
  _SendPosition_Response__max_serialized_size
};

static rosidl_message_type_support_t _SendPosition_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_SendPosition_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, my_arm_def_interfaces, srv, SendPosition_Response)() {
  return &_SendPosition_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "my_arm_def_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "my_arm_def_interfaces/srv/send_position.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t SendPosition__callbacks = {
  "my_arm_def_interfaces::srv",
  "SendPosition",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, my_arm_def_interfaces, srv, SendPosition_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, my_arm_def_interfaces, srv, SendPosition_Response)(),
};

static rosidl_service_type_support_t SendPosition__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &SendPosition__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, my_arm_def_interfaces, srv, SendPosition)() {
  return &SendPosition__handle;
}

#if defined(__cplusplus)
}
#endif
