import rclpy
from rclpy.node import Node
from custom_interface.srv import Distance
import math

class DistanceServer(Node):

    def __init__(self):
        super().__init__("distance_server")
        self.server_ = self.create_service(Distance, "Calculate_distance", self.distance_callback)
        self.get_logger().info("Service server Python node has been created")
    

    def distance_callback(self, request, response): 
        try:
            dx = request.a.x - request.b.x
            dy = request.a.y - request.b.y
            distance = math.sqrt(dx**2 + dy**2)
            response.distance = distance
            response.success = True
            response.message = f"Successfully calculated {distance:.3f}"
        except Exception as e:
            response.distance = 0.0
            response.success = False
            response.message = f"Error {str(e)}"
        return response 


def main(args = None):
    rclpy.init(args=args)
    node = DistanceServer()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__=='__main__':
    main()