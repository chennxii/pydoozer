#!/usr/bin/env python

from setuptools import setup

setup(
    name='PyDoozer',
    version='0.2.1',
    author='Jeff Lindsay',
    author_email='jeff.lindsay@twilio.com',
    description='doozer client',
    packages=['doozer'],
    install_requires=['gevent', 'protobuf'],
    data_files=[],
)
