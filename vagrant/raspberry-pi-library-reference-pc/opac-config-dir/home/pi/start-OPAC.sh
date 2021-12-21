#!/bin/sh

# Change this to your library URL. No spaces.
libraryurl=library.clamsnet.org

while true; do
    chromium -incognito --proxy-server="127.0.0.1:8118" "$libraryurl"
done
