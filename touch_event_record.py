#!/usr/local/bin/python

'''
A simple script that accepts input via stdin (piped from adb shell getevent)
and does the appropriate conversions, printing out the corresponding
adb shell sendevent commands to replay your touch actions.

@author:      Seth Gregory
@version:     1.0
@description: adb shell getevent/sendevent conversion utility
@usage:       adb shell getevent | touch_event_record.py
'''

import sys
import string

# This value may vary between devices.  Run an adb shell getevent and look at
# the list of event types.  Set this variable to the appropriate one (e.g.,
# mine looks like this:
#         add device 6: /dev/input/event1
#           name:     "Melfas MMSxxx Touchscreen"
event = 'event1'

# Keep a count of how many captured events we collect, just for fun.
count = 0

# Watch the buffer and convert any matching items
try:
  buff = ''
  while True:
    buff += sys.stdin.read(1)
    if buff.endswith('\n'):
      if(buff.startswith('/dev/input/' + event)):
        linelist = string.split(buff[:-1])
        linelist[0] = 'adb shell sendevent /dev/input/' + event
        linelist[1] = str(int(linelist[1], 16))
        linelist[2] = str(int(linelist[2], 16))
        linelist[3] = str(int(linelist[3], 16))
        output = ' '.join(linelist)
        print output
        count = count + 1
      buff = ''
      
# Catch KeyboardInterrupt exception on CTRL+C
except KeyboardInterrupt:
  sys.stdout.flush()
  pass
  print '\nExiting.  ' + str(count) + ' commands captured.'