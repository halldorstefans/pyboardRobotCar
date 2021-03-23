# main.py -- put your code here!
from pyb import Pin, Timer, ADC

p1 = Pin('X1') # X1 is rightMotor
p3 = Pin('X3') # X3 is leftMotor

tim = Timer(2, freq=1000)

rightMotor = tim.channel(1, Timer.PWM, pin=p1)
leftMotor = tim.channel(3, Timer.PWM, pin=p3)

rightLineSensor = ADC(Pin('X5'))
leftLineSensor = ADC(Pin('X6'))

rightMotor.pulse_width_percent(0)
leftMotor.pulse_width_percent(0)

while (True):
    rightDetect = rightLineSensor.read()
    leftDetect = leftLineSensor.read()

    if (leftDetect > 1000 and rightDetect > 1000):
        rightMotor.pulse_width_percent(50)
        leftMotor.pulse_width_percent(50)

    if (leftDetect > 1000 and rightDetect < 1000):
        rightMotor.pulse_width_percent(10)

    if (leftDetect < 1000 and rightDetect > 1000):
        leftMotor.pulse_width_percent(10)

    if (leftDetect < 1000 and rightDetect < 1000):
        rightMotor.pulse_width_percent(0)
        leftMotor.pulse_width_percent(0)
