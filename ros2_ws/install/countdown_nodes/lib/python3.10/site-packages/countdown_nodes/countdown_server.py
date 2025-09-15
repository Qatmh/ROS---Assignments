import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from countdown_interfaces.action import Countdown
import time

class CountdownActionServer(Node):
    def __init__(self):
        super().__init__('countdown_server')
        self.declare_parameter('start_from', 5)
        self._action_server = ActionServer(
            self,
            Countdown,
            'countdown',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback)

    def goal_callback(self, goal_request):
        self.get_logger().info(f'Received goal: start_from={goal_request.start_from}')
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT

    async def execute_callback(self, goal_handle):
        feedback_msg = Countdown.Feedback()

        count = goal_handle.request.start_from
        self.get_logger().info(f'Starting countdown from {count}')

        while count >= 0:
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return Countdown.Result(result_text='Countdown canceled')
            
            feedback_msg.current = count
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f'Feedback: {count}')
            time.sleep(1)
            count -= 1

        goal_handle.succeed()
        result = Countdown.Result()
        result.result_text = 'Countdown finished successfully!'
        return result

def main(args=None):
    rclpy.init(args=args)
    node = CountdownActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
