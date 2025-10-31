#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue


class DijkstraPlanner(Node):
    def __init__(self):
        super().__init__('dijkstra')

        self.waypoints = np.array([
            [-8.0, 4.5],
            [6.0, 4.5],
            [6.0, 1.0],
            [-3.0, 1.0],
            [-4.0, -4.0],
            [8.0, -4.0],
        ])
        self.num_nodes = len(self.waypoints)

        self.edges = [
            (0, 1), (1, 2), (2, 3),
            (3, 4), (4, 5), (0, 3), (1, 5), (2, 5)
        ]
 
        self.adj = np.zeros((self.num_nodes, self.num_nodes), dtype=int)
        self.weights = np.full((self.num_nodes, self.num_nodes), np.inf)
        for i, j in self.edges:
            d = np.linalg.norm(self.waypoints[i] - self.waypoints[j])
            self.adj[i, j] = self.adj[j, i] = 1
            self.weights[i, j] = self.weights[j, i] = d

        self.start = 3
        self.goal = 1

        self.path, self.cost = self.run_dijkstra(self.start, self.goal)
        self.get_logger().info(f"Path found: {self.path} | Cost = {self.cost:.2f}")

        self.plot_path()

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.timer = self.create_timer(0.1, self.navigate)

        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.current_index = 0
        self.path_points = [tuple(self.waypoints[i]) for i in self.path]

    def run_dijkstra(self, start, goal):
        q = PriorityQueue()
        q.put((0, start, [start]))
        visited = set()

        while not q.empty():
            cost, node, path = q.get()
            if node in visited:
                continue
            visited.add(node)

            if node == goal:
                return path, cost

            for neighbor in range(self.num_nodes):
                if self.adj[node, neighbor] == 1 and neighbor not in visited:
                    new_cost = cost + self.weights[node, neighbor]
                    q.put((new_cost, neighbor, path + [neighbor]))

        return [], np.inf

    def plot_path(self):
        G = nx.Graph()
        G.add_edges_from(self.edges)
        pos = {i: (self.waypoints[i][0], self.waypoints[i][1]) for i in range(self.num_nodes)}

        plt.figure(figsize=(6, 5))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
        path_edges = list(zip(self.path, self.path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=3)
        nx.draw_networkx_nodes(G, pos, nodelist=[self.start], node_color='green', node_size=900)
        nx.draw_networkx_nodes(G, pos, nodelist=[self.goal], node_color='red', node_size=900)
        plt.title(f"Dijkstra Path {self.start} to {self.goal} | Cost = {self.cost:.2f}")
        plt.grid(True)
        plt.show()

    def odom_callback(self, msg):
        """Get robot position and orientation"""
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation
        siny = 2 * (q.w * q.z + q.x * q.y)
        cosy = 1 - 2 * (q.y * q.y + q.z * q.z)
        self.yaw = math.atan2(siny, cosy)

    def navigate(self):
        if self.current_index >= len(self.path_points):
            self.stop()
            self.get_logger().info("Reached goal!")
            rclpy.shutdown()
            return

        gx, gy = self.path_points[self.current_index]
        dx, dy = gx - self.x, gy - self.y
        dist = math.sqrt(dx**2 + dy**2)
        target_angle = math.atan2(dy, dx)
        angle_error = self.angle_diff(target_angle, self.yaw)

        cmd = Twist()
        if abs(angle_error) > 0.3:
            cmd.angular.z = 0.6 * angle_error
        elif dist > 0.2:
            cmd.linear.x = 0.15
        else:
            self.get_logger().info(f"Reached node {self.path[self.current_index]}")
            self.current_index += 1

        self.cmd_pub.publish(cmd)

    def stop(self):
        """Stop robot motion"""
        self.cmd_pub.publish(Twist())

    def angle_diff(self, a, b):
        diff = a - b
        while diff > math.pi:
            diff -= 2 * math.pi
        while diff < -math.pi:
            diff += 2 * math.pi
        return diff


def main(args=None):
    rclpy.init(args=args)
    node = DijkstraPlanner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
