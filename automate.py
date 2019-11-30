from gpiozero import LED,Motor
from picamera import PiCamera
from time import sleep

lights = LED(14)
actuator = Motor(forward=17, backward=18)
#coopcam = PiCamera()

lights.on()
sleep(5)
lights.off()

actuator.forward()
sleep(3)
actuator.reverse()
sleep(3)
actuator.stop()

#coopcam.capture('/home/pi/chickens.jpg')
