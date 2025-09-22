from setuptools import find_packages, setup

package_name = 'countdown_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'countdown_interfaces'],
    zip_safe=True,
    maintainer='mahmmudqatmh',
    maintainer_email='mdqatm@utu.fi',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'countdown_server = countdown_nodes.countdown_server:main',
        'countdown_client = countdown_nodes.countdown_client:main',
        'countdown_cancel_client = countdown_nodes.countdown_cancel_client:main',
        ],
    },
)
