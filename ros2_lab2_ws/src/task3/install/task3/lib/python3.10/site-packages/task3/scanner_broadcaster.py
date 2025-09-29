import math
import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

class ScannerBroadcaster(Node):

    def __init__(self):
        super().__init__("scanner_broadcaster")
        self.broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_transform)

    def broadcast_transform(self):
        t = self.get_clock().now().seconds_nanoseconds()[0] + \
            self.get_clock().now().seconds_nanoseconds()[1] / 1e9
        
        transform_stamped = TransformStamped()
        transform_stamped.header.stamp = self.get_clock().now().to_msg()
        transform_stamped.header.frame_id = "robot"
        transform_stamped.child_frame_id = "scanner"

        transform_stamped.transform.translation.x = 0.3
        transform_stamped.transform.translation.y = 0.3 * math.sin(2 * math.pi * 0.5 * t)
        transform_stamped.transform.translation.z =0.6

        transform_stamped.transform.rotation.x = 0.0
        transform_stamped.transform.rotation.y = 0.0
        transform_stamped.transform.rotation.z = 0.0
        transform_stamped.transform.rotation.w = 1.0

        self.broadcaster.sendTransform(transform_stamped)

def main(args=None):
    rclpy.init(args=args)
    node = ScannerBroadcaster()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
