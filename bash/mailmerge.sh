#!/bin/bash

# Credit for this script goes to Peter. Thanks!

NAMES_FILE="names.txt"
INPUT_FILE="template.txt"
OUTPUT_FILE="letter"
MARKER="NAME"

IFS=$'\n' # Separator is newline
set -f # Disable globbing

for i in $(cat < "$NAMES_FILE"); do # Loop over every name in NAMES_FILE

	OUTFILENAME=$OUTPUT_FILE-$i.txt # i.e. letter-peter.txt

	# Replace all MARKER with the name, and output it to OUTFILENAME
	cat $INPUT_FILE | sed s/$MARKER/$i/g > $OUTFILENAME

	# echo to stdout
	cat $OUTFILENAME
done
