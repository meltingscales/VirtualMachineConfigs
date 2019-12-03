#http://officecdn.microsoft.com.edgesuite.net/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/O365HomePremRetail.img

$file="~/Downloads/O365HomePremRetail.img"
$url="http://officecdn.microsoft.com.edgesuite.net/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/O365HomePremRetail.img"

if(![System.IO.File]::Exists($file)){
    Invoke-WebRequest -Uri "$url" -OutFile "$file"
}
