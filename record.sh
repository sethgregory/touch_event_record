#!/bin/sh
echo "Ready to record.  Outputting to replay.sh\n[use ctrl+c to exit]\n"
adb shell getevent | tee replay.sh | ./touch_event_record.py
