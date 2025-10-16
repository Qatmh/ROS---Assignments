#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import numpy as np
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry, OccupancyGrid
from math import cos, sin
from std_msgs.msg import Header


class LidarMappingNode(Node):
    def __init__(self):
        super().__init__('lidar_mapping')
        
        self.grid_size = 0.1  # 10 cm
        self.map_size = 200 #20m x 20m
        self.origin = [100, 100]  # Center of the map
        self.room_map = np.full((self.map_size, self.map_size), -1)  # All unknown initially

        self.subscription_scan = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.subscription_odom = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

        # Publisher for RViz
        self.map_pub = self.create_publisher(OccupancyGrid, '/lidar_map', 10)
        self.timer = self.create_timer(1.0, self.publish_map)
        
        self.robot_x = 0.0
        self.robot_y = 0.0
        self.robot_yaw = 0.0

    def publish_map(self):
        map_msg = OccupancyGrid()
        map_msg.header = Header()
        map_msg.header.stamp = self.get_clock().now().to_msg()
        map_msg.header.frame_id = "map"

        map_msg.info.resolution = self.grid_size
        map_msg.info.width = self.map_size
        map_msg.info.height = self.map_size

        map_msg.info.origin.position.x = -self.origin[0] * self.grid_size
        map_msg.info.origin.position.y = -self.origin[1] * self.grid_size
        map_msg.info.origin.position.z = 0.0

        ros_map = np.copy(self.room_map)
        ros_map[ros_map == 1] = 100

        map_msg.data = ros_map.T.flatten().tolist()

        self.map_pub.publish(map_msg)
    
    def odom_callback(self, msg):
        self.robot_x = msg.pose.pose.position.x
        self.robot_y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        self.robot_yaw = np.arctan2(siny_cosp, cosy_cosp)

    def scan_callback(self, msg):
        num_rays = len(msg.ranges)
        angles = msg.angle_min + np.arange(num_rays) * msg.angle_increment
        ranges = np.array(msg.ranges)

        # Robot grid position
        rx = int(self.robot_x / self.grid_size) + self.origin[0]
        ry = int(self.robot_y / self.grid_size) + self.origin[1]

        for i in range(num_rays):
            distance = ranges[i]
            if not np.isfinite(distance) or distance < msg.range_min or distance > msg.range_max:
                continue

            angle = angles[i]
            x_world = self.robot_x + distance * cos(angle + self.robot_yaw)
            y_world = self.robot_y + distance * sin(angle + self.robot_yaw)

            # Convert to grid
            gx = int(x_world / self.grid_size) + self.origin[0]
            gy = int(y_world / self.grid_size) + self.origin[1]

            if not (0 <= gx < self.map_size and 0 <= gy < self.map_size):
                continue

            line_points = bresenham_points([rx, ry], [gx, gy])

            # Mark free space
            for x, y in line_points:
                if 0 <= x < self.map_size and 0 <= y < self.map_size:
                    if self.room_map[y, x] == -1:
                        self.room_map[y, x] = 0

            # Mark obstacle
            self.room_map[gy, gx] = 1  
    

def bresenham_points(p0, p1):
    point_list = []  # We will fill this list with all points in between p0 and p1

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
        if [x0, y0] != p0 and [x0, y0] != p1:  # exclude first and last
            point_list.append([x0, y0])
        if x0 == x1 and y0 == y1:
            break  # This means we have finished, so we break the loop

        e2 = 2 * err
        if e2 > -dy:
            # overshot in the y direction
            err = err - dy
            x0 = x0 + sx
        if e2 < dx:
            # overshot in the x direction
            err = err + dx
            y0 = y0 + sy

    return point_list


def main(args=None):
    rclpy.init(args=args)
    node = LidarMappingNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
