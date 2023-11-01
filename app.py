from time import sleep
from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

servo_pins = [29 ,31 ,33 ,35 ,36 ,38 ,37 ,40]

def led_pin(pin_on, pin_off):
    GPIO.output(pin_on, GPIO.HIGH)
    GPIO.output(pin_off, GPIO.LOW)

def move_servo(servo, direction, pin_z, pin_c):
    move_time = 0.25
    if direction == "left":
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

for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)

servos = [GPIO.PWM(pin, 50) for pin in servo_pins]

for servo in servos:
    servo.start(0)

try:
    while True:
        angles = [2, 11, 6]
        for i in range(len(servos)):
            for j in range(len(angles)):
                duty_cycle = angles[j]
                servos[i].ChangeDutyCycle(duty_cycle)
                sleep(1)
except KeyboardInterrupt:
    for servo in servos:
        servo.stop()
    GPIO.cleanup()

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8080)
