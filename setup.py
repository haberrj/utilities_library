# Author: Ron Haber
# Date: 3.1.2021

from setuptools import find_packages, setup

setup(
    name='haber_utils',
    packages=find_packages(include=['haber_utils']),
    version='0.1.0',
    description='General utility functions that keep being rewritten',
    author='Ron Haber',
    license='N/A',
    install_requires=['pandas'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)