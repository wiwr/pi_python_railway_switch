from time import sleep
from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

def led_pin(pin_on, pin_off):
    GPIO.output(pin_on, GPIO.HIGH)
    GPIO.output(pin_off, GPIO.LOW)

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

    #return new_direction

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/switch/<servo>/<direction>')
def left(servo, direction):
    print(servo)
    print(direction)
    if servo == "1":
        move_servo(s1, direction, s1_z, s1_c)
    elif servo == "2":
        move_servo(s2, direction, s2_z, s2_c)
    elif servo == "3":
        move_servo(s3, direction, s3_z, s3_c)
    elif servo == "4":
        move_servo(s4, direction, s4_z, s4_c)
    elif servo == "5":
        move_servo(s5, direction, s5_z, s5_c)
    return render_template('index.html') 

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
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

s1.start(0)
s2.start(0)
s3.start(0)
s4.start(0)
s5.start(0)

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

led_pin(s1_c, s1_z)
led_pin(s2_c, s2_z)
led_pin(s3_c, s3_z)
led_pin(s4_c, s4_z)
led_pin(s5_c, s5_z)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
