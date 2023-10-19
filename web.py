import time
import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)

s1 = GPIO.PWM(3, 50)

html = """<!DOCTYPE html>
<html>
    <head>
        <title>Railway Switch</title>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <center>
            <h1>Railway Switch</h1>
        </center>
        <form>
            <center>
                <button class="ButtonLeft" name="servo1" value="on" type="submit">On</button>
                <button class="ButtonRight" name="servo1" value="off" type="submit">Off</button>
            </center>
        </form>
    </body>
</html>
"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print("request:")
        print(request)
        request = str(request)
        servo1_on request.find('servo1=on')
        servo1_off request.find('servo1=off')

        print( 'servo on = ' + str(servo1_on))
        print( 'servo off = ' + str(servo1_off))

        if servo1_on == 8:
            print("servo1 on")
            servo1.ChangeDutyCycle(2.5)
        if servo1_off == 8:
            print("servo1 off")
            servo1.ChangeDutyCycle(0)

        response = html
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')

