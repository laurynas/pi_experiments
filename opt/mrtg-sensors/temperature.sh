#!/bin/bash

TEMP=$(awk -F'=' '/ t=/ { print $NF }' /sys/bus/w1/devices/28-0000054ca394/w1_slave)
UPTIME=$(uptime | awk -F, '{print $1}' | awk -Fup '{print $2}')
TEXT="Ambient Temperature"

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

echo ${TEMP}
echo 0
echo ${UPTIME}
echo ${TEXT}
