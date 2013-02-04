touch_event_record
==================

A simple script that accepts input via stdin (piped from adb shell getevent)
and does the appropriate conversions, printing out the corresponding
adb shell sendevent commands to replay your touch actions.

@author:      Seth Gregory
@version:     1.0
@description: adb shell getevent/sendevent conversion utility
@usage:       adb shell getevent | touch_event_record.py
