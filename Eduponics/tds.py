#!/usr/bin/python

'''
Copyright (c) 2020 STEMinds
Website: https://steminds.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of self software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and self permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import time
from Eduponics import ads1x15
from ulab import *
from machine import I2C, Pin
import time

class TDS():

    def __init__(self,channel=0,temperature=25,i2c=None,mcp_address=None,ads_address=None):
        self.channel = channel
        self.kvalue = 1.0
        self.temperature = temperature
        self.values_buffer = [] # empty list of values for median average
        self.scount = 30 # how many times to take samples to make median average
        self.vref = 4.096 # analog reference voltage(Volt) of the ADC, based on ADS chip gain 1
        # Open i2c bus
        self.ads_address = 0x49
        self.mcp_address = 0x20
        self.gain = 1
        self.adc = ads1x15.ADS1115(i2c, ads_address=self.ads_address, mcp_address=self.mcp_address, self.gain)

    def overwrite_buffer(self, item):
        self.values_buffer.insert(0, item)
        self.values_buffer = self.values_buffer[:self.scount]

    def set_temperature(self,temp):
        self.temperature = temp

    def reset_buffer(self):
        self.values_buffer = []

    def ReadChannel(self):
        # read data from i2c ADC
        adc_read = self.adc.read(self.channel)
        voltage = adc_read["voltage"]
        raw_data = adc_read["raw"]
        return raw_data

    def read(self):
        # Read values from ADC then run median filter for accurate results
        value1 = self.ReadChannel()
        value2 = self.ReadChannel()
        # make sure the value is not 0
        if value1 or value2 != 0:
            # append the value for the values buffer list for median average
            buffer = [value1,value2]
            self.overwrite_buffer(buffer)
            # turn the list into numpy array
            double_buffer = numpy.array(self.values_buffer)
            # run median_filter on the numpy array
            median_voltage = self.median_filter(double_buffer) * self.vref / 1024.0;
            # calculate voltage based on temperature compensation
            compensation_coefficient = 1.0 + 0.02 * (self.temperature - 25.0);
            compensation_volatge = median_voltage / compensation_coefficient
            # calculate final tds value in ppm
            tds_value = int((133.42 * compensation_volatge * compensation_volatge * compensation_volatge - 255.86 * compensation_volatge * compensation_volatge + 857.39 * compensation_volatge) * 0.5)
            return tds_value
        else:
            return 0

    def median_filter(self, data):
        return numpy.mean(data)
