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
