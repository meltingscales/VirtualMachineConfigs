# README

A collection of some useful Vagrantfiles and setup scripts.

Feel free to do whatever you want with this code.
No license.

## Vagrant plugins

Some of these boxes require these plugins.

Install them with `vagrant plugin install <PLUGIN>` if you get an error message.

-   `vagrant plugin install vagrant-disksize` 
-   `vagrant plugin install vagrant-libvirt` (see <https://github.com/vagrant-libvirt/vagrant-libvirt>) and 
    <https://github.com/hashicorp/vagrant/issues/7039>
    -   I recommend using `virt-manager` to manage KVM VMs in a GUI. Similar to VirtualBox.

## Running

- Install VirtualBox. See <https://www.virtualbox.org/>.

- Some of these VMs use KVM. This is more advanced. Use Google. VB is easier.

- Install Vagrant. See <https://www.vagrantup.com/downloads.html> for instructions.

- Then, in any of these directories, run `vagrant up` in a terminal. See each sub-readme for specific instructions.

## Issues

### VMs won't start

See <https://www.virtualbox.org/ticket/18536>.

Run `scripts/fix-hyperv-issues.ps1` and then restart windows TWICE.