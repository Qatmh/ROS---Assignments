import rclpy
from rclpy.node import Node
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
import math

class TFListener(Node):
    def __init__(self):
        super().__init__("tf_listener")
        self.tf_buffer = Buffer()
        self.listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(2.0 ,self.timer_callback)

        self.last_position = None
        self.last_time = None

    def timer_callback(self):
        try:
            transform = self.tf_buffer.lookup_transform(
                "map",
                "lidar",
                rclpy.time.Time()
            )
            x = transform.transform.translation.x
            y = transform.transform.translation.y
            z = transform.transform.translation.z
            distance = math.sqrt(x**2 + y**2 + z**2)

            now = self.get_clock().now().nanoseconds * 1e-9

            if self.last_position is not None:
                dt = now - self.last_time
                if dt > 0:
                    dx = x - self.last_position[0]
                    dy = y - self.last_position[1]
                    dz = z - self.last_position[2]
                    speed = math.sqrt(dx**2 + dy**2 + dz**2) / dt
                    self.get_logger().info(f"Speed relative to map: {speed:.3f} m/s")
            self.get_logger().info(f"Lidar distance from origin: {distance:.3f} m")

            self.last_position = (x, y, z)
            self.last_time = now
        
        except TransformException as ex:
            self.get_logger.info(f"Could not transform: {ex}")

def main(args=None):
    rclpy.init(args=args)
    node = TFListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()