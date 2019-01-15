#!/usr/bin/env bash

# Update ya package lists
apt update

# Install Python 3 and Pip.
apt-get install -y python3 python3-pip

# Install flask.
python3 -m pip install flask  #TODO manage deps using pipfile instead of baked-in shell script
