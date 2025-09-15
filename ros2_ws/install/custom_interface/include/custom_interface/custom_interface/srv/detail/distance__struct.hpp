// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from custom_interface:srv/Distance.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__STRUCT_HPP_
#define CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'a'
// Member 'b'
#include "geometry_msgs/msg/detail/point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__custom_interface__srv__Distance_Request __attribute__((deprecated))
#else
# define DEPRECATED__custom_interface__srv__Distance_Request __declspec(deprecated)
#endif

namespace custom_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Distance_Request_
{
  using Type = Distance_Request_<ContainerAllocator>;

  explicit Distance_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : a(_init),
    b(_init)
  {
    (void)_init;
  }

  explicit Distance_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : a(_alloc, _init),
    b(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _a_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _a_type a;
  using _b_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _b_type b;

  // setters for named parameter idiom
  Type & set__a(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->a = _arg;
    return *this;
  }
  Type & set__b(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->b = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_interface::srv::Distance_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_interface::srv::Distance_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_interface::srv::Distance_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_interface::srv::Distance_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_interface::srv::Distance_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_interface::srv::Distance_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_interface::srv::Distance_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_interface::srv::Distance_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_interface::srv::Distance_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_interface::srv::Distance_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_interface__srv__Distance_Request
    std::shared_ptr<custom_interface::srv::Distance_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_interface__srv__Distance_Request
    std::shared_ptr<custom_interface::srv::Distance_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Distance_Request_ & other) const
  {
    if (this->a != other.a) {
      return false;
    }
    if (this->b != other.b) {
      return false;
    }
    return true;
  }
  bool operator!=(const Distance_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Distance_Request_

// alias to use template instance with default allocator
using Distance_Request =
  custom_interface::srv::Distance_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace custom_interface


#ifndef _WIN32
# define DEPRECATED__custom_interface__srv__Distance_Response __attribute__((deprecated))
#else
# define DEPRECATED__custom_interface__srv__Distance_Response __declspec(deprecated)
#endif

namespace custom_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Distance_Response_
{
  using Type = Distance_Response_<ContainerAllocator>;

  explicit Distance_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->distance = 0.0;
      this->success = false;
      this->message = "";
    }
  }

  explicit Distance_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->distance = 0.0;
      this->success = false;
      this->message = "";
    }
  }

  // field types and members
  using _distance_type =
    double;
  _distance_type distance;
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;

  // setters for named parameter idiom
  Type & set__distance(
    const double & _arg)
  {
    this->distance = _arg;
    return *this;
  }
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_interface::srv::Distance_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_interface::srv::Distance_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_interface::srv::Distance_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_interface::srv::Distance_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_interface::srv::Distance_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_interface::srv::Distance_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_interface::srv::Distance_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_interface::srv::Distance_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_interface::srv::Distance_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_interface::srv::Distance_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_interface__srv__Distance_Response
    std::shared_ptr<custom_interface::srv::Distance_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_interface__srv__Distance_Response
    std::shared_ptr<custom_interface::srv::Distance_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Distance_Response_ & other) const
  {
    if (this->distance != other.distance) {
      return false;
    }
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const Distance_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Distance_Response_

// alias to use template instance with default allocator
using Distance_Response =
  custom_interface::srv::Distance_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace custom_interface

namespace custom_interface
{

namespace srv
{

struct Distance
{
  using Request = custom_interface::srv::Distance_Request;
  using Response = custom_interface::srv::Distance_Response;
};

}  // namespace srv

}  // namespace custom_interface

#endif  // CUSTOM_INTERFACE__SRV__DETAIL__DISTANCE__STRUCT_HPP_
