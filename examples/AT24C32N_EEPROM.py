"""
MicroPython TinyRTC I2C Module, DS1307 RTC + AT24C32N EEPROM
https://github.com/mcauser/micropython-tinyrtc
https://github.com/STEMinds/micropython-eduponics
MIT License
Copyright (c) 2018 Mike Causer
              2021 STEMinds
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

# AT24C32A, 32K (32768 kbit / 4 KB), 128 pages, 32 bytes per page, i2c addr 0x50
from Eduponics import at24c02
import machine
import time

# initialize i2c connection
i2c = machine.I2C(scl=machine.Pin(15), sda=machine.Pin(4))

# define the EEPROM using the I2C
eeprom = at24c02.AT24C32N(i2c)

# print 32 bytes
print(eeprom.read(0, 32))

# write "hello world" starting from sector 0
eeprom.write(0, 'hello world')

# read 11 bytes from the EEPROM
print(eeprom.read(0, 11))
