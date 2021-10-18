# disable fast startup
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /v HiberbootEnabled /t REG_DWORD /d "0" /f

# list features
Get-WindowsOptionalFeature -online

# disable
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All
Disable-WindowsOptionalFeature -Online -FeatureName HypervisorPlatform
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
Disable-WindowsOptionalFeature -Online -FeatureName Containers
Disable-WindowsOptionalFeature -Online -FeatureName Containers-DisposableClientVM
Disable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
