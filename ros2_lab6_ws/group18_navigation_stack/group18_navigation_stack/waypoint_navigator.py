import os
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import numpy as np
import matplotlib.pyplot as plt 

class WaypointNavigator(Node):
    def __init__(self):
        super().__init__("waypoint_navigator")

        self.waypoints = [
            (-8.0, 4.5),
            (6.0, 5.5),
            (6.0, 1.0),
            (-4.0, 1.0),
            (-4.0, -4.0),
            (8.0, -4.0)
        ]
        self.current_index = 0
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0

        self.cmd_pub = self.create_publisher(Twist, "/cmd_vel", 10)
        self.odom_sub = self.create_subscription(Odometry, "/odom", self.odom_callback, 10)

        self.path = []
        self.odom_time = []
        self.odom_line = []
        self.odom_angle = []


        self.timer = self.create_timer(0.1, self.navigation)
        

    def odom_callback(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        
        q = msg.pose.pose.orientation
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        self.yaw = math.atan2(siny_cosp, cosy_cosp)
        
        self.path.append((self.x, self.y))
        now = self.get_clock().now().seconds_nanoseconds()[0]
        self.odom_time.append(now)
        self.odom_line.append(msg.twist.twist.linear.x)
        self.odom_angle.append(msg.twist.twist.angular.z)
        
    def navigation(self):
        if self.current_index >= len(self.waypoints):
            self.plotting()
            return

        x_point, y_point = self.waypoints[self.current_index]
        dx = x_point - self.x
        dy = y_point - self.y
        distance = math.sqrt(dx**2 + dy**2)
        angle = math.atan2(dy, dx)
        angle_error = self.angle_diff(angle, self.yaw)

        twist = Twist()

        if abs(angle_error) > 0.2:
            twist.angular.z = 1 * angle_error
        elif distance > 0.05:
            twist.linear.x = 0.25
        else:
            self.get_logger().info(f"reached waypoint {self.current_index + 1}")
            self.current_index += 1
        
        self.cmd_pub.publish(twist)

    def angle_diff(self, a, b):
        diff = a - b
        while diff > math.pi:
            diff -= 2 * math.pi
        while diff < -math.pi:
            diff += 2 * math.pi
        return diff
    
    def plotting(self):
        twist = Twist()
        self.cmd_pub.publish(twist)
        self.get_logger().info("Path done")

        path = np.array(self.path)
        times = np.array(self.odom_time)
        line = np.array(self.odom_line)
        angle = np.array(self.odom_angle)

        map_file = "mymap.csv"
        os.path.exists(map_file)
        grid = np.loadtxt(map_file, delimiter=",")
        plt.figure(figsize=(6, 6))
        plt.title("path over grid")
        plt.imshow(grid, cmap="gray", origin="lower")
        plt.plot(path[:,0] / 0.1 + grid.shape[1]//2,
                    path[:,1] / 0.1 + grid.shape[0]//2, "r-", linewidth=2)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()

        
        t0 = times[0]
        plt.figure()
        plt.title("velocity vs time")
        plt.plot(times - t0, line, label="Linear (m/s)")
        plt.plot(times - t0, angle, label="angular (rad/s)")
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity")
        plt.legend()
        plt.grid(True)
        plt.show()



def main(args=None):
    rclpy.init(args=args)
    node = WaypointNavigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()