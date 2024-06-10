# Ansible minecraft

These are config files for Ansible that let you provision Minecraft servers quickly and easily.

## Requirements

Playing: Use Prism Launcher to play Minecraft. Or FTB Launcher/CurseForge, but Prism is recommended.
Local testing: Linux OS, Virtualbox, Vagrant, Ansible
Deploying: Linux OS, Ansible

## Testing locally

    vagrant up --provision
    vagrant ssh
    systemctl status minecraft
    journalctl -u minecraft.service

## Deploying to a baremetal machine

1. Clone this repo
2. `cd` to the desired server folder
3. Run `ansible-playbook <minecraft_version>.yml`
4. Run `systemctl status <minecraft_service_name>`
5. Visit `<ip>:25565` with minecraft.
