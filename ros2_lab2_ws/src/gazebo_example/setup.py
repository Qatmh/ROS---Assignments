from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'gazebo_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch',
        '*.py'))),
        # Install world files
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds',
        '*.world'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lassi',
    maintainer_email='lasahl02@gmail.com',
    description='TODO: Package description',
    license='Apache-',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
