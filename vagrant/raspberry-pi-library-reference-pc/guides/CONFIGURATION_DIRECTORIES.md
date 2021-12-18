# List of configuration directories and files

- `/etc/privoxy/`: The whitelists and blacklists.

	- `opac.action`: Our custom (white/black)list.


- `/etc/xdg/lxsession/LXDE-pi/`: The folder that controls the desktop environment.

	- `autostart`: 	The file that controls what elements of the desktop are enabled or disabled.
	Note that all the settings for background, top bar, etc. are all disabled,
	denoted by the '#' symbol before the '@' commands.
					
	Also note that there is a command that executes a script located at
	`/home/pi/start_OPAC.sh`. This is how Chromium, the browser, is started! 

					
- `/home/pi/start_OPAC.sh`: As previously mentioned, this starts up the browser up.
	It also restarts the browser if it closes. The `while true; do`
	accomplishes this.
							
	If you look inside the file, please note the startup flags that I
	have passed to chromium, most notably `--proxy-server=<...>` and
	`"library.clamsnet.org"`.
							
	The `proxy-server` argument is how Privoxy controls Chromium's
	access to the internet.
							
	Privoxy runs at 127.0.0.1:8118 by default.

That's about it!