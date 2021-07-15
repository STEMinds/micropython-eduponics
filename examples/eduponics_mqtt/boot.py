"""
MicroPython MQTT Eduponics APP Client
https://github.com/STEMinds/micropython-eduponics
MIT License
Copyright (c) 2020 STEMinds

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
import network
import esp
import time
esp.osdebug(None)
import gc
gc.collect()

# set WiFi credentials
ssid = ''
password = ''

# check if there is username and password for wifi
if(ssid != '' and password != ''):

    station = network.WLAN(network.STA_IF)

    station.active(True)
    station.connect(ssid, password)

    timeout_interval = 10

    # try to connect with timeout interval
    for i in range(0,timeout_interval):
        if(station.isconnected() == False):
            time.sleep(1)
            pass
        else:
            break;

    if(station.isconnected()):
        print('Connected to WiFi successfully, IP: %s' % station.ifconfig()[0])
    else:
        print("Something went wrong, connection timeout, try again!")
else:
    print("Please add WiFi credentials properly")
