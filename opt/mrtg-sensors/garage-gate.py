#!/usr/bin/env python

import RPi.GPIO as GPIO, os

PIN = 23
UPTIME = os.popen("uptime | awk -F, '{print $1}' | awk -Fup '{print $2}'").read().strip()
TEXT="Garage Gate"

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)
 
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

print GPIO.input(PIN) + 1
print 0
print UPTIME
print TEXT
