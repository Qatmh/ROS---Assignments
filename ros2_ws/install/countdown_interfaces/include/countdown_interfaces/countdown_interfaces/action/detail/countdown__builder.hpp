// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from countdown_interfaces:action/Countdown.idl
// generated code does not contain a copyright notice

#ifndef COUNTDOWN_INTERFACES__ACTION__DETAIL__COUNTDOWN__BUILDER_HPP_
#define COUNTDOWN_INTERFACES__ACTION__DETAIL__COUNTDOWN__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "countdown_interfaces/action/detail/countdown__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace countdown_interfaces
{

namespace action
{

namespace builder
{

class Init_Countdown_Goal_start_from
{
public:
  Init_Countdown_Goal_start_from()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::countdown_interfaces::action::Countdown_Goal start_from(::countdown_interfaces::action::Countdown_Goal::_start_from_type arg)
  {
    msg_.start_from = std::move(arg);
    return std::move(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::countdown_interfaces::action::Countdown_Goal>()
{
  return countdown_interfaces::action::builder::Init_Countdown_Goal_start_from();
}

}  // namespace countdown_interfaces


namespace countdown_interfaces
{

namespace action
{

namespace builder
{

class Init_Countdown_Result_result_text
{
public:
  Init_Countdown_Result_result_text()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::countdown_interfaces::action::Countdown_Result result_text(::countdown_interfaces::action::Countdown_Result::_result_text_type arg)
  {
    msg_.result_text = std::move(arg);
    return std::move(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::countdown_interfaces::action::Countdown_Result>()
{
  return countdown_interfaces::action::builder::Init_Countdown_Result_result_text();
}

}  // namespace countdown_interfaces


namespace countdown_interfaces
{

namespace action
{

namespace builder
{

class Init_Countdown_Feedback_current
{
public:
  Init_Countdown_Feedback_current()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::countdown_interfaces::action::Countdown_Feedback current(::countdown_interfaces::action::Countdown_Feedback::_current_type arg)
  {
    msg_.current = std::move(arg);
    return std::move(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::countdown_interfaces::action::Countdown_Feedback>()
{
  return countdown_interfaces::action::builder::Init_Countdown_Feedback_current();
}

}  // namespace countdown_interfaces


namespace countdown_interfaces
{

namespace action
{

namespace builder
{

class Init_Countdown_SendGoal_Request_goal
{
public:
  explicit Init_Countdown_SendGoal_Request_goal(::countdown_interfaces::action::Countdown_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::countdown_interfaces::action::Countdown_SendGoal_Request goal(::countdown_interfaces::action::Countdown_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_SendGoal_Request msg_;
};

class Init_Countdown_SendGoal_Request_goal_id
{
public:
  Init_Countdown_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Countdown_SendGoal_Request_goal goal_id(::countdown_interfaces::action::Countdown_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Countdown_SendGoal_Request_goal(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::countdown_interfaces::action::Countdown_SendGoal_Request>()
{
  return countdown_interfaces::action::builder::Init_Countdown_SendGoal_Request_goal_id();
}

}  // namespace countdown_interfaces


namespace countdown_interfaces
{

namespace action
{

namespace builder
{

class Init_Countdown_SendGoal_Response_stamp
{
public:
  explicit Init_Countdown_SendGoal_Response_stamp(::countdown_interfaces::action::Countdown_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::countdown_interfaces::action::Countdown_SendGoal_Response stamp(::countdown_interfaces::action::Countdown_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_SendGoal_Response msg_;
};

class Init_Countdown_SendGoal_Response_accepted
{
public:
  Init_Countdown_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Countdown_SendGoal_Response_stamp accepted(::countdown_interfaces::action::Countdown_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_Countdown_SendGoal_Response_stamp(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::countdown_interfaces::action::Countdown_SendGoal_Response>()
{
  return countdown_interfaces::action::builder::Init_Countdown_SendGoal_Response_accepted();
}

}  // namespace countdown_interfaces


namespace countdown_interfaces
{

namespace action
{

namespace builder
{

class Init_Countdown_GetResult_Request_goal_id
{
public:
  Init_Countdown_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::countdown_interfaces::action::Countdown_GetResult_Request goal_id(::countdown_interfaces::action::Countdown_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::countdown_interfaces::action::Countdown_GetResult_Request>()
{
  return countdown_interfaces::action::builder::Init_Countdown_GetResult_Request_goal_id();
}

}  // namespace countdown_interfaces


namespace countdown_interfaces
{

namespace action
{

namespace builder
{

class Init_Countdown_GetResult_Response_result
{
public:
  explicit Init_Countdown_GetResult_Response_result(::countdown_interfaces::action::Countdown_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::countdown_interfaces::action::Countdown_GetResult_Response result(::countdown_interfaces::action::Countdown_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_GetResult_Response msg_;
};

class Init_Countdown_GetResult_Response_status
{
public:
  Init_Countdown_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Countdown_GetResult_Response_result status(::countdown_interfaces::action::Countdown_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Countdown_GetResult_Response_result(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::countdown_interfaces::action::Countdown_GetResult_Response>()
{
  return countdown_interfaces::action::builder::Init_Countdown_GetResult_Response_status();
}

}  // namespace countdown_interfaces


namespace countdown_interfaces
{

namespace action
{

namespace builder
{

class Init_Countdown_FeedbackMessage_feedback
{
public:
  explicit Init_Countdown_FeedbackMessage_feedback(::countdown_interfaces::action::Countdown_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::countdown_interfaces::action::Countdown_FeedbackMessage feedback(::countdown_interfaces::action::Countdown_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_FeedbackMessage msg_;
};

class Init_Countdown_FeedbackMessage_goal_id
{
public:
  Init_Countdown_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Countdown_FeedbackMessage_feedback goal_id(::countdown_interfaces::action::Countdown_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Countdown_FeedbackMessage_feedback(msg_);
  }

private:
  ::countdown_interfaces::action::Countdown_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::countdown_interfaces::action::Countdown_FeedbackMessage>()
{
  return countdown_interfaces::action::builder::Init_Countdown_FeedbackMessage_goal_id();
}

}  // namespace countdown_interfaces

#endif  // COUNTDOWN_INTERFACES__ACTION__DETAIL__COUNTDOWN__BUILDER_HPP_
