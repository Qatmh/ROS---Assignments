import rclpy
from rclpy.node import Node
from person_msgs.msg import Person
import random

class PersonPublisher(Node):
    def __init__(self):
        super().__init__('person_publisher')
        self.publisher_ = self.create_publisher(Person, 'person_info', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1 Hz

    def timer_callback(self):
        msg = Person()
        msg.name = "Student_" + str(random.randint(1, 100))
        msg.age = random.randint(10, 18)
        msg.is_student = True
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: name={msg.name}, age={msg.age}, is_student={msg.is_student}')

def main(args=None):
    rclpy.init(args=args)
    node = PersonPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
