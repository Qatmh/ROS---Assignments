# TASK 3
In this task, we created a python node named lidar_broadcaster.py which publishes static transform from the robot frame to lidar. Second node scanner_broadcaster.py was implemented to broadcast dynamic transform from the robot to scanner while oscillating along the y-axis 0.3 at frequency of 0.5 Hz. To verify these we created tf_listener.py which listens transforms from map to the lidar frame and prints the distance from the origin every two seconds and also calculates speed. Revolution_counter.py which counts the number of revolutions the robot makes around the map origin. 

## To run
> ros2 run task3 lidar_broadcaster

> ros2 run task3 scanner_broadcaster 
 
> ros2 run task3 revolution_counter 
 
> ros2 run task3 tf_listener 

<img width="1156" height="432" alt="rqt_tf_tree" src="https://github.com/user-attachments/assets/6174fb4b-9d46-482a-a90f-c59b08aa8640" />

# TASK 4

We created gazebo world that contais room with windows, door and table inside the room. world can be launched using launch file. In rviz the reference frame was set to the robot's base and tf transforms, laser scan data and camera image data were added.

## To run
> ros2 launch gazebo_example gazebo_example.launch.py
