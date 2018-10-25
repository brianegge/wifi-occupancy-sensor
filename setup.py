#!/usr/bin/python


from setuptools import setup

setup(
    name='wifi_occupancy_sensor',
    version='0.0.1',
    packages=['wifi_occupancy_sensor'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_restful',
    ],
)
