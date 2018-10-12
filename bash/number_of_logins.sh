#!/bin/bash

# Credit for this script goes to Peter. Thanks!

USERNAME=$1 # The first argument from the command line.

if [ "$#" -ne "1" ]; then # They didn't pass in any arguments.
	USERNAME=`whoami` # Get the current user, since we don't have any arguments.
	echo "No user supplied. Using '$USERNAME' instead."
fi

echo "Showing times that $USERNAME has logged in."

last | grep "$1" | wc -l
