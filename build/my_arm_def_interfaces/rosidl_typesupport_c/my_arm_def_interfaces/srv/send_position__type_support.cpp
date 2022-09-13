// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from my_arm_def_interfaces:srv/SendPosition.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "my_arm_def_interfaces/msg/rosidl_typesupport_c__visibility_control.h"
#include "my_arm_def_interfaces/srv/detail/send_position__struct.h"
#include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/message_type_support_dispatch.h"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_c/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace my_arm_def_interfaces
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _SendPosition_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _SendPosition_Request_type_support_ids_t;

static const _SendPosition_Request_type_support_ids_t _SendPosition_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _SendPosition_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _SendPosition_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _SendPosition_Request_type_support_symbol_names_t _SendPosition_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, my_arm_def_interfaces, srv, SendPosition_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, my_arm_def_interfaces, srv, SendPosition_Request)),
  }
};

typedef struct _SendPosition_Request_type_support_data_t
{
  void * data[2];
} _SendPosition_Request_type_support_data_t;

static _SendPosition_Request_type_support_data_t _SendPosition_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _SendPosition_Request_message_typesupport_map = {
  2,
  "my_arm_def_interfaces",
  &_SendPosition_Request_message_typesupport_ids.typesupport_identifier[0],
  &_SendPosition_Request_message_typesupport_symbol_names.symbol_name[0],
  &_SendPosition_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t SendPosition_Request_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_SendPosition_Request_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace my_arm_def_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_my_arm_def_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, my_arm_def_interfaces, srv, SendPosition_Request)() {
  return &::my_arm_def_interfaces::srv::rosidl_typesupport_c::SendPosition_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "my_arm_def_interfaces/msg/rosidl_typesupport_c__visibility_control.h"
// already included above
// #include "my_arm_def_interfaces/srv/detail/send_position__struct.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace my_arm_def_interfaces
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _SendPosition_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _SendPosition_Response_type_support_ids_t;

static const _SendPosition_Response_type_support_ids_t _SendPosition_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _SendPosition_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _SendPosition_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _SendPosition_Response_type_support_symbol_names_t _SendPosition_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, my_arm_def_interfaces, srv, SendPosition_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, my_arm_def_interfaces, srv, SendPosition_Response)),
  }
};

typedef struct _SendPosition_Response_type_support_data_t
{
  void * data[2];
} _SendPosition_Response_type_support_data_t;

static _SendPosition_Response_type_support_data_t _SendPosition_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _SendPosition_Response_message_typesupport_map = {
  2,
  "my_arm_def_interfaces",
  &_SendPosition_Response_message_typesupport_ids.typesupport_identifier[0],
  &_SendPosition_Response_message_typesupport_symbol_names.symbol_name[0],
  &_SendPosition_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t SendPosition_Response_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_SendPosition_Response_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace my_arm_def_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_my_arm_def_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, my_arm_def_interfaces, srv, SendPosition_Response)() {
  return &::my_arm_def_interfaces::srv::rosidl_typesupport_c::SendPosition_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "my_arm_def_interfaces/msg/rosidl_typesupport_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/service_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace my_arm_def_interfaces
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _SendPosition_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _SendPosition_type_support_ids_t;

static const _SendPosition_type_support_ids_t _SendPosition_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _SendPosition_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _SendPosition_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _SendPosition_type_support_symbol_names_t _SendPosition_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, my_arm_def_interfaces, srv, SendPosition)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, my_arm_def_interfaces, srv, SendPosition)),
  }
};

typedef struct _SendPosition_type_support_data_t
{
  void * data[2];
} _SendPosition_type_support_data_t;

static _SendPosition_type_support_data_t _SendPosition_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _SendPosition_service_typesupport_map = {
  2,
  "my_arm_def_interfaces",
  &_SendPosition_service_typesupport_ids.typesupport_identifier[0],
  &_SendPosition_service_typesupport_symbol_names.symbol_name[0],
  &_SendPosition_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t SendPosition_service_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_SendPosition_service_typesupport_map),
  rosidl_typesupport_c__get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace my_arm_def_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_my_arm_def_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_c, my_arm_def_interfaces, srv, SendPosition)() {
  return &::my_arm_def_interfaces::srv::rosidl_typesupport_c::SendPosition_service_type_support_handle;
}

#ifdef __cplusplus
}
#endif
