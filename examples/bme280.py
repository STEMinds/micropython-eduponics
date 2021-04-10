"""
MicroPython BME280 temperature, humidity and air-pressure sensor
https://github.com/STEMinds/micropython-eduponics
MIT License
Copyright (c) 2021 STEMinds

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from machine import I2C,Pin
from Eduponics import bme280
from utime import sleep

# setup I2C connection
i2c = I2C(scl=Pin(15), sda=Pin(4))

# Initialize BME280 object with default address 0x76
bme280 = bme280.BME280(i2c=i2c)

while True:
    # get the values from the BME280 library
    values = bme280.values
    altitude = bme280.altitude
    dew_point = bme280.dew_point
    sea_level = bme280.sealevel
    # print the values every 1 second
    print("------------------------")
    print("Temperature: %s" % values[0])
    print("Humidity: %s" % values[1])
    print("Pressure: %s" % values[2])
    print("Altitude: %s" % altitude)
    print("Dew point: %s" % dew_point)
    print("Sea level: %s" % sea_level)
    print("------------------------")
    print("")
    sleep(1)
