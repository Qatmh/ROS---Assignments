import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import cv2
import numpy as np
import time
from cv_bridge import CvBridge

class cameraSubscriber(Node):
    def __init__(self):
        super().__init__("camera_subscriber")
        self.subscription = self.create_subscription(
            CompressedImage, "camera/image_raw/compressed",
            self.listener_callback, 10)
        
        self.frames = 0
        self.start_time = time.time()

        self.bridge = CvBridge()
    
    def listener_callback(self, msg):

        frame = self.bridge.compressed_imgmsg_to_cv2(msg, desired_encoding="bgr8")
        self.frames += 1

        ros_time = msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        height, width, _ = frame.shape

        cv2.putText(frame, f"Frame: {self.frames} (Compressed)", (0, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f"size: {width}X{height}", (0, 70), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f"ROS Time: {ros_time}", (0, 110), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f"Elapsed: {elapsed_time:.1f}s", (0, 150), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        cv2.imshow("Compressed image processing", frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = cameraSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()