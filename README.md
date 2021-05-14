[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=STEMinds_micropython-eduponics&metric=bugs)](https://sonarcloud.io/dashboard?id=STEMinds_micropython-eduponics)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=STEMinds_micropython-eduponics&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=STEMinds_micropython-eduponics)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=STEMinds_micropython-eduponics&metric=ncloc)](https://sonarcloud.io/dashboard?id=STEMinds_micropython-eduponics)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=STEMinds_micropython-eduponics&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=STEMinds_micropython-eduponics)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=STEMinds_micropython-eduponics&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=STEMinds_micropython-eduponics)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=STEMinds_micropython-eduponics&metric=security_rating)](https://sonarcloud.io/dashboard?id=STEMinds_micropython-eduponics)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=STEMinds_micropython-eduponics&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=STEMinds_micropython-eduponics)

# MicroPython-Eduponics

The official MicroPython Eduponics library for Eduponics Mini ESP32 dev board.

## What can this library do

This library allows you to control all the functionalities of the ESP32 Eduponics mini dev board from one place.
The classes that are currently supported are:

- umqttsimple.py - implementation of simple MQTT protocol for MicroPython.
- ads1x15.py - ADS1x15 precide Analog-to-digital chip (available on extension board).
- mcp23017.py - MCP23017 16-bit IO Expander (available on extension board).
- at24c02.py - AT24C02 EEPROM module.
- bh1750.py - BH1750 photodiode (light sensor).
- bme280.py - 3 in 1: temperature, humidity and barometric sensor.
- ds1307.py - DS1307 RTC module.
- pcf8574.py - PCF8574 8-bit IO Expander (available on valve extension board).
- tds.py - To control TDS sensor through extension board.

The ADS1x15 class is integrated with MCP23017 in order to control the on-board MOSFET's and allow super low power consumption.
When the program ask for data form the ADC the MOSFET will open allowing current to flow (which will activate the sensor) once probing is done, the MOSFET will be deactivated.

This approach also allows to control multiple sensors such as: pH, EC, TDS etc .. without conflict! also extending the sensors lifespan.

The MCP23017 class also contains code to control the valve which can be found on the Eduponics Mini extension board.

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

Examples are available in the examples/ directory.

## License

MIT License

Copyright (c) 2014 Adafruit Industries,
              2016 Radomir Dopieralski (@deshipu),
              2016 Paul Cunnane 2016,
              2016 Peter Dahlebrg,
              2017 Robert Hammelrath (@robert-hh),
              2019 Mike Causer (@mcauser),
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
