Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

choco feature enable -n allowGlobalConfirmation

choco install -y GoogleChrome
choco install -y vscode
choco install -y notepadplusplus
choco install -y git
choco install -y atom
choco install -y 7zip
choco install -y tor
choco install -y ghostscript
choco install -y imagemagick
