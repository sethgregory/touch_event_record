touch_event_record
==================

A simple script that accepts input via stdin (piped from adb shell getevent)
and does the appropriate conversions, printing out the corresponding
adb shell sendevent commands to replay your touch actions.

After completing your input, you can copy the output into a shell script
(or, optionally, use the commandline argument to specify an output file)
and add sleep statements as needed to introduce delays between touch
events in playback.  (A later version may automatically create these, but
for now you're on your own ;))

** NOTE: Requires the Android Debug Bridge (adb) utility to be installed.

Usage: adb shell getevent | touch_event_record.py

    The following options are available:

    -h    Print usage summary

    -o    Specify an output file (e.g., -o outfile.txt)

    -e    Specify the appropriate event name for your device's touchscreen,
          (e.g., -e event1) - you can find this by running adb shell getevent
          and reading the top of the output.

