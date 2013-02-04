touch_event_record
==================

A simple script that accepts input via stdin (piped from adb shell getevent)
and does the appropriate conversions, printing out the corresponding
adb shell sendevent commands to replay your touch actions.

Requires the Android Dev Bridge (adb) utility to be installed.

Usage: adb shell getevent | touch_event_record.py
