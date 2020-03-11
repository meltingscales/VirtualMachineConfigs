# Windows 7

Windows 7 for apps that need Windows 7.

WinRM is not enabled by default.

To enable, run this in `powershell.exe`:

    WinRM qc
    
And follow the prompts.

After that, `vagrant up --provision` should work.