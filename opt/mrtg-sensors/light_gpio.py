#!/usr/bin/env python

import RPi.GPIO as GPIO, time, os
import numpy as np

PIN = 23
UPTIME = os.popen("uptime | awk -F, '{print $1}' | awk -Fup '{print $2}'").read().strip()
TEXT="Light"
MAX=100000

GPIO.setmode(GPIO.BCM)
 
def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)
 
        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
		if reading >= MAX:
		    break

        return reading

def f_avg(times, f, *args):
        results = [f(*args) for _ in range(times)]
        return results

# http://people.ee.ethz.ch/~oetiker/webtools/mrtg/reference.html
# "The external command must return 4 lines of output:
# Line 1
# current state of the first variable, normally 'incoming bytes count'
# Line 2
# current state of the second variable, normally 'outgoing bytes count'
# Line 3
# string (in any human readable format), telling the uptime of the target.
# Line 4
# string, telling the name of the target. "

print MAX - int(np.mean(f_avg(5, RCtime, PIN)))
print 0
print UPTIME
print TEXT
