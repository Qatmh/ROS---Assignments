from setuptools import find_packages, setup

package_name = 'person_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'person_msgs'], 
    zip_safe=True,
    maintainer='mahmmudqatmh',
    maintainer_email='mdqatm@utu.fi',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'publisher_person = person_node.publisher_person:main',
        'subscriber_person = person_node.subscriber_person:main',
        ],
    },
)
