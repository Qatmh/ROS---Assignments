from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'task3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
        glob(os.path.join('launch', '*launch.[pxy][y|a]ml]'))),
        (os.path.join('share', package_name, 'img_data'),
        glob(os.path.join('img_data', '*.*'))),
        ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lassi',
    maintainer_email='lasahl02@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lidar_broadcaster = task3.lidar_broadcaster:main',
            'scanner_broadcaster = task3.scanner_broadcaster:main',
            'revolution_counter = task3.revolution_listener:main',
            'tf_listener = task3.tf_listener:main',
        ],
    },
)
