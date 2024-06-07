# Ansible minecraft

## Testing locally

    vagrant up
    vagrant ssh
    systemctl status minecraft
    journalctl -u minecraft.service

## Deploying to a baremetal machine

1. Clone this repo
2. `cd` to the desired server folder
3. Run `ansible-playbook minecraft_<version>.yml`
4. Run `systemctl status minecraft`
5. Visit `<ip>:25565` with minecraft.
