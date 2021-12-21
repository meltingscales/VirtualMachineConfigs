# Raspberry Pi Library Reference PC

Meant to set up a Raspberry Pi to serve as an Online Public Access Catalogue (OPAC) computer.

No video games, non-worksafe sites, email browsing, etc.

Migrated from <https://github.com/HenryFBP/obpl-opac>
## Base Images

### x86

This work was tested on an x86 (NOT ARM!) image:

<https://downloads.raspberrypi.org/rpd_x86/images/rpd_x86-2021-01-12/2021-01-11-raspios-buster-i386.iso>

-   Release date: 
    -   January 11th 2021
-   Kernel version:
    -   4.19
-   Size:
    -   2,948MB
-   SHA256 file integrity hash (of `.iso` file, not `.box` file): 
    -   `c78c8dca8ca80ffbac90f4cedfedb6793b37b06df307b0c87e778eef3842a9be`

### ARM

NOTE: Not tested yet.

https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-11-08/2021-10-30-raspios-bullseye-armhf.zip

## How do I use this?

1.  Install base ARM image onto a physical Raspberry Pi
2.  Copy `setup-script.sh` and `opac-config-dir/` onto your raspberry pi using a USB stick, or by using `git clone https://github.com/HenryFBP/VagrantPackerFiles && cd VagrantPackerFiles/vagrant/raspberry-pi-library-reference-pc/`
3.  Edit `CONFIG_DIR` variable in `setup-script.sh` to reflect the place that `opac-config-dir/` was copied to.
4.  Run `bash setup-script.sh` and examine stdout for messages to see if succeeded or failed.
5.  Repeat 3/4 if unsuccessful, or restart Pi.
6.  You should see a black screen with Chromium running a proxy that only lets you visit sites defined in the below list:

    [./opac-config-dir/etc/privoxy/opac.action](./opac-config-dir/etc/privoxy/opac.action)

    Feel free to edit it to reflect your organization's domain whitelist.

## Issues

TODO

## TODO

-   Use Packer
    -   https://www.packer.io/guides/automatic-operating-system-installs/preseed_ubuntu