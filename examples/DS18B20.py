from machine import Pin, I2C
import onewire, ds18x20, time
from eduponics import mcp23017

# IO12 reserved for powering the board, define it
power = Pin(12, Pin.OUT)
# activate the board
power.value(1)

# make sure the board have enough time to wakeup
time.sleep(0.1)

# setup I2C
i2c = I2C(scl=Pin(33), sda=Pin(32))

# define MCP with MOSFET pins
mcp = mcp23017.MCP23017(i2c, 0x20)

# define MCP DS18B20 as input
mcp.pin(0, mode=1)

# get input from pin
ds_pin = mcp[0].input()
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    print(rom)
    print(ds_sensor.read_temp(rom))
  time.sleep(5)
