#!/usr/bin/env python
#----------------------------------------------------------------
#	Note:
#		ds18b20's data pin must be connected to pin7.
#		replace the 28-XXXXXXXXX as yours.
#----------------------------------------------------------------
import os
import time
ds18b20 = ''

def setup():
	global ds18b20
	for i in os.listdir('/sys/bus/w1/devices'):
		if i != 'w1_bus_master1':
			ds18b20 = i

def read():
	#global ds18b20
	location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
	tfile = open(location)
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	global temperature
        temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
       
        return temperature
def far():
        #global 
        temperatureF = temperature * 9/5
        temperatureF +=32
        
        return temperatureF
	
def loop():
	while True:
		if read() != None:
		    	#os.system('clear')
                        print "\rCurrent temperature :%0.3f C" % read()
                        print "\r                    :%0.3f F" %  far()
                        
                       #time.sleep(.1)
                        

def destroy():
	pass

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()

