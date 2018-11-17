

$in = "-1";

while(!($in -eq "0")) { # While it is not zero,

    Write-Host -NoNewLine "Enter a choice, 1 or 2. 0 Exits.
> "

    $in = $Host.UI.ReadLine() # Read line without adding an ugly colon.

    Switch($in)
    {
        "0" {break;}

        "1" {
            Write-Host -NoNewLine "One!`n";
            break;
        }
    
        "2" {
            Write-Host -NoNewLine "Two!`n";
            break;
        }

        default {
            "Invalid choice.`n"
            break;
        }
    }
}