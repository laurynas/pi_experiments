#!/bin/bash

CPU1TEMP=$(cat /sys/class/thermal/thermal_zone0/temp)
UPTIME=$(uptime | awk -F, '{print $1}' | awk -Fup '{print $2}')
TEXT="CPU Temperature"

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

echo ${CPU1TEMP}
echo ${CPU1TEMP}
echo ${UPTIME}
echo ${TEXT}
