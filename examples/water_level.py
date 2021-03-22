import machine

# define water level sensor as INPUT on IO pin number 21
water_level = machine.Pin(21, machine.Pin.IN)

# this function will return 0 if container have no water and 1 if it has water
def is_empty():
    return water_level.value()

# check if the water container is empty is not
if(is_empty()):
    print("The water container is empty")
else:
    print("The water container is full")
