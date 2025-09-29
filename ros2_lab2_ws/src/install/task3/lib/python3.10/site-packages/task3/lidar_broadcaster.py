import rclpy
from rclpy.node import Node
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped

class LidarBroadcaster(Node):

    def __init__(self):
        super().__init__("lidar_broadcaster")

        self.broadcaster = StaticTransformBroadcaster(self)

        self.make_transforms()

    def make_transforms(self):
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "robot"
        t.child_frame_id = "lidar"

        t.transform.translation.x = 0.3
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.5
        
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        
        self.broadcaster.sendTransform(t)
        self.get_logger().info("Published static transform: robot to lidar")

def main(args=None):
    rclpy.init(args=args)
    node = LidarBroadcaster()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()