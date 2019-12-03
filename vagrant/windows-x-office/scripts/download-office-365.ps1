#https://www.ryadel.com/en/ms-office-2016-365-official-iso-img-images-for-download-offline-install-product-key-required/

$file="~/Downloads/Office365.img"
$url="http://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/O365ProPlusRetail.img"

if(![System.IO.File]::Exists($file)){
    Invoke-WebRequest -Uri "$url" -OutFile "$file"
}
