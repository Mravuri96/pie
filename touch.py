#!/usr/bin/env python
import RPi.GPIO as GPIO
import ultrasonic2
import time
import ds18b20

TouchPin = 13
Gpin   = 27
Rpin   = 18

tmp = 0

def setup():
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
    # GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
    GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
    GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)

def Led(x):
    if x == 1:
        GPIO.output(Rpin, 0)
        GPIO.output(Gpin, 1)
    if x ==0:
        GPIO.output(Rpin, 1)
        GPIO.output(Gpin, 0)


def Print(x):
    global tmp
    if x != tmp:
        if x == 1:
                print '    **********'
                print '    *     ON *'
                print '    **********'
                #ultrasonic2.hello()
        if x == 0:
                print '    **********'
                print '    * OFF    *'
                print '    **********'
        return x
        tmp = x


def loop():
    while True:
            setup()
            a = GPIO.input(TouchPin)
            Led(a)
            activate = Print(a)
            if activate == 1:
                 ultrasonic2.hello()
                 GPIO.cleanup()

def destroy():
    GPIO.output(Gpin, GPIO.HIGH)       # Green led off
    GPIO.output(Rpin, GPIO.HIGH)       # Red led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
            loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
            destroy()


