import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from countdown_interfaces.action import Countdown
import time

class CountdownCancelClient(Node):
    def __init__(self):
        super().__init__('countdown_cancel_client')
        self.declare_parameter('start_from', 10)
        self.declare_parameter('cancel_after', 3.0)  # seconds before cancel
        self._action_client = ActionClient(self, Countdown, 'countdown')

    def send_goal(self):
        goal_msg = Countdown.Goal()
        goal_msg.start_from = self.get_parameter('start_from').value

        self._action_client.wait_for_server()
        self.get_logger().info(f'Sending goal: start_from={goal_msg.start_from}')
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        self.goal_handle = future.result()
        if not self.goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')
        cancel_after = self.get_parameter('cancel_after').value
        self.get_logger().info(f'Will cancel after {cancel_after} seconds...')
        time.sleep(cancel_after)
        self.cancel_goal()

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'Received feedback: {feedback_msg.feedback.current}')

    def cancel_goal(self):
        cancel_future = self.goal_handle.cancel_goal_async()
        cancel_future.add_done_callback(self.cancel_done)

    def cancel_done(self, future):
        self.get_logger().info('Cancel request sent')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=None)
    node = CountdownCancelClient()
    node.send_goal()
    rclpy.spin(node)
