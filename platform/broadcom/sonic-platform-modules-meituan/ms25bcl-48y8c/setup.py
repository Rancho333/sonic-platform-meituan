#!/usr/bin/env python

import os
import sys
from setuptools import setup
os.listdir

setup(
   name='sonic_platform',
   version='1.0',
   description='Module to initialize Celestica B3010 platforms',
      
   packages=['b3010', 'sonic_platform'],
   package_dir={'b3010'      : 'classes',
                'sonic_platform': 'sonic_platform'},
)

