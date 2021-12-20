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

echo Updating software via apt-get...
apt-get update && apt-get upgrade

apt-get install gedit

echo "Installing 'Chromium', an open-source Google Chrome-like browser."
apt-get install chromium-browser -y

echo "Installing 'unclutter' to hide cursor when not active..."
apt-get install unclutter -y

echo "Installing 'privoxy' to prevent people from accessing certain sites."
apt-get install privoxy -y







exit 1 #TODO redo this lightdm block 
#To Disable Sleep:

# Edit the lightdm.conf file by entering: sudo nano /etc/lightdm/lightdm.conf
# Add the following lines to the [SeatDefaults] section:
# xserver-command=X –s 0 dpms


echo "Opening editor for 'lightdm' to prevent sleep... See comments in shell script."
read -p "ENTER to continue..." nothing

nano "/etc/lightdm/lightdm.conf"
exit 1 #TODO redo this lightdm block 








exit 1 #TODO redo this LXLE block 
# Edit the LXDE autostart file by entering:
# sudo nano /etc/xdg/lxsession/LXDE/autostart

# Comment out everything by adding # in front of each existing line and then add the following lines:
# @xset s off
#
# @xset –dpms
#
# @xset s noblank
#
# while true; do 
# 	chromium-browser –kiosk –incognito http://yourlibrarycatalogue.html
# done

echo "Opening editor for 'LXDE' autostart file..."
read -p "ENTER to continue..." nothing
nano "/etc/xdg/lxsession/LXDE/autostart"
exit 1 #TODO redo this LXLE block 







echo "Done! Reboot for glory!"