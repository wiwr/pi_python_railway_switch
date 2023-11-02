from time import sleep
from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

servo_pins = [29 ,31 ,33 ,35 ,36 ,38 ,37 ,40]

def move_servo(servo_id, angle):
    duty_cycle = 2.5 + 10 * angle / 180
    servos[servo_id].ChangeDutyCycle(duty_cycle)

@app.route("/")
def index():
    print('index')
    return render_template('index.html')

@app.route("/control", methods=['GET'])
def control_servo():
    print('control')
    direction = request.args.get('direction') 
    servo_id = int(request.args.get('servo_id'))
    print(direction)
    print(servo_id)
    if direction == 'left':
        move_servo(servo_id, 0) 
    elif direction == 'right':
        move_servo(servo_id, 180) 
    return 'OK'

GPIO.setmode(GPIO.BOARD)

for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)

servos = [GPIO.PWM(pin, 50) for pin in servo_pins]

for servo in servos:
    servo.start(0)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
