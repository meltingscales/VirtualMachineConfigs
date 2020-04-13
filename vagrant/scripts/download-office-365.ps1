#https://www.ryadel.com/en/ms-office-2016-365-official-iso-img-images-for-download-offline-install-product-key-required/

Import-Module BitsTransfer

function EnsureExists($url, $filepath)
{
    if (![System.IO.File]::Exists($filepath))
    {
        Start-BitsTransfer -Source "$url" -Destination "$filepath"
    }
}

$file = -join ((Resolve-Path "~/Downloads/"), "Office365.img")
$url = "http://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/O365ProPlusRetail.img"

EnsureExists -url $url -file $file