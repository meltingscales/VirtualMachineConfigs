#!/usr/bin/env bash
#
# See http://publiclibrariesonline.org/2015/05/building-small-cheap-dedicated-catalog-stations-do-it-yourself-rasberry-pi-opacs/

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root. Try 'sudo $0'."
   exit 1
fi

# Directory holding the OPAC config
CONFIG_DIR=/data/opac-config-dir/

# dont edit
OPAC_COPIED_FLAG=/home/pi/COPIED_OPAC_FILES

if [[ ! -d $CONFIG_DIR ]]; then
   echo "Missing directory $CONFIG_DIR"
   exit 1
fi

echo "Updating software via apt-get..."
apt-get update
# apt-get upgrade -y

apt-get install -y gedit htop lynx fish dos2unix

which chromium
# if exit code is nonzero, chromium is not a command.
if [ "$?" -eq "1" ]; then
   echo "Installing 'Chromium', an open-source Google Chrome-like browser."
   apt-get install -y chromium
else
   echo "Already have Chromium installed."
fi

echo "Installing 'unclutter' to hide cursor when not active..."
apt-get install -y unclutter

echo "Installing 'privoxy' to prevent people from accessing certain sites."
apt-get install -y privoxy

if [[ ! -f $OPAC_COPIED_FLAG ]]; then
   echo "We have not copied the OPAC setup files from $CONFIG_DIR"
   rsync -avz $CONFIG_DIR / #--dry-run --verbose
   echo "We have copied OPAC files." > $OPAC_COPIED_FLAG
   echo "You should reboot to see changes!"
   echo "Also -- before that...Change the password for the 'pi' user!"
else
   echo "Already copied OPAC setup files from $CONFIG_DIR".
fi

echo "Done!"