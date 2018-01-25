import RPi.GPIO as GPIO
import time
import lcddriver
import touch
import ds18b20 as tem

def hello():
    display = lcddriver.lcd()
    #display = lcddriver.lcd()
    #GPIO.setmode(GPIO.BCM)

    TRIG = 19 
    ECHO = 16

    # print "Distance Measurement In Progress"

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    # print "Waiting For Sensor To Settle"
    #time.sleep(0.000001)

    GPIO.output(TRIG, True)
    time.sleep(0.1)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start


    distance = pulse_duration * 17150

    distance = round(distance, 2)
    #time.sleep(0.001)
    display.lcd_display_string(str(distance),1)
#    display.lcd_display_string("cm",2)
    a = tem .far()
    display.lcd_display_string(str(a),2)
    time.sleep(0.2)
    
    GPIO.cleanup()
