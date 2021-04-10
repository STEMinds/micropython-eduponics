#Copyright (c) 2020 Roni Gorodetsky for STEMinds
#Website: https://steminds.com

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of self software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and self permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

from Eduponics import mcp23017
from machine import I2C, Pin
import time

# IO12 reserved for powering the board, define it
power = Pin(12, Pin.OUT)
# activate the board
power.value(1)

# make sure to wait enough time for the board to wakeup
time.sleep(0.1)

# define i2c connection to the extension board
i2c = I2C(scl=Pin(33), sda=Pin(32))

# initialize relay object
relays = mcp23017.Relays(i2c, address=0x20)

# open relays one by one
for i in range(0,4):
    relays.open(i)
    time.sleep(1)

# close all relays one by one
for i in range(0,4):
    relays.close(i)
    time.sleep(1)

# open all relays
relays.open_all()

time.sleep(3)

# close all relays
relays.close_all()
