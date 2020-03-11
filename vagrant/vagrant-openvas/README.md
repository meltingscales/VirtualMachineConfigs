# Vagrant-defined OpenVAS Host

    vagrant up
    vagrant ssh
    VM> sudo -i
    VM> openvas-setup

## Notes

 * If during `openvas-setup` you encounter the error `[e] Update of CVEs failed at file '/var/lib/openvas/scap-data/nvdcve-2.0-2011.xml': xsltproc exited with code 137` simply re-run `openvas-setup`.
