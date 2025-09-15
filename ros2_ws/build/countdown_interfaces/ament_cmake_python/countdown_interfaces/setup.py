from setuptools import find_packages
from setuptools import setup

setup(
    name='countdown_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('countdown_interfaces', 'countdown_interfaces.*')),
)
