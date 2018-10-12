#!/bin/bash

# Credit for this script goes to Peter. Thanks!

DISK_USAGE="$(df | grep '/dev/sda1' | awk '{print $5}' | tr -d '%')"

THRESHHOLD=10

echo "$DISK_USAGE% of disk used."

if [ "$DISK_USAGE" -gt "$THRESHHOLD" ]; then
	echo "Over $THRESHHOLD% disk used. Delete your files, please!"
else
	echo "Under $THRESHHOLD% disk used. Good job not downloading crap!"
fi
