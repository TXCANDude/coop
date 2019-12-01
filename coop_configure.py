import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(25, GPIO.IN)
GPIO.output(14, GPIO.HIGH)


