import rclpy
from rclpy.node import Node
from tf2_ros import Buffer, TransformListener, TransformException
import math

class RevolutionCounter(Node):
    def __init__(self):
        super().__init__("revolution_counter")
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.timer = self.create_timer(0.1, self.timer_callback)
        self.revolutions = 0
        self.last_angle = None

    def timer_callback(self):
        try:
            transform = self.tf_buffer.lookup_transform(
                'map',
                'robot',
                rclpy.time.Time()
            )
        
            x = transform.transform.translation.x
            y = transform.transform.translation.y

            current_angle = math.atan(y, x)

            if self.last_angle is not None:
                angle_diff = current_angle - self.last_angle

                while angle_diff > math.pi:
                    angle_diff -= 2 * math.pi
                while angle_diff < -math.pi:
                    angle_diff += 2 * math.pi

                self.total_angle += angle_diff

                if angle_diff > math.pi/2:
                    self.revolutions -= 1
                elif angle_diff < -math.pi/2:
                    self.revolutions += 1
            
            self.last_angle = current_angle

            self.get_logger().info(f"Revolutions: {self.revolutions}")
        except TransformException as ex:
            self.get_logger().info(f"Could not transform: {ex}")

def main(args=None):
    rclpy.init(args=args)
    node = RevolutionCounter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()