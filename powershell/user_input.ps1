
Write-Host -NoNewLine "Enter something to un-scronch:
 > "

$in = $Host.UI.ReadLine() # Read line without adding an ugly colon.

$expanded = [char[]]$in # Inject spaces.

Write-Host ($in+" -> "+$expanded) 