import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
p = GPIO.PWM(7, 50)
p.start(0)
p.ChangeDutyCycle(12)
sleep(1)
GPIO.cleanup()
