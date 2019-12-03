#https://www.ryadel.com/en/ms-office-2016-365-official-iso-img-images-for-download-offline-install-product-key-required/

function DownloadFile($url, $targetFile)
{
    $uri = New-Object "System.Uri" "$url"

    $request = [System.Net.HttpWebRequest]::Create($uri)

    $request.set_Timeout(15000) #15 second timeout

    $response = $request.GetResponse()

    $totalLength = [System.Math]::Floor($response.get_ContentLength()/1024)

    $responseStream = $response.GetResponseStream()

    $targetStream = New-Object -TypeName System.IO.FileStream -ArgumentList $targetFile, Create

    $buffer = new-object byte[] 10KB

    $count = $responseStream.Read($buffer, 0, $buffer.length)

    $downloadedBytes = $count

    while ($count -gt 0)

    {

        $targetStream.Write($buffer, 0, $count)

        $count = $responseStream.Read($buffer, 0, $buffer.length)

        $downloadedBytes = $downloadedBytes + $count

        Write-Progress -activity "Downloading file '$( $url.split('/') | Select-Object -Last 1 )'" -status "Downloaded ($([System.Math]::Floor($downloadedBytes/1024) )K of $( $totalLength )K): " -PercentComplete ((([System.Math]::Floor($downloadedBytes/1024)) / $totalLength)  * 100)

    }

    Write-Progress -activity "Finished downloading file '$( $url.split('/') | Select-Object -Last 1 )'"

    $targetStream.Flush()

    $targetStream.Close()

    $targetStream.Dispose()

    $responseStream.Dispose()

}

function EnsureExists($url, $filepath)
{
    if (![System.IO.File]::Exists($filepath))
    {
        DownloadFile -url "$url" -targetFile "$filepath"
    }
}

$file = "~/Downloads/Office365.img"
$url = "http://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/O365ProPlusRetail.img"

EnsureExists($url, $file)