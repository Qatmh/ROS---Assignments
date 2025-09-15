import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

class PersonSubscriber(Node):
    def __init__(self):
        super().__init__('person_subscriber')
        self.subscription = self.create_subscription(
            Person,
            'person_info',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: name={msg.name}, age={msg.age}, is_student={msg.is_student}')

def main(args=None):
    rclpy.init(args=args)
    node = PersonSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
