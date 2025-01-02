#!/usr/bin/env python
import config
import adafruit_max31855
import digitalio
import time
import datetime
import sys

try:
    import board
except NotImplementedError:
    print("not running a recognized blinka board, exiting...")
    import sys
    sys.exit()

########################################################################
#
# To test your gpio output to control a relay...
#
# Edit config.py and set the following in that file to match your
# hardware setup: gpio_heat, gpio_heat_invert
#
# then run this script...
# 
# ./test-output.py
#
# This will switch the output on for five seconds and then off for five 
# seconds. Measure the voltage between the output and any ground pin.
# You can also run ./gpioreadall.py in another window to see the voltage
# on your configured pin change.
########################################################################

if not (hasattr(config,'gpio_failsafe')):
    print("failsafe relay not configured, exiting...")
    sys.exit()

failsafe_relay = digitalio.DigitalInOut(config.gpio_failsafe)
failsafe_relay.direction = digitalio.Direction.OUTPUT
on = True
off = False

print("\nboard: %s" % (board.board_id))
print("failsafe relay configured as config.gpio_failsafe  = %s BCM pin\n" % (config.gpio_failsafe))

while True:
    failsafe_relay.value = on
    print("%s failsafe on" % datetime.datetime.now())
    time.sleep(5)
    failsafe_relay.value = off
    print("%s failsafe off" % datetime.datetime.now())
    time.sleep(5)
