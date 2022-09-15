from Eduponics import pca9535
from machine import I2C, Pin
import time

# IO12 reserved for powering the board, define it
power = Pin(12, Pin.OUT)
# activate the board
power.value(1)

# make sure to wait enough time for the board to wakeup
time.sleep(0.1)

# define i2c connection to the extension board
i2c = I2C(scl=Pin(33), sda=Pin(32))

# initialize relay object (default address might be 0x20)
relays = pca9535.Relays(i2c, address=0x27)

# open relays one by one
for i in range(0,4):
    relays.open(i)
    time.sleep(1)

# close all relays one by one
for i in range(0,4):
    relays.close(i)
    time.sleep(1)

# open all relays
relays.open_all()

time.sleep(3)

# close all relays
relays.close_all()
