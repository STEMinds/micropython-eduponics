#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'eduponics')))

from Eduponics import __version__
sys.path.pop(0)

setup(
    name='micropython-eduponics',
    packages=find_packages(),
    include_package_data=True,
    version=__version__,
    download_url = 'https://github.com/STEMinds/micropython-eduponics/archive/1.0.7.tar.gz',
    keywords = ["STEMinds",'MicroPython','uPython', 'Eduponics-Mini', 'Eduponics', 'ESP32', 'ADS1x15', 'MCP23017', 'TDS', 'pH', 'bh1750', 'BME280', 'DS1307', 'AT24C02'],
    description='',
    long_description='',
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        "Programming Language :: Python :: Implementation :: MicroPython",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    author='STEMinds',
    author_email='contact@steminds.com',
    url='https://github.com/STEMinds/micropython-eduponics',
    install_requires=[''],
)
