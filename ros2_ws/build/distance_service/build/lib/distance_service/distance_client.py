import rclpy
from rclpy.node import Node
from custom_interface.srv import Distance
from geometry_msgs.msg import Point

class DistanceClient(Node):

    def __init__(self):
        super().__init__('distance_client')
        
        self.declare_parameter("a_x", 0.0)
        self.declare_parameter("a_y", 0.0)
        self.declare_parameter("b_x", 0.0)
        self.declare_parameter("b_y", 0.0)

        p1_x = self.get_parameter("a_x").value
        p1_y = self.get_parameter("a_y").value
        p2_x = self.get_parameter("b_x").value
        p2_y = self.get_parameter("b_y").value

        client = self.create_client(Distance, 'Calculate_distance')
        while not client.wait_for_service(1.0):
            self.get_logger().info('Waiting for the Server...')

        a = Point(x=p1_x, y=p1_y)
        b = Point(x=p2_x, y=p2_y)
        
        request = Distance.Request()
        request.a = a
        request.b = b

        future = client.call_async(request)
        future.add_done_callback(self.distance_callback)


    def distance_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Distance: {response.distance:.3f}")
            self.get_logger().info(f"Success: {response.success}")
            self.get_logger().info(f"Message: {response.message}")
        except Exception as e:
            self.get_logger().info(f'Service call failed {e}')


def main(args=None):
    rclpy.init(args=args)
    node = DistanceClient()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__=='__main__':
    main()