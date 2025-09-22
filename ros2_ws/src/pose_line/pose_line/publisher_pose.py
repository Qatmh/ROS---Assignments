import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import math

class PosePublisher(Node):
    def __init__(self):
        super().__init__('pose_publisher')
        self.publisher_ = self.create_publisher(PoseStamped, 'robot_pose', 10)
        timer_period = 0.5  # 2 Hz
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.x = 0.0
        self.y = 0.0
        self.step = 0.1  # move 0.1 m per step in x

    def timer_callback(self):
        msg = PoseStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "map"
        msg.pose.position.x = self.x
        msg.pose.position.y = self.y
        msg.pose.position.z = 0.0
        msg.pose.orientation.w = 1.0  # neutral orientation

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: x={self.x:.2f}, y={self.y:.2f}')

        self.x += self.step  # move in +x direction


def main(args=None):
    rclpy.init(args=args)
    node = PosePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
