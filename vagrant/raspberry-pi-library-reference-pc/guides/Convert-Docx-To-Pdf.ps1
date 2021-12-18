# Turns all DOCX files into PDF files.

$Word=New-Object -ComObject Word.Application

$Files=Get-ChildItem ".\*.docx"

ForEach ($File In $Files) {
    $Document=$Word.Documents.Open($File.FullName)

    $Name=($Document.FullName).Replace("docx", "pdf")

    Write-Host($Name)

    $Document.SaveAs([ref] $Name, [ref] 17)
    $Document.Close()
}