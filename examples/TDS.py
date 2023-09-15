"""
MicroPython Eduponics mini TDS sensor - demo
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

from Eduponics import ads1x15,tds
from machine import Pin
from machine import SoftI2C as I2C
import time

# IO12 reserved for powering the board, define it
power = Pin(12, Pin.OUT)
# activate the board
power.value(1)

# make sure to wait enough time for the board to wakeup
time.sleep(0.1)

# setup I2C
i2c = I2C(scl=Pin(33), sda=Pin(32))

# intialize the TDS sensor
tds = tds.TDS(i2c=i2c,channel=0)

# while true, keep checking value
while True:
    # NOTE: the mosfet will turn on and off after testing from ADS chip
    # it's suggested to wait 0.5-1 seconds or more between testing data
    # frequent mosfet openening and closing might shorten it's lifespan.
    print("TDS: %s" % tds.read())
    time.sleep(0.5)
