import RPi.GPIO as GPIO
from time import sleep

def led_pin(pin):
    sleep_time = 2
    print(pin)
    GPIO.output(pin, GPIO.HIGH)
    sleep(sleep_time)
    GPIO.output(pin, GPIO.LOW)
    sleep(sleep_time)
    GPIO.output(pin, GPIO.HIGH)
    sleep(sleep_time)
#    GPIO.output(pin, GPIO.LOW)
#    sleep(1)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

led_pin(15)
led_pin(8)
led_pin(19)
led_pin(18)
led_pin(10)
led_pin(12)
led_pin(16)
led_pin(22)
led_pin(23)
led_pin(21)

GPIO.cleanup()
