# Kali Vagrant VM

## Required setup

Please [see the README.md](../README.md) at `../README.md` for a list of required software.

## Features

### Pentesting demos

See `~/Github/` in the VM for some cool repos that let you pentest locally. Please read the README files in each repo.

I have tried to find ones that use Docker for your convenience to avoid manual setup.

### Tor
- Kalitorify -- run `kalitorify --help`. It is a transparent Tor proxy tool that edits iptables for you.
- Tor Browser helper

### Desktop apps
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
