from Eduponics import mcp23017,ads1x15
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

# setup adc for the extension board (default address for MCP might be 0x20)
ads_address = 0x48
mcp_address = 0x27
gain = 1

# the only change needed is add the var "chip" with the value "PCA9535"
adc = ads1x15.ADS1115(i2c=i2c, address=ads_address,mcp_address=mcp_address, gain=gain, chip="PCA9535")

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

# get voltage
for i in range(0,4):
    adc_read = adc.read(i)
    # get sensor value
    voltage = adc_read["voltage"]
    value = adc_read["raw"]
    # print the analog results (moisture)
    print("sensor value: %s" % value)
    print("sensor value in percentage: %s" % value_in_percentage(value))
    time.sleep(1)

