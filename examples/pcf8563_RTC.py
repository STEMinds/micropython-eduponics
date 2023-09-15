import utime
import time
import pcf8563
from machine import Pin
from machine import SoftI2C as I2C

def handle_interrupt(pin):
    if r.check_for_alarm_interrupt():
        print('is alarm clock interrupt')
    else:
        print('is not for alarm interrupt')
    r.clear_alarm()

#irq = Pin(37, mode=Pin.IN,handler=handle_interrupt,trigger=Pin.IRQ_FALLING)
i2c = I2C(scl=Pin(15), sda=Pin(4))
pcf = pcf8563.PCF8563(i2c)

print('[-] Current RTC time')
pcf.datetime()
time.sleep(1)

print('Clear alarm config register')
pcf.clear_alarm()

print('Setting current clock datetime')
pcf.write_all(50,30,15,3,17,9,49)

#print('Set the alarm to match for minutes')
#r.set_daily_alarm(minutes=31)

#print('Enable rtc chip interrupt')
#r.enable_alarm_interrupt()

while True:
    print(pcf.datetime())
    time.sleep(1)
