import machine, neopixel
import time

# Configure the RGB LED at IO pin 14 (1 indicates 1 LED)
np = neopixel.NeoPixel(machine.Pin(14), 1)

np[0] = (255, 0, 0) # set to red, full brightness
np.write() # save changes
time.sleep(1)
np[0] = (0, 255, 0) # set to green, full brightness
np.write() # save changes
time.sleep(1)
np[0] = (0, 0, 255) # set to blue, full brightness
np.write() # save changes
time.sleep(1)
np[0] = (0, 0, 0) # empty the LED colors (wipe)
np.write() # save changes
