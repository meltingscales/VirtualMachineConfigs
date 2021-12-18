# Hardware

- There is no power button, no reboot button, etc.
- The raspberry pi doesn't come with any hardware that can interface with humans.
- To reboot, just unplug and plug back in the power cable.

  It is a microUSB cable.

# General

- `CTRL-ALT-T` opens terminal.
- `sudo reboot now` will reboot the machine. Useful if anything weird happens or the pi is
  unresponsive or crashing.
- Going to `https://www.privoxy.org/config/` or `http://p.p/` (yes, that is actually a URL) _would_ allow 
  you to configure stuff via the web, but I disabled that feature, so now it just lets you
  *look* at the settings.

# Disabling the firewall

If you want to use the computer for sites like `google.com` or `facebook.com`, you _can_ edit the
configuration by running `sudo gedit /etc/privoxy/opac.action` and commenting out this line:

```/ #Matches all URLS.```

, where the commented-out version looks like:

```#/ #Matches all URLS.```

Save the file, and ta-da! No more firewall.

Just remember to change it back or else OTHER PEOPLE will be able to go on Facebook, etc.


# Terminal commands

- `pwd` tells you where you are. Stands for 'print working directory'.
- `ls` displays files in current directory. Stands for 'list'.
- `cd` changes your current directory. Stands for 'change directory'.
- `sudo <COMMAND [...]>` executes a command with Superuser privileges. Stands for 'superuser do'.

- `pcmanfm` opens file explorer, similar to `explorer.exe` in Windows and `finder` in OSX.
	- I recommend doing `sudo pcmanfm` to ensure you can save any document opened using it.
- `lxpanel` turns on the desktop.
- `gedit <FILENAME>` edits a file. Note that you may need to run `sudo gedit <FILENAME>` if you cannot save it.