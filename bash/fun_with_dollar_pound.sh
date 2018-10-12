#!/bin/bash

if [ "$#" -eq "0" ]; then
	echo "Try running me with arguments."
	echo "Example: '$0 you smell bad'."
fi

echo "You passed me $# arguments!"
