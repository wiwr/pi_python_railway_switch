import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(13,GPIO.OUT)
p = GPIO.PWM(13, 50)
p.start(0)
p.ChangeDutyCycle(12)
sleep(1)
GPIO.cleanup()
