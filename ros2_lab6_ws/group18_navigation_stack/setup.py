from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'group18_navigation_stack'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, "launch"), glob(os.path.join("launch",
        "*.py"))),
        (os.path.join("share", package_name, "worlds"), glob(os.path.join("worlds",
        "*.world")))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lassi',
    maintainer_email='lasahl02@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "lidar_mapper = group18_navigation_stack.lidar_mapping:main",
            "waypoint_navigator = group18_navigation_stack.waypoint_navigator:main",
            "dijkstra = group18_navigation_stack.dijkstra_planning:main",
            "astar = group18_navigation_stack.a_star_task3:main",
            "dijkstra_full = group18_navigation_stack.dijkstra_full_graph:main"
        ],
    },
)
