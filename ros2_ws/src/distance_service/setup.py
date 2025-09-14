from setuptools import find_packages, setup
package_name = 'distance_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'custom_interface'],
    zip_safe=True,
    maintainer='lassi',
    maintainer_email='lasahl02@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "distance_server = distance_service.distance_server:main",
            "distance_client = distance_service.distance_client:main"
        ],
    },
)


