"""
MicroPython MQTT Eduponics APP Client
https://github.com/STEMinds/micropython-eduponics
MIT License
Copyright (c) 2023 STEMinds

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

from Eduponics import umqttsimple,bh1750,bme280
import machine
import time
import json

# set adc (analog to digital) on pin 35
adc = machine.ADC(machine.Pin(35))
# set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.atten(machine.ADC.ATTN_11DB)

# Configure light sensor
light_sensor = bh1750.BH1750()

# Configure BME280
# setup I2C connection
i2c = machine.SoftI2C(scl=machine.Pin(15), sda=machine.Pin(4))
# Initialize BME280 object with default address 0x76
bme_sensor = bme280.BME280(i2c=i2c)
# initialize dht object, DHT11 coonected to IO19
#d = dht.DHT11(machine.Pin(19))

# define water level sensor as INPUT on IO pin number 21
water_level = machine.Pin(21, machine.Pin.IN)

# define pump on pin IO23 as OUTPUT, define pump state
pump = machine.Pin(23, machine.Pin.OUT)
pump_state = False

# MQTT Unique ID
UUID = "YOUR_UUID_GENERATED_ID"
# MQTT Topics
topics = ["plants/soil","plants/environment","plants/water"]

def handle_water_level(pin):
    global pump_state
    # water level triggered, turn off the pump
    # wait for 0.3 seconds to make sure it's just a little below the water sensor
    # else the pump might become unstable
    time.sleep(0.3)
    pump.value(0)
    pump_state = False

def get_soil_moisture():

    # sensor min and max values
    # can be changed and callibrated
    minVal = 710
    maxVal = 4095

    # read soil moisture sensor data
    val = adc.read()

    # scale the value based on maxVal and minVal
    scale = 100 / (minVal - maxVal)
    # get calculated scale
    normal_reading = ("%s%s" % (int((val - maxVal) * scale),"%"))
    # we can also get inverted value if needed
    inverted_reading = ("%s%s" % (int((minVal - val) * scale),"%"))
    # for this example we'll return only the normal reading
    # put everything in a JSON format suitable for the eduponics app
    plant = {
        "id":0,
        "name":"Plant A",
        "enabled":1,
        "moisture":normal_reading
    }
    # return the data
    return str(plant).replace("'",'"')

def get_environmental_data():

    # get light from the light sensor
    lux = int(light_sensor.readLight())
    # get bme280 sensor data
    bme280_values = bme_sensor.values
    temperature = bme280_values[0].replace("C","")
    pressure = bme280_values[1]
    humidity = bme280_values[2].replace("%","")
    # get DHT11 sensor data
    # measure sensor data
    #d.measure()
    # get temperature and humidity
    #temperature = d.temperature()
    #humidity = d.humidity()
    # get water quantity
    water_quantity = water_level.value()

    # put all this data into a JSON object
    data = {
        "temp":temperature,
        "humidity":humidity,
        "sunlight":lux,
        "water_quantity":water_quantity
    }

    return str(data).replace("'",'"')

def water_plant():
    global pump_state
    if(pump_state or water_level.value() == 1):
        # turn off the pump
        pump.value(0)
        pump_state = False
    else:
        # turn on the pump
        pump.value(1)
        pump_state = True
    return True

def on_message_callback(topic, msg):
    '''
    this is a callback, will be called when the app asks for certain information
    such as to water the plants when the watering button pressed
    '''
    # convert topic and message byte to string
    topic = str(topic, 'utf-8')
    msg = json.loads(str(msg, 'utf-8'))

    if(topic == "%s/plants/soil" % UUID or topic == "%s/plants/environment" % UUID):
        # Do nothing, we only publish to those topics
        pass
    elif(topic == "%s/plants/water" % UUID):
        # when the app request for plant watering it goes here
        if("key" in msg and "status" in msg):
            # valid request, let's process it
            if(msg["status"] == "pending"):
                # it's waiting for us to water it, let's water it
                water_plant()
                # after watering, publish success message of watering
                response = {"key":msg["key"],"status":"ok"}
                client.publish("%s/plants/water" % UUID, str(response).replace("'",'"'))
    else:
        print((topic, msg))

def connect_and_subscribe():

    print("[-] Connecting to MQTT client ...")
    # set the MQTT broker object
    client = umqttsimple.MQTTClient()
    # set a callback for incoming messages (subscribed topics)
    client.set_callback(on_message_callback)
    # connect to the broker
    client.connect()

    # subscribe to the topics
    for topic in topics:
        client.subscribe("%s/%s" % (UUID,topic))
        print("[-] Subscribed to %s successfully" % topic)
        print("[-] Connected to %s MQTT broker successfully" % client.server)

    return client

def restart_and_reconnect():
    # something  went wrong, reconnect in 5 seconds ...
    print('[-] Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()

# configure few variables
last_message = 0
message_interval = 5
# set callback on the water level sensor, if no water stop the pump
water_level.irq(trigger=machine.Pin.IRQ_RISING, handler=handle_water_level)

while True:
    try:
        # check if there are new messages pending to be processed
        # if there are, redirect them to callback on_message_callback()
        client.check_msg()

        # check if the last published data wasn't less than message_interval
        if (time.time() - last_message) > message_interval:
            # get soil moisture
            soil_moisture = get_soil_moisture()
            # publish soil moisture data
            client.publish("%s/plants/soil" % UUID, soil_moisture)
            #print("[-] published soil moisture")

            # update environmetal data
            env = get_environmental_data()
            client.publish("%s/plants/environment" % UUID, env)
            #print("[-] published evironmental data")

            # update last message timestamp
            last_message = time.time()

    except OSError as e:
        # if something goes wrong, reconnct to MQTT server
        restart_and_reconnect()
