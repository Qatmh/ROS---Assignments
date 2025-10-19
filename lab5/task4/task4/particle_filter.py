#!/usr/bin/env python

import rclpy
from rclpy.node import Node

import sys
import time
from pfilter import (
    ParticleFilter,
    gaussian_noise,
    cauchy_noise,
    t_noise,
    squared_error,
    independent_sample,
)
import numpy as np

from scipy.stats import norm, gamma, uniform

from std_msgs.msg       import Float64
from sensor_msgs.msg    import LaserScan
from geometry_msgs.msg  import PoseStamped
from geometry_msgs.msg  import PoseWithCovarianceStamped
from geometry_msgs.msg  import PoseArray
from sensor_msgs.msg    import Range
from nav_msgs.msg       import Odometry
from rclpy.clock        import Clock
from rclpy.duration     import Duration
from pfilter            import ParticleFilter, squared_error


from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy
import math
import matplotlib.pyplot as plt

def quat_to_yaw(q): 
    x, y, z, w = q.x, q.y, q.z, q.w 
    siny_cosp = 2 * (w * z + x * y) 
    cosy_cosp = 1 - 2 * (y * y + z * z) 
    return math.atan2(siny_cosp, cosy_cosp)

class LidarParticleFilter(Node):
    def __init__(self):
        super().__init__('lidar_position_pf_rclpy')

        self.num_particles = 400
        self.measurement_noise = 0.05
        self.weights_sigma = 1.2
        self.resample_proportion = 0.01

        self.real_obstacle_position = np.array([2.0, -2.0])

        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odometry_cb, 10)
        self.scan_sub = self.create_subscription(LaserScan, '/scan', self.scan_cb, 10)

        self.odometry = None
        self.scan = None

        self.prev_odom_pos = None
        self.prev_odom_yaw = None

        self.true_x = []
        self.true_y = []
        self.est_x = []
        self.est_y = []

        self.particle_odom = np.array([0.0, 0.0])
        self.particle_dtheta = 0.0

        def dynamics_fn(x):
            dx = self.particle_odom
            dth = self.particle_dtheta
            xp = np.empty_like(x)
            xp[:, 0] = x[:, 0] + dx[0]
            xp[:, 1] = x[:, 1] + dx[1]
            xp[:, 2] = x[:, 2] + dth
            xp[:, 2] = (xp[:, 2] + math.pi) % (2 * math.pi) - math.pi
            return xp

        self.prior_fn = lambda n: np.column_stack((
            np.random.uniform(-5, 5, n),
            np.random.uniform(-5, 5, n),
            np.random.uniform(-math.pi, math.pi, n)))

        self.pf = ParticleFilter(
            prior_fn=self.prior_fn,
            observe_fn=self.calc_hypothesis,
            dynamics_fn=dynamics_fn,
            n_particles=self.num_particles,
            noise_fn=self.add_noise,
            weight_fn=self.calc_weights,
            resample_proportion=self.resample_proportion,
        )

        self.pf.init_filter()

        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.odom_line, = self.ax.plot([], [], 'b-', label='Odometry')
        self.est_line, = self.ax.plot([], [], 'r--', label='Estimate')
        self.ax.legend()
        self.ax.set_xlabel('X (m)')
        self.ax.set_ylabel('Y (m)')
        self.ax.set_title('Live Particle Filter Localization')
        self.ax.grid(True)
        self.fig.show()
        self.fig.canvas.draw()

    def odometry_cb(self, odom):
        self.odometry = odom

    def scan_cb(self, scan):
        self.scan = scan

    def calc_hypothesis(self, x):
        dx = self.real_obstacle_position[0] - x[:, 0]
        dy = self.real_obstacle_position[1] - x[:, 1]
        v = np.column_stack((dx, dy))
        cos_t = np.cos(-x[:, 2])
        sin_t = np.sin(-x[:, 2])
        rx = cos_t * v[:, 0] - sin_t * v[:, 1]
        ry = sin_t * v[:, 0] + cos_t * v[:, 1]
        return np.column_stack((rx, ry))

    def add_noise(self, x):
        xp = np.empty_like(x)
        xp[:, 0] = x[:, 0] + np.random.normal(0, self.measurement_noise, x.shape[0])
        xp[:, 1] = x[:, 1] + np.random.normal(0, self.measurement_noise, x.shape[0])
        xp[:, 2] = x[:, 2] + np.random.normal(0, self.measurement_noise / 2.0, x.shape[0])
        xp[:, 2] = (xp[:, 2] + math.pi) % (2 * math.pi) - math.pi
        return xp

    def calc_weights(self, hypotheses, observations):
        return squared_error(hypotheses, observations, sigma=self.weights_sigma)

    def update_filter(self):
        if self.odometry is None or self.scan is None:
            return

        robot_pos = np.array([self.odometry.pose.pose.position.x, self.odometry.pose.pose.position.y])
        robot_yaw = quat_to_yaw(self.odometry.pose.pose.orientation)

        if self.prev_odom_pos is None:
            self.prev_odom_pos = robot_pos.copy()
            self.prev_odom_yaw = robot_yaw
            self.particle_odom = np.array([0.0, 0.0])
            self.particle_dtheta = 0.0
        else:
            delta = robot_pos - self.prev_odom_pos
            self.particle_odom = delta
            dtheta = robot_yaw - self.prev_odom_yaw
            dtheta = (dtheta + math.pi) % (2 * math.pi) - math.pi
            self.particle_dtheta = dtheta
            self.prev_odom_pos = robot_pos.copy()
            self.prev_odom_yaw = robot_yaw

        ranges = np.array(self.scan.ranges)
        valid_mask = np.isfinite(ranges) & (ranges > self.scan.range_min) & (ranges < self.scan.range_max)
        if not np.any(valid_mask):
            return
        valid_indices = np.where(valid_mask)[0]
        min_idx = valid_indices[np.argmin(ranges[valid_indices])]
        r = ranges[min_idx]
        angle = self.scan.angle_min + min_idx * self.scan.angle_increment
        obs_x = r * math.cos(angle)
        obs_y = r * math.sin(angle)
        relative_obstacle_pos = np.array([obs_x, obs_y])

        self.pf.update(observed=relative_obstacle_pos)
        mean = self.pf.mean_state

        self.true_x.append(robot_pos[0])
        self.true_y.append(robot_pos[1])
        self.est_x.append(mean[0])
        self.est_y.append(mean[1])

        self.odom_line.set_data(self.true_x, self.true_y)
        self.est_line.set_data(self.est_x, self.est_y)
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def plot(self):
        plt.ioff()
        plt.savefig('particle_filter_live_plot.png')
        plt.close(self.fig)
        self.destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = LidarParticleFilter()
    timer = node.create_timer(0.2, node.update_filter)
    rclpy.spin(node)
    node.plot()
    rclpy.shutdown()

