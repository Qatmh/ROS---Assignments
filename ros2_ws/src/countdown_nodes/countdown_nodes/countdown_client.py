import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from countdown_interfaces.action import Countdown

class CountdownClient(Node):
    def __init__(self):
        super().__init__('countdown_client')
        self.declare_parameter('start_from', 10)
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
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'Received feedback: {feedback_msg.feedback.current}')

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Result: {result.result_text}')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = CountdownClient()
    node.send_goal()
    rclpy.spin(node)
