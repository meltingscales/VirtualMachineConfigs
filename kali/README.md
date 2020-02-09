# Kali Vagrant VM

## Required setup

Please see the README.md at `../README.md` for a list of rqeuired software.

## Features

- Kalitorify -- run `kalitorify --help`. It is a transparent Tor proxy tool that edits iptables for you.
- Tor Browser helper
- `enpass` (password manager)


Snaps:
 - `snap run android-studio` (android VM)
 - `snap run wickrme` (chat)
 - `snap run discord` (chat)

That's about it. It's Kali. Many uses!

## Caveats/extra setup

You must run `vagrant up --provision` after SSH fails due to a step that enables AppArmor breaking SSH connections.

Too lazy to fix.

The command for one-touch deploys is now:

`vagrant up; vagrant up --provision`

instead of just:

`vagrant up`.
