import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,  GPIO.OUT)
GPIO.setup(5,  GPIO.OUT)
GPIO.setup(7,  GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state35 = GPIO.input(35)
    input_state36 = GPIO.input(36)
    input_state37 = GPIO.input(37)
    input_state38 = GPIO.input(38)
    input_state40 = GPIO.input(40)
    if input_state35 == False:
        p = GPIO.PWM(3, 50)
        p.start(0)
        p.ChangeDutyCycle(12)
        sleep(1)
        p.stop()
    if input_state36 == False:
        p = GPIO.PWM(5, 50)
        p.start(0)
        p.ChangeDutyCycle(12)
        sleep(1)
        p.stop()
    if input_state37 == False:
        p = GPIO.PWM(7, 50)
        p.start(0)
        p.ChangeDutyCycle(12)
        sleep(1)
        p.stop()
    if input_state38 == False:
        p = GPIO.PWM(11, 50)
        p.start(0)
        p.ChangeDutyCycle(12)
        sleep(1)
        p.stop()
    if input_state40 == False:
        p = GPIO.PWM(13, 50)
        p.start(0)
        p.ChangeDutyCycle(12)
        sleep(1)
        p.stop()
