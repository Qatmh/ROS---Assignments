import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class ColorFilterNode(Node):
    def __init__(self):
        super().__init__('color_filter_node')
        
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=10
        )

        self.subscription = self.create_subscription(
            Image, '/image_raw', 
            self.listener_callback, qos_profile
        )

        self.bridge = CvBridge()

    def add_label(self, image, label):
        return cv2.putText(image.copy(), label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    def concat_vh(self, image_list):
        return cv2.vconcat([cv2.hconcat(row) for row in image_list])

    def listener_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        resized_image = cv2.resize(image,(400, 300))
        
        hsv = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)

        lower_red1_hsv = np.array([0, 50, 70])
        upper_red1_hsv = np.array([10, 255, 255])
        lower_red2_hsv = np.array([170, 50, 70])
        upper_red2_hsv = np.array([179, 255, 255])

        lower_green_hsv = np.array([40, 50, 70])
        upper_green_hsv = np.array([80, 255, 255])

        lower_blue_hsv = np.array([100, 170, 50])
        upper_blue_hsv = np.array([130, 255, 255])

        red_mask = cv2.inRange(hsv, lower_red1_hsv, upper_red1_hsv) | cv2.inRange(hsv, lower_red2_hsv, upper_red2_hsv) 
        red_hsv = cv2.bitwise_and(resized_image, resized_image, mask=red_mask)
        
        green_mask = cv2.inRange(hsv, lower_green_hsv, upper_green_hsv)
        green_hsv = cv2.bitwise_and(resized_image, resized_image, mask=green_mask)
        
        blue_mask = cv2.inRange(hsv, lower_blue_hsv, upper_blue_hsv)
        blue_hsv = cv2.bitwise_and(resized_image, resized_image, mask=blue_mask)
        
        original = self.add_label(resized_image, "Original")
        red = self.add_label(red_hsv, "Red Filter")
        green = self.add_label(green_hsv, "Green Filter")
        blue = self.add_label(blue_hsv, "Blue Filter")

        grid = self.concat_vh([[original, red], 
                         [green, blue]])

        cv2.imshow("Task4", grid)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = ColorFilterNode()
    rclpy.spin(node)
    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()