#!/usr/bin/env bash
#
# See http://publiclibrariesonline.org/2015/05/building-small-cheap-dedicated-catalog-stations-do-it-yourself-rasberry-pi-opacs/

# Directory holding the OPAC config. Change this path, if using a USB drive or `git clone` to get the configuration files from GitHub.
CONFIG_DIR=/data/opac-config-dir/

# flag that indicates that config files have already been copied
OPAC_COPIED_FLAG=/home/pi/COPIED_OPAC_FILES

# edit below if you know what you're doing
DEBUG=0
DEBUG_EXTRA_COMMANDS=0

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root. Try 'sudo $0'."
   exit 1
fi

if [[ ! -d $CONFIG_DIR ]]; then
   echo "Missing directory $CONFIG_DIR"
   exit 1
fi

   # Debug halt, i.e. for tweaking base image
if [[ $DEBUG -ne 0 ]]; then
   echo "Halting in debug mode. See below 'exit 1' for debug packages/commands."

   if [[ $DEBUG_EXTRA_COMMANDS -ne 0 ]]; then
      echo "Running extra debug commands."

      apt-get install -y baobab gparted wajig
      apt-get install -y gedit htop lynx fish dos2unix pv

      wajig large
      
      # Fill up all blocks in virtual disk, to improve compression
      dd if=/dev/zero | pv | sudo dd of=/bigassfile
      sync
      sleep 1
      sync
      ls -lash /
      df -h
      rm -f /bigassfile

      # After this, you can shrink the disk or `dd` to a new, smaller disk -- use gparted iso to boot from.
   else
     exit 1
   fi
fi

echo "Updating software via apt-get..."
apt-get update
# apt-get upgrade -y

echo "Removing unneeded packages..."
apt-get remove -y libreoffice-* qemu-user-static openjdk-*

apt-get autoremove -y

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
   rsync -avz $CONFIG_DIR --verbose /
   echo "We have copied OPAC files." > $OPAC_COPIED_FLAG
   echo "You should reboot to see changes!"
   echo "Also -- before that...Change the default password for the 'pi' user by running 'passwd pi'!"
else
   echo "Already copied OPAC setup files from $CONFIG_DIR".
fi

echo "Done!"
