# Raspberry Pi Library Reference PC

Meant to set up a Raspberry Pi to serve as an Online Public Access Catalogue (OPAC) computer.

No video games, non-worksafe sites, email browsing, etc.

Migrated from <https://github.com/HenryFBP/obpl-opac>

## Testing locally

1.  Install [Vagrant](https://vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2.  Clone/download this repo.
3.  In this directory (`/vagrant/raspberry-pi-library-reference-pc/`), run `vagrant up` in terminal
4.  Open VirtualBox and reboot the Pi. It should reboot into a fully configured OPAC PC!

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

## How do I use this on a real Raspberry Pi?

1.  Install [a base x86/x64 image](https://www.raspberrypi.com/software/) onto a physical Raspberry Pi's SD card.
2.  Copy `setup-script.sh` and `opac-config-dir/` onto your raspberry pi using a USB stick, or by using 
    
    ```bash
    apt install -y git
    git clone https://github.com/HenryFBP/VagrantPackerFiles
    cd VagrantPackerFiles/vagrant/raspberry-pi-library-reference-pc/
    ```
    
3.  Edit the `CONFIG_DIR` variable in `setup-script.sh` to reflect the place that `opac-config-dir/` was copied to.
4.  Run `bash setup-script.sh` and examine terminal output for messages to see if succeeded or failed.
5.  Change the password for the `pi` user by running `passwd pi`
    1.  **This step is critical for security**, as users can use `CTRL-ALT-T` to switch to a terminal and login with the default creds `pi:raspberry`, and then circumvent the Privoxy proxy, or possibly do this during GRUB boot if they are very knowledgeable with Linux.

6.  You should see a black screen with Chromium running a proxy that only lets you visit sites defined in the below list:

    [./opac-config-dir/etc/privoxy/opac.action](./opac-config-dir/etc/privoxy/opac.action)

    Feel free to edit it to reflect your organization's domain whitelist.

## What sites are blocked?

Determined by this file:

[./opac-config-dir/etc/privoxy/opac.action](./opac-config-dir/etc/privoxy/opac.action)

It's in "whitelist/allowlist" configuration (Due to line 3), to block all by default and only allow specific domains. 

Feel free to edit it to your organization's needs.

## Issues

TODO

## TODO

-   Use Packer to create base RPI image
    -   https://www.packer.io/guides/automatic-operating-system-installs/preseed_ubuntu

-   Currently, images are produced by running `vagrant package` in this directory.
    -   It creates a `package.box` file (zip file) that can be uploaded to Vagrant public box repository.