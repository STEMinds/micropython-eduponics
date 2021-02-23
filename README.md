# MicroPython-Eduponics

The official MicroPython Eduponics library for Eduponics Mini ESP32 dev board.

## How to install

First, connect the ESP32 board to the WiFi by creating boot.py file and writing the following:

```python
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'WIFI_NAME'
password = 'WIFI_PASSWORD'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connected to WiFi successfully, IP: %s' % station.ifconfig()[0])
```

Make sure to change WiFi ESSID and Password. Once the ESP32 is connected to the Wifi, run the following commands:

```python
import upip
upip.install("micropython-eduponics")
```

This will install the latest version of micropython-eduponics package through upip.

## License

MIT License

Copyright (c) 2014 Adafruit Industries,
              2016 Radomir Dopieralski (@deshipu),
              2016 Paul Cunnane 2016,
              2016 Peter Dahlebrg,
              2017 Robert Hammelrath (@robert-hh),
              2019 Mike Causer,
              2021 STEMinds (@STEMinds),

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
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
