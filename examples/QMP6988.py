"""
QMP6988 Example code for Eduponics mini v2.0
https://github.com/STEMinds/micropython-eduponics
MIT License
Copyright (c) 2022 STEMinds
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

from machine import Pin
from machine import SoftI2C as I2C
from Eduponics import qmp6988

# setup I2C connection
i2c = I2C(scl=Pin(15), sda=Pin(4))

def test_qmp6988():
    print("[-] Reading QMP6988 Barometric pressure sensor...")
    qmp = qmp6988.QMP6988(i2c)
    temp, pressure = qmp.measure()
    print("Temp/Pressure: {}°C/{}Pa".format(temp, pressure))
    print("")

# test qmp6988
test_qmp6988()
