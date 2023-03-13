"""
MicroPython QA file to test all the sensors on the Eduponics Mini
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
import machine
from machine import I2C,ADC,Pin
from eduponics import bme280,at24c02,ds1307,bh1750,pcf8563,qmp6988,sht30
import neopixel
import time
import esp32
import dht

# configure wakeup deep sleep functionality
wake_up = Pin(36, mode = Pin.IN)
# level parameter can be: esp32.WAKEUP_ANY_HIGH or esp32.WAKEUP_ALL_LOW
esp32.wake_on_ext0(pin = wake_up, level = esp32.WAKEUP_ANY_HIGH)

# configure neopixel
np = neopixel.NeoPixel(Pin(14), 1)

# define water level sensor as INPUT on IO pin number 21
water_level = Pin(21, Pin.IN)

# define pump on pin IO23 as OUTPUT
pump = Pin(23, Pin.OUT)

# initialize dht object, DHT11 coonected to IO19
#d = dht.DHT11(Pin(19))

# setup I2C connection
i2c = I2C(scl=Pin(15), sda=Pin(4))

def test_qmp6988():
    qmp = qmp6988.QMP6988(i2c)
    temp, pressure = qmp.measure()
    print("Temp/Pressure: {}°C/{}Pa".format(temp, pressure))

def test_sht30():
    sensor = sht30.SHT30(i2c=i2c)
    temperature, humidity = sensor.measure()
    print('Temperature:', temperature, 'ºC, RH:', humidity, '%')
    
def test_eeprom():
    input("[-] Testing EEPROM ... press enter when ready ...")
    print("")
    eeprom = at24c02.AT24C32N(i2c)
    print("[-] Reading 32 bytes ...")
    print(eeprom.read(0, 32))
    print("[-] Writing 11 bytes - 'Hello World' ...")
    eeprom.write(0, 'hello world')
    print("[-] Reading 11 bytes - 'Hello World' ...")
    print(eeprom.read(0, 11))
    # print space to make it pretty
    print("")

def test_dht11():
    input("[-] Testing DHT11 sensor 5 times ... press enter when ready ...")
    print("")
    # intialize counter
    counter = 0
    while counter != 4:
        # measure sensor data
        d.measure()
        # get temperature and humidity
        temperature = d.temperature()
        humidity = d.humidity()
        # wait a second
        time.sleep(1)
        # update counter
        counter = counter + 1
    # print space to make it pretty
    print("")

def test_pcf8563():
    # set pcf8563 object
    pcf = pcf8563.PCF8563(i2c)
    # print current time
    print("[-] Current RTC time: %s" % str(pcf.datetime()))
    time.sleep(1)
    # clear alarm
    print('[-] Clear alarm config register')
    pcf.clear_alarm()
    # set alarm - disabled for now
    #print('Set the alarm to match for minutes')
    #r.set_daily_alarm(minutes=31)
    #print('Enable rtc chip interrupt')
    #r.enable_alarm_interrupt()
    # write time
    print('[-] Setting current clock datetime')
    """Direct write un-none value.
    Range: seconds [0,59], minutes [0,59], hours [0,23],
    day [0,7], date [1-31], month [1-12], year [0-99].
    """
    pcf.write_all(0,0,21,5,15,9,22)
    # set counter
    counter = 0
    input("[-] Getting time 5 times, press enter when ready ...")
    while counter != 4:
        print(pcf.datetime())
        time.sleep(1)
        counter = counter + 1
    # print space to make it pretty
    print("")

def test_bh1750():
    # initialize sensor
    sensor = bh1750.BH1750()
    # initialize counter
    counter = 0
    input("[-] Testing BH1750 sensor 5 times, press enter when ready ...")
    print("")
    while counter != 4:
        # get light value
        value = sensor.readLight()
        print("[-] Light in the room: %slx" % value)
        # sleep one second
        time.sleep(1)
        # increase counter
        counter = counter + 1
    # print space to make it pretty
    print("")

def test_bme280():
    # Initialize BME280 object with default address 0x76
    sensor = bme280.BME280(i2c=i2c)
    # setup counter
    counter = 0
    input("[-] Reading BME280 values 5 times, press enter when ready ...")
    print("")
    while counter != 4:
        # get the values from the BME280 library
        values = sensor.values
        altitude = sensor.altitude
        dew_point = sensor.dew_point
        sea_level = sensor.sealevel
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
        time.sleep(1)
        counter = counter + 1
    # print space to make it pretty
    print("")

def test_pump():
    input("[-] Turn on/off the pump 3 times, press enter when ready ...")
    print("")
    counter = 0
    while counter != 3:
        # turn on the pump
        print("[-] Pump ON")
        pump.value(1)
        # wait one second
        time.sleep(1)
        # turn off the pump
        print("[-] Pump OFF")
        pump.value(0)
        # wait one second
        time.sleep(1)
        # update counter
        counter = counter + 1
    # print space to make it pretty
    print("")

def read_water_level():
    # set counter
    counter = 1
    # read water level values
    input("[-] Reading water sensor values 5 times, press enter when ready ...")
    print("")
    while counter != 5:
        # will return 0 if container have no water and 1 if it has water
        value = water_level.value()
        print("[-] Water level: %s" % value)
        time.sleep(1)
        # update counter
        counter = counter + 1
    # print space to make it pretty
    print("")

def test_rgb():
    input("[-] Testing RGB LED, press enter when ready ...")
    print("")
    print("[-] Setting RGB Red")
    np[0] = (255, 0, 0) # set to red, full brightness
    np.write() # save changes
    time.sleep(1)
    print("[-] Setting RGB Green")
    np[0] = (0, 175, 0) # set to green, half brightness
    np.write() # save changes
    time.sleep(1)
    print("[-] Setting RGB Blue")
    np[0] = (0, 0, 85) # set to blue, quarter brightness
    np.write() # save changes
    time.sleep(1)
    print("[-] Setting RGB OFF")
    np[0] = (0, 0, 0) # empty the LED colors (wipe)
    np.write() # save changes
    # print space to make it pretty
    print("")

def read_soil_moisture():
    # set adc (analog to digital) on pin 35
    adc = ADC(Pin(35))
    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
    adc.atten(ADC.ATTN_11DB)
    # set counter
    counter = 1
    # read soil moisture values
    input("[-] Reading soli moisture values 5 times, press enter when ready ...")
    print("")
    while counter != 5:
        # get sensor value
        value = adc.read()
        print("[-] Soil moisture: %s" % value)
        time.sleep(1)
        # update counter
        counter = counter + 1
    # print space to make it pretty
    print("")

def main():
    # test RGB
    test_rgb()
    # test soil moisture
    read_soil_moisture()
    # test pump
    test_pump()
    # test water level
    read_water_level()
    # test bme280
    #test_bme280()
    # test bh1750
    test_bh1750()
    # test qmp6988
    test_qmp6988()
    # test sht30
    test_sht30()
    # test pcf8563
    test_pcf8563()
    # test EEPROM
    test_eeprom()
    # test DHT11
    #test_dht11()
    # finally, go to deep sleep and test waking up
    print('[-] Going to sleep now .. wake me up to test.')
    machine.deepsleep()

# start the main program
main()
