// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from my_arm_def_interfaces:srv/SendPosition.idl
// generated code does not contain a copyright notice

#ifndef MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__FUNCTIONS_H_
#define MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "my_arm_def_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "my_arm_def_interfaces/srv/detail/send_position__struct.h"

/// Initialize srv/SendPosition message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * my_arm_def_interfaces__srv__SendPosition_Request
 * )) before or use
 * my_arm_def_interfaces__srv__SendPosition_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
bool
my_arm_def_interfaces__srv__SendPosition_Request__init(my_arm_def_interfaces__srv__SendPosition_Request * msg);

/// Finalize srv/SendPosition message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
void
my_arm_def_interfaces__srv__SendPosition_Request__fini(my_arm_def_interfaces__srv__SendPosition_Request * msg);

/// Create srv/SendPosition message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * my_arm_def_interfaces__srv__SendPosition_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
my_arm_def_interfaces__srv__SendPosition_Request *
my_arm_def_interfaces__srv__SendPosition_Request__create();

/// Destroy srv/SendPosition message.
/**
 * It calls
 * my_arm_def_interfaces__srv__SendPosition_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
void
my_arm_def_interfaces__srv__SendPosition_Request__destroy(my_arm_def_interfaces__srv__SendPosition_Request * msg);


/// Initialize array of srv/SendPosition messages.
/**
 * It allocates the memory for the number of elements and calls
 * my_arm_def_interfaces__srv__SendPosition_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
bool
my_arm_def_interfaces__srv__SendPosition_Request__Sequence__init(my_arm_def_interfaces__srv__SendPosition_Request__Sequence * array, size_t size);

/// Finalize array of srv/SendPosition messages.
/**
 * It calls
 * my_arm_def_interfaces__srv__SendPosition_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
void
my_arm_def_interfaces__srv__SendPosition_Request__Sequence__fini(my_arm_def_interfaces__srv__SendPosition_Request__Sequence * array);

/// Create array of srv/SendPosition messages.
/**
 * It allocates the memory for the array and calls
 * my_arm_def_interfaces__srv__SendPosition_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
my_arm_def_interfaces__srv__SendPosition_Request__Sequence *
my_arm_def_interfaces__srv__SendPosition_Request__Sequence__create(size_t size);

/// Destroy array of srv/SendPosition messages.
/**
 * It calls
 * my_arm_def_interfaces__srv__SendPosition_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
void
my_arm_def_interfaces__srv__SendPosition_Request__Sequence__destroy(my_arm_def_interfaces__srv__SendPosition_Request__Sequence * array);

/// Initialize srv/SendPosition message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * my_arm_def_interfaces__srv__SendPosition_Response
 * )) before or use
 * my_arm_def_interfaces__srv__SendPosition_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
bool
my_arm_def_interfaces__srv__SendPosition_Response__init(my_arm_def_interfaces__srv__SendPosition_Response * msg);

/// Finalize srv/SendPosition message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
void
my_arm_def_interfaces__srv__SendPosition_Response__fini(my_arm_def_interfaces__srv__SendPosition_Response * msg);

/// Create srv/SendPosition message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * my_arm_def_interfaces__srv__SendPosition_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
my_arm_def_interfaces__srv__SendPosition_Response *
my_arm_def_interfaces__srv__SendPosition_Response__create();

/// Destroy srv/SendPosition message.
/**
 * It calls
 * my_arm_def_interfaces__srv__SendPosition_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
void
my_arm_def_interfaces__srv__SendPosition_Response__destroy(my_arm_def_interfaces__srv__SendPosition_Response * msg);


/// Initialize array of srv/SendPosition messages.
/**
 * It allocates the memory for the number of elements and calls
 * my_arm_def_interfaces__srv__SendPosition_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
bool
my_arm_def_interfaces__srv__SendPosition_Response__Sequence__init(my_arm_def_interfaces__srv__SendPosition_Response__Sequence * array, size_t size);

/// Finalize array of srv/SendPosition messages.
/**
 * It calls
 * my_arm_def_interfaces__srv__SendPosition_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
void
my_arm_def_interfaces__srv__SendPosition_Response__Sequence__fini(my_arm_def_interfaces__srv__SendPosition_Response__Sequence * array);

/// Create array of srv/SendPosition messages.
/**
 * It allocates the memory for the array and calls
 * my_arm_def_interfaces__srv__SendPosition_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
my_arm_def_interfaces__srv__SendPosition_Response__Sequence *
my_arm_def_interfaces__srv__SendPosition_Response__Sequence__create(size_t size);

/// Destroy array of srv/SendPosition messages.
/**
 * It calls
 * my_arm_def_interfaces__srv__SendPosition_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_arm_def_interfaces
void
my_arm_def_interfaces__srv__SendPosition_Response__Sequence__destroy(my_arm_def_interfaces__srv__SendPosition_Response__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // MY_ARM_DEF_INTERFACES__SRV__DETAIL__SEND_POSITION__FUNCTIONS_H_
