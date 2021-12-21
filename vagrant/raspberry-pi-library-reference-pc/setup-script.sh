#!/usr/bin/env bash
#
# See http://publiclibrariesonline.org/2015/05/building-small-cheap-dedicated-catalog-stations-do-it-yourself-rasberry-pi-opacs/

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root. Try 'sudo $0'."
   exit 1
fi

# Directory holding
CONFIG_DIR=/data/opac-config-dir/

if [[ ! -d $CONFIG_DIR ]]; then
   echo "Missing directory $CONFIG_DIR"
   exit 1
fi

echo "Updating software via apt-get..."
apt-get update
# apt-get upgrade -y

apt-get install -y gedit htop lynx fish

which chromium
# if exit code is nonzero, chromium is not a command.
if [ "$?" -eq "1" ]; then
   echo "Installing 'Chromium', an open-source Google Chrome-like browser."
   apt-get install -y chromium
fi

echo "Installing 'unclutter' to hide cursor when not active..."
apt-get install -y unclutter

echo "Installing 'privoxy' to prevent people from accessing certain sites."
apt-get install -y privoxy

if [[ ! -f /home/pi/COPIED_OPAC_FILES ]]; then
   echo "We have not copied the OPAC setup files from $CONFIG_DIR"
   rsync -avz $CONFIG_DIR / #--dry-run --verbose
   touch /home/pi/COPIED_OPAC_FILES
   echo "You should reboot to see changes!"
else
   echo "Already copied OPAC setup files from $CONFIG_DIR".
fi

echo "Done!"