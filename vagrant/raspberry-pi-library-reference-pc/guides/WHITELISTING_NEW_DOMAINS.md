# Where can I whitelist new domains?

You can find the domains whitelisted under the `/etc/privoxy/opac.action` file.

PROTIP:

1. Open terminal with `CTRL-ALT-T`.
2. Type in `sudo pcmanfm /etc/privoxy` to open `pcmanfm` to the Privoxy configuration directory.
	a. Alternatively, `sudo nano /etc/privoxy/opac.action` will do the trick.

# Cool, how do I do it?

If simply viewing the file doesn't answer this question, please go to https://www.privoxy.org/user-manual/actions-file.html

You just add the site below the ```{ -block }``` section, like so:

	```
	{ -block }
	
	www.kongregate.com
	www.abcgames.com

	```
	
etc.

Section 8.4 details the 'patterns' that you can use.

# Why does X pattern exist? What's with the asterisks/`*`s?

`*.google.com` is a pattern that allows `maps.google.com`, `docs.google.com`, etc.

This is why you see `*.clamsnet.org`, because the pattern `clamsnet.org` does NOT cover:

- encore.clamsnet.org
- library.clamsnet.org
- info.clamsnet.org

Anyways, have fun blocking!