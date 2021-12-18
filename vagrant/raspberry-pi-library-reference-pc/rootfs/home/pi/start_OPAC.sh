#!/bin/sh

while true; do
    chromium-browser -incognito --proxy-server="127.0.0.1:8118" "library.clamsnet.org"
done
