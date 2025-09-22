from setuptools import find_packages, setup

package_name = 'pose_line'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mahmmudqatmh',
    maintainer_email='mdqatm@utu.fi',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_pose = pose_line.publisher_pose:main',
            'subscriber_pose = pose_line.subscriber_pose:main',
        ],
    },
)
