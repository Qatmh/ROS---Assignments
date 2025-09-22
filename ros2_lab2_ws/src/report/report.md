# TASK3
In this task, we created a python node named lidar_broadcaster.py which publishes static transform from the robot frame to lidar. Second node scanner_broadcaster.py was implemented to broadcast dynamic transform from the robot to scanner while oscillating along the y-axis 0.3 at frequency of 0.5 Hz. To verify these we created tf_listener.py which listens transforms from map to the lidar frame and prints the distance from the origin every two seconds and also calculates speed. Revolution_counter.py which counts the number of revolutions the robot makes around the map origin. 

# TASK 4

We created gazebo world that contais room with windows, door and table inside the room. world can be launched using launch file. In rviz the reference frame was set to the robot's base and tf transforms, laser scan data and camera image data were added.
