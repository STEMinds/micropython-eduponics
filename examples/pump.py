import machine
import time

# define pump on pin IO23 as OUTPUT
pump = machine.Pin(23, machine.Pin.OUT)
# define sleep interval as 3 seconds
sleep_interval = 1

# turn on the pump
pump.value(1)
# wait for the defined sleep interval
time.sleep(sleep_interval)
# turn off the pump
pump.value(0)
