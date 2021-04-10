"""
MicroPython Eduponics mini soil moisture sensor - demo
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

from machine import ADC,Pin

# set max val and min val of the sensor
# this requires manual calibration
# minVal get be recieved by putting the sensor submerged in the water
# maxVal can be recieved by making sure the sensor is dry in the clear air
minVal = 710
maxVal = 4095

def value_in_percentage(val):
    # scale the value based on maxVal and minVal
    scale = 100 / (minVal - maxVal)
    # get calculated scale
    normal_reading = ("%s%s" % (int((val - maxVal) * scale),"%"))
    # we can also get inverted value if needed
    inverted_reading = ("%s%s" % (int((minVal - val) * scale),"%"))
    # for this example we'll return only the normal reading
    return normal_reading

# set adc (analog to digital) on pin 35
adc = ADC(Pin(35))
# read analog input
adc.read()
# set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.atten(ADC.ATTN_11DB)
# get sensor value
value = adc.read()
# print the analog results (moisture)
print("sensor value: %s" % value)
print("sensor value in percentage: %s" % value_in_percentage(value))
