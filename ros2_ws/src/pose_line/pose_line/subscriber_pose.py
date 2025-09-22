import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class PoseSubscriber(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        self.subscription = self.create_subscription(
            PoseStamped,
            'robot_pose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused warning

    def listener_callback(self, msg):
        x = msg.pose.position.x
        y = msg.pose.position.y
        self.get_logger().info(f'Received pose: x={x:.2f}, y={y:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
