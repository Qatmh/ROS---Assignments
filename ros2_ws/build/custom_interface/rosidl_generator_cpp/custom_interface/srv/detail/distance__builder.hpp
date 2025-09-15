// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interface:srv/Distance.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__BUILDER_HPP_
#define CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interface/srv/detail/distance__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interface
{

namespace srv
{

namespace builder
{

class Init_Distance_Request_b
{
public:
  explicit Init_Distance_Request_b(::custom_interface::srv::Distance_Request & msg)
  : msg_(msg)
  {}
  ::custom_interface::srv::Distance_Request b(::custom_interface::srv::Distance_Request::_b_type arg)
  {
    msg_.b = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interface::srv::Distance_Request msg_;
};

class Init_Distance_Request_a
{
public:
  Init_Distance_Request_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Distance_Request_b a(::custom_interface::srv::Distance_Request::_a_type arg)
  {
    msg_.a = std::move(arg);
    return Init_Distance_Request_b(msg_);
  }

private:
  ::custom_interface::srv::Distance_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interface::srv::Distance_Request>()
{
  return custom_interface::srv::builder::Init_Distance_Request_a();
}

}  // namespace custom_interface


namespace custom_interface
{

namespace srv
{

namespace builder
{

class Init_Distance_Response_message
{
public:
  explicit Init_Distance_Response_message(::custom_interface::srv::Distance_Response & msg)
  : msg_(msg)
  {}
  ::custom_interface::srv::Distance_Response message(::custom_interface::srv::Distance_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interface::srv::Distance_Response msg_;
};

class Init_Distance_Response_success
{
public:
  explicit Init_Distance_Response_success(::custom_interface::srv::Distance_Response & msg)
  : msg_(msg)
  {}
  Init_Distance_Response_message success(::custom_interface::srv::Distance_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_Distance_Response_message(msg_);
  }

private:
  ::custom_interface::srv::Distance_Response msg_;
};

class Init_Distance_Response_distance
{
public:
  Init_Distance_Response_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Distance_Response_success distance(::custom_interface::srv::Distance_Response::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_Distance_Response_success(msg_);
  }

private:
  ::custom_interface::srv::Distance_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interface::srv::Distance_Response>()
{
  return custom_interface::srv::builder::Init_Distance_Response_distance();
}

}  // namespace custom_interface

#endif  // CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__BUILDER_HPP_
