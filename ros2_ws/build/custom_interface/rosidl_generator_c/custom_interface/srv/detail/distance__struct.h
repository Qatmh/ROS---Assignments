// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interface:srv/Distance.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__STRUCT_H_
#define CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'a'
// Member 'b'
#include "geometry_msgs/msg/detail/point__struct.h"

/// Struct defined in srv/Distance in the package custom_interface.
typedef struct custom_interface__srv__Distance_Request
{
  geometry_msgs__msg__Point a;
  geometry_msgs__msg__Point b;
} custom_interface__srv__Distance_Request;

// Struct for a sequence of custom_interface__srv__Distance_Request.
typedef struct custom_interface__srv__Distance_Request__Sequence
{
  custom_interface__srv__Distance_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interface__srv__Distance_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Distance in the package custom_interface.
typedef struct custom_interface__srv__Distance_Response
{
  double distance;
  bool success;
  rosidl_runtime_c__String message;
} custom_interface__srv__Distance_Response;

// Struct for a sequence of custom_interface__srv__Distance_Response.
typedef struct custom_interface__srv__Distance_Response__Sequence
{
  custom_interface__srv__Distance_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interface__srv__Distance_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__STRUCT_H_
