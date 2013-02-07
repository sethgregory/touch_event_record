#!/usr/bin/env python

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
import getopt


def main(argv):

  # This value may vary between devices.  Run an adb shell getevent and look at
  # the list of event types.  Set this variable to the appropriate one (e.g.,
  # mine looks like this:
  #         add device 6: /dev/input/event1
  #           name:     "Melfas MMSxxx Touchscreen"
  event = 'event1'
  
  # Keep a count of how many captured events we collect, just for fun.
  count = 0

  # No file output by default
  outputfile = ''


  # Get and parse commandline args/options  
  try:
    opts, args = getopt.getopt(argv,"he:o:",["event=", "output="])
  except getopt.GetoptError:
    print 'touch_event_record.py [-d <eventnum>] [-o <outputfile>]'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'touch_event_record.py [-d <eventnum>] [-o <outputfile>]'
      sys.exit()
    elif opt in ("-e", "--event"):
      event = arg
    elif opt in ("-o", "--output"):
      outputfile = arg
      file = open(outputfile, 'w')

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
          if outputfile != '':
            file.write(output + '\n')
          count = count + 1
        buff = ''
        
  # Catch KeyboardInterrupt exception on CTRL+C
  except KeyboardInterrupt:
    sys.stdout.flush()

    if outputfile != '':
      file.close()

    pass
    print '\nExiting.  ' + str(count) + ' commands captured.'

if __name__ == "__main__":
  main(sys.argv[1:])