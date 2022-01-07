from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
# prints the tello battery percentage
print(me.get_battery())

# takeoff() functions takes off
# land() function lands the drone
me.takeoff()
me.send_rc_control(0, 50, 0, 0)
sleep(1)
me.send_rc_control(0,-50, 0, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
me.land()