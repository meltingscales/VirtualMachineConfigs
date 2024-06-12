# Ansible minecraft

These are config files for Ansible that let you provision Minecraft servers quickly and easily.

## Adding new server modpacks

You can reasonably expect to be able to copy any working example in this folder and just modify some variables. 

HOWEVER: Some of these installations are slightly different in the following ways:

- Some require you to invoke the Forge installer once
- Some require an install script like `Install.sh`
- Some require you to invoke the Forge server/Minecraft server directly
- Some require a startup script like `ServerStart.sh`
- Some require you to flatten a nested directory from the modpack .zip file

When you create and test a new modpack, just monitor the output from Ansible, as well as inspect the modpack files inside `/opt/minecraft/` and you should be able to figure out what needs to be changed.

## Requirements

- Playing: Use Prism Launcher to play Minecraft. Or FTB Launcher/CurseForge, but Prism is recommended.
- Local testing: Linux OS, Virtualbox, Vagrant, Ansible
- Deploying: Linux OS, Ansible

## Testing locally

```bash
vagrant up --provision
vagrant ssh

# for service status
systemctl status minecraft

# for logs
journalctl -u minecraft.service
tail -f /opt/minecraft/*/logs/latest.log
```

## Deploying to a baremetal machine

Note tha the baremetal machine must run Debian. Ubuntu works just fine.

1. Clone this repo
2. `cd` to the desired server folder
3. Run `ansible-playbook <minecraft_version>.yml`
4. Run `systemctl status <minecraft_service_name>`
5. Visit `<ip>:25565` with minecraft.
