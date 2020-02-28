from bottle import route, run, template, request
import time
import PiMotor
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

IP_ADDRESS = '10.50.6.109'

GPIO.setwarnings(False)

servoPIN1 = 7

GPIO.setup(servoPIN1, GPIO.OUT)
servoX = GPIO.PWM(servoPIN1, 50)
servoX.start(7.3)

servoPIN2 = 12

GPIO.setup(servoPIN2, GPIO.OUT)
servoY = GPIO.PWM(servoPIN2, 50)
servoY.start(7.5)

m1 = PiMotor.Motor("MOTOR1", 1)
m2 = PiMotor.Motor("MOTOR2", 1)
m3 = PiMotor.Motor("MOTOR3", 1)
m4 = PiMotor.Motor("MOTOR4", 1)

mLeft = PiMotor.LinkedMotors(m1, m2)
mRight = PiMotor.LinkedMotors(m3, m4)

mAll = PiMotor.LinkedMotors(m1, m2, m3, m4)

ab = PiMotor.Arrow(3)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(1)
ar = PiMotor.Arrow(4)

sensor =  PiMotor.Sensor("ULTRASONIC", 40)

def move_forward():
    mAll.forward(50)
    af.on()

def forward_stop():
    mAll.stop()
    af.off()

def move_reverse():
    mAll.reverse(100)
    ab.on()

def reverse_stop():
    mAll.stop()
    ab.off()

@route('/')
def index():
    cmd = request.GET.get('command', '')
    if cmd == 'f':
        mAll.stop()
        move_forward()
    elif cmd == 'l':
        mAll.stop()
        mLeft.forward(50)
        mRight.reverse(50)
        time.sleep(0.5)
        mAll.stop()
    elif cmd == 's':
        mAll.stop()
    elif cmd == 'r':
        mAll.stop()
        mRight.forward(50)
        mLeft.reverse(50)
        time.sleep(0.5)
        mAll.stop()
    elif cmd == 'b':
        mAll.stop()
        mAll.reverse(30)
    return template('index.html')

try:
    run(host=IP_ADDRESS, port=2000)

finally:
    mAll.stop()
    GPIO.cleanup()
