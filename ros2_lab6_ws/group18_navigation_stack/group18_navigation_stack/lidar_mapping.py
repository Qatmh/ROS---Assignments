import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from std_msgs.msg import String
import numpy as np
import math
import os
from rclpy.time import Time

class LidarMappingNode(Node):
    def __init__(self):
        super().__init__('lidar_mapping')

        self.grid_size = 0.1  # 10 cm
        self.map_size = 200 #20m x 20m
        self.origin = [100, 100]  # Center of the map
        self.room_map = np.full((self.map_size, self.map_size), -1)  # All unknown initially

        self.subscription_scan = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.subscription_odom = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

        self.map_pub = self.create_publisher(String, '/map_path', 10)
        self.timer = self.create_timer(2.0, self.save_map)
        
        self.robot_x = 0.0
        self.robot_y = 0.0
        self.robot_yaw = 0.0

        self.get_logger().info("Lidar mapper started")

    def odom_callback(self, msg):
        self.robot_x = msg.pose.pose.position.x
        self.robot_y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        self.robot_yaw = math.atan2(siny_cosp, cosy_cosp)

    def scan_callback(self, msg):
        rays = len(msg.ranges)
        angles = msg.angle_min + np.arange(rays) * msg.angle_increment
        ranges = np.array(msg.ranges)

        rx = int(self.robot_x / self.grid_size) + self.origin[0]
        ry = int(self.robot_y / self.grid_size) + self.origin[1]

        for i in range(rays):
            distance = ranges[i]
            if not np.isfinite(distance) or distance < msg.range_min or distance > msg.range_max:
                continue

            angle = angles[i]
            x_world = self.robot_x + distance * math.cos(angle + self.robot_yaw)
            y_world = self.robot_y + distance * math.sin(angle + self.robot_yaw)
        
            grid_x = int(x_world / self.grid_size) + self.origin[0]
            grid_y = int(y_world / self.grid_size) + self.origin[1]

            if not (0 <= grid_x < self.map_size and 0 <= grid_y < self.map_size):
                continue

            line_points = self.bresenham_points([rx, ry], [grid_x, grid_y])

            for x, y in line_points:
                if 0 <= x < self.map_size and 0 <= y < self.map_size:
                    if self.room_map[y, x] == -1:
                        self.room_map[y, x] = 0
            
            self.room_map[grid_y, grid_x] = 1

    def bresenham_points(self, p0, p1):
        point_list = []

        x0, y0 = p0[0], p0[1]
        x1, y1 = p1[0], p1[1]

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        if x0 < x1:
            sx = 1
        else:
            sx = -1

        if y0 < y1:
            sy = 1
        else:
            sy = -1

        err = dx - dy

        while True:
            if [x0, y0] != p0 and [x0, y0] != p1:
                point_list.append([x0, y0])
            if x0 == x1 and y0 == y1:
                break 

            e2 = 2 * err
            if e2 > -dy:
                err = err - dy
                x0 = x0 + sx
            if e2 < dx:
                err = err + dx
                y0 = y0 + sy

        return point_list
    
    def save_map(self):
        np.savetxt("mymap.csv", self.room_map, delimiter=",")

        msg = String()
        msg.data = os.path.abspath("mymap.csv")
        self.map_pub.publish(msg)

        self.get_logger().info("Map saved")


def main(args=None):
    rclpy.init(args=args)
    node = LidarMappingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()