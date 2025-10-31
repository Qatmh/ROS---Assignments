#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx
from queue import PriorityQueue
import time


class DijkstraExplorer(Node):
    def __init__(self):
        super().__init__('dijkstra_explorer_task4')

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

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

        self.timer = self.create_timer(0.1, self.navigate)

        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0

        self.start_node = 0
        self.visited = [self.start_node]
        self.total_path = [self.start_node]
        self.current_path = []
        self.current_index = 0
        self.target_node = None
        self.total_cost = 0.0

        self.traj_x, self.traj_y = [], []
        self.start_time = time.time()
        self.plan_next_target()

    def odom_callback(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        self.yaw = math.atan2(siny_cosp, cosy_cosp)
        self.traj_x.append(self.x)
        self.traj_y.append(self.y)

    def run_dijkstra(self, start, goal):
        q = PriorityQueue()
        q.put((0, start, [start]))
        visited = set()
        while not q.empty():
            cost, node, path = q.get()
            if node == goal:
                return path, cost
            if node in visited:
                continue
            visited.add(node)
            for n in range(self.num_nodes):
                if self.adj[node, n] == 1 and n not in visited:
                    new_cost = cost + self.weights[node, n]
                    q.put((new_cost, n, path + [n]))
        return [], np.inf

    def plan_next_target(self):
        current = self.total_path[-1]
        nearest, best_cost, best_path = None, float('inf'), []

        for node in range(self.num_nodes):
            if node not in self.visited:
                path, cost = self.run_dijkstra(current, node)
                if cost < best_cost:
                    nearest, best_cost, best_path = node, cost, path

        if nearest is None:
            self.get_logger().info("All nodes visited")
            self.stop_robot()
            self.plot_results()
            rclpy.shutdown()
            return

        self.target_node = nearest
        self.current_path = [tuple(self.waypoints[i]) for i in best_path]
        self.current_index = 0
        self.visited.append(nearest)
        self.total_path.extend(best_path[1:])
        self.total_cost += best_cost
        self.get_logger().info(f"Next target: Node {nearest} Cost {best_cost:.2f}m Path {best_path}")

    def navigate(self):
        if not self.current_path:
            return

        goal_x, goal_y = self.current_path[self.current_index]
        dx, dy = goal_x - self.x, goal_y - self.y
        dist = math.hypot(dx, dy)
        goal_angle = math.atan2(dy, dx)
        angle_err = self.normalize_angle(goal_angle - self.yaw)

        cmd = Twist()
        if abs(angle_err) > 0.3:
            cmd.angular.z = 0.8 * angle_err
        elif dist > 0.2:
            cmd.linear.x = 0.15
            cmd.angular.z = 0.4 * angle_err
        else:
            self.current_index += 1
            if self.current_index >= len(self.current_path):
                self.get_logger().info(f"Reached node {self.target_node}")
                self.plan_next_target()

        self.cmd_pub.publish(cmd)

    def normalize_angle(self, a):
        while a > math.pi: a -= 2 * math.pi
        while a < -math.pi: a += 2 * math.pi
        return a

    def stop_robot(self):
        self.cmd_pub.publish(Twist())

    def plot_results(self):
        G = nx.Graph()
        G.add_edges_from(self.edges)
        pos = {i: (self.waypoints[i][0], self.waypoints[i][1]) for i in range(self.num_nodes)}

        plt.figure(figsize=(7, 6))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
        path_edges = list(zip(self.total_path, self.total_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
        nx.draw_networkx_nodes(G, pos, nodelist=self.visited, node_color='orange', node_size=900)
        nx.draw_networkx_nodes(G, pos, nodelist=[self.start_node], node_color='green', node_size=1000)
        nx.draw_networkx_nodes(G, pos, nodelist=[self.total_path[-1]], node_color='red', node_size=1000)

        plt.title(f"Visited: {len(self.visited)} Total cost: {self.total_cost:.2f}m")
        plt.xlabel("X (m)")
        plt.ylabel("Y (m)")
        plt.grid(True)

        plt.plot(self.traj_x, self.traj_y, 'r-', linewidth=2, label='Actual Trajectory')
        plt.legend()
        plt.show()


def main(args=None):
    rclpy.init(args=args)
    node = DijkstraExplorer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
