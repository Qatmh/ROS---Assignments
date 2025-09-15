// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_interface:srv/Distance.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__TRAITS_HPP_
#define CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "custom_interface/srv/detail/distance__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'a'
// Member 'b'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace custom_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const Distance_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: a
  {
    out << "a: ";
    to_flow_style_yaml(msg.a, out);
    out << ", ";
  }

  // member: b
  {
    out << "b: ";
    to_flow_style_yaml(msg.b, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Distance_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: a
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "a:\n";
    to_block_style_yaml(msg.a, out, indentation + 2);
  }

  // member: b
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "b:\n";
    to_block_style_yaml(msg.b, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Distance_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace custom_interface

namespace rosidl_generator_traits
{

[[deprecated("use custom_interface::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const custom_interface::srv::Distance_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  custom_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use custom_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const custom_interface::srv::Distance_Request & msg)
{
  return custom_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<custom_interface::srv::Distance_Request>()
{
  return "custom_interface::srv::Distance_Request";
}

template<>
inline const char * name<custom_interface::srv::Distance_Request>()
{
  return "custom_interface/srv/Distance_Request";
}

template<>
struct has_fixed_size<custom_interface::srv::Distance_Request>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Point>::value> {};

template<>
struct has_bounded_size<custom_interface::srv::Distance_Request>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Point>::value> {};

template<>
struct is_message<custom_interface::srv::Distance_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace custom_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const Distance_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: distance
  {
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
    out << ", ";
  }

  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Distance_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: distance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
    out << "\n";
  }

  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Distance_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace custom_interface

namespace rosidl_generator_traits
{

[[deprecated("use custom_interface::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const custom_interface::srv::Distance_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  custom_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use custom_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const custom_interface::srv::Distance_Response & msg)
{
  return custom_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<custom_interface::srv::Distance_Response>()
{
  return "custom_interface::srv::Distance_Response";
}

template<>
inline const char * name<custom_interface::srv::Distance_Response>()
{
  return "custom_interface/srv/Distance_Response";
}

template<>
struct has_fixed_size<custom_interface::srv::Distance_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<custom_interface::srv::Distance_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<custom_interface::srv::Distance_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<custom_interface::srv::Distance>()
{
  return "custom_interface::srv::Distance";
}

template<>
inline const char * name<custom_interface::srv::Distance>()
{
  return "custom_interface/srv/Distance";
}

template<>
struct has_fixed_size<custom_interface::srv::Distance>
  : std::integral_constant<
    bool,
    has_fixed_size<custom_interface::srv::Distance_Request>::value &&
    has_fixed_size<custom_interface::srv::Distance_Response>::value
  >
{
};

template<>
struct has_bounded_size<custom_interface::srv::Distance>
  : std::integral_constant<
    bool,
    has_bounded_size<custom_interface::srv::Distance_Request>::value &&
    has_bounded_size<custom_interface::srv::Distance_Response>::value
  >
{
};

template<>
struct is_service<custom_interface::srv::Distance>
  : std::true_type
{
};

template<>
struct is_service_request<custom_interface::srv::Distance_Request>
  : std::true_type
{
};

template<>
struct is_service_response<custom_interface::srv::Distance_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__TRAITS_HPP_
