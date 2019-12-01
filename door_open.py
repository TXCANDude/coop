from gpiozero import Motor, Button
from time import sleep

doorstatus = Button(25)
actuator = Motor(forward=17, backward=18)

if doorstatus.is_pressed:
    actuator.forward()
    sleep(3)
    actuator.stop()



