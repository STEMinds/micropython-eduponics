"""
MicroPython Eduponics mini water activated pump - demo
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

import machine
import esp32
import time

# define pump on pin IO23 as OUTPUT
pump = machine.Pin(23, machine.Pin.OUT, machine.Pin.PULL_UP)
# define water level sensor as INPUT on IO pin number 21
water_level = machine.Pin(21, machine.Pin.IN)
# define wakeup button and callback
wake_up = machine.Pin(36, mode = machine.Pin.IN)

def water_level_change(pin):
    return 1

def wakeup_pressed(pin):
    # turn on the pump
    pump.value(pin)
    print("pressed")

# define the callbacks for the sensors
water_level.irq(trigger=machine.Pin.IRQ_FALLING, handler=water_level_change)
wake_up.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=wakeup_pressed)
