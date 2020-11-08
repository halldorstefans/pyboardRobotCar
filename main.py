from pyb import Pin, Timer
import utime

counter = 0

p1 = Pin('X1') # X1 has TIM2, CH1
p3 = Pin('X3') # X3 has TIM2, CH3

tim2 = Timer(2, freq=1000)

ch1 = tim2.channel(1, Timer.PWM, pin=p1)
ch3 = tim2.channel(3, Timer.PWM, pin=p3)

while counter < 10:
    ch1.pulse_width_percent(50)
    ch3.pulse_width_percent(50)

    utime.sleep_ms(1000)

    ch1.pulse_width_percent(10)
    ch3.pulse_width_percent(50)

    utime.sleep_ms(500)

    counter += 1

ch1.pulse_width_percent(0)
ch3.pulse_width_percent(0)
