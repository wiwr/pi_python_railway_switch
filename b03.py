#Import libraries
import RPi.GPIO as GPIO
from time import sleep

def move_servo(servo, direction, pin_z, pin_c):
    move_time = 0.25
    if direction == "left":
        move = 2.5
        new_direction = "right"
        led_pin(pin_z, pin_c)
    elif direction == "right":
        move = 11.5
        new_direction = "left"
        led_pin(pin_c, pin_z)
    else:
        move = 0
        new_direction = "right"
        led_pin(pin_z, pin_c)

    servo.ChangeDutyCycle(move)
    sleep(move_time)
    servo.ChangeDutyCycle(0)
    
    return new_direction

def led_pin(pin_on, pin_off):
    GPIO.output(pin_on, GPIO.HIGH)
    GPIO.output(pin_off, GPIO.LOW)

#Switch off warnings
#GPIO.setwarnings(False)

#Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

#Config servo and set to variable
#50 is
GPIO.setup(3,  GPIO.OUT)
GPIO.setup(5,  GPIO.OUT)
GPIO.setup(7,  GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
s1 = GPIO.PWM(3, 50)
s2 = GPIO.PWM(5, 50)
s3 = GPIO.PWM(7, 50)
s4 = GPIO.PWM(11, 50)
s5 = GPIO.PWM(13, 50)
s1_direction = "left"
s2_direction = "left"
s3_direction = "left"
s4_direction = "left"
s5_direction = "left"

s1_z = 19
s1_c = 15
s2_z = 22
s2_c = 18
s3_z = 16
s3_c = 21
s4_z = 10
s4_c = 12
s5_z = 23
s5_c = 8

GPIO.setup(s1_z, GPIO.OUT)
GPIO.setup(s1_c, GPIO.OUT)
GPIO.setup(s2_z, GPIO.OUT)
GPIO.setup(s2_c, GPIO.OUT)
GPIO.setup(s3_z, GPIO.OUT)
GPIO.setup(s3_c, GPIO.OUT)
GPIO.setup(s4_z, GPIO.OUT)
GPIO.setup(s4_c, GPIO.OUT)
GPIO.setup(s5_z, GPIO.OUT)
GPIO.setup(s5_c, GPIO.OUT)

GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_pin(s1_c, s1_z)
led_pin(s2_c, s2_z)
led_pin(s3_c, s3_z)
led_pin(s4_c, s4_z)
led_pin(s5_c, s5_z)

s1.start(0)
s2.start(0)
s3.start(0)
s4.start(0)
s5.start(0)

try:
    while True:
        input_state35 = GPIO.input(35)
        input_state36 = GPIO.input(36)
        input_state37 = GPIO.input(37)
        input_state38 = GPIO.input(38)
        input_state40 = GPIO.input(40)
        if input_state35 == False:
            print(35)
            s1_direction = move_servo(s1, s1_direction, s1_z, s1_c)
        if input_state36 == False:
            print(36)
            s2_direction = move_servo(s2, s2_direction, s2_z, s2_c)
        if input_state37 == False:
            print(37)
            s3_direction = move_servo(s3, s3_direction, s3_z, s3_c)
        if input_state38 == False:
            print(38)
            s4_direction = move_servo(s4, s4_direction, s4_z, s4_c)
        if input_state40 == False:
            print(40)
            s5_direction = move_servo(s5, s5_direction, s5_z, s5_c)
finally:
    s1.stop()
    s2.stop()
    s3.stop()
    s4.stop()
    s5.stop()
    GPIO.cleanup()
    print("Goodbye!")
