# demo.ps1

function hello() {
    echo("Ciao")
}

$message = "Coucou Powershell"
echo($message)

$nb = Read-Host -Prompt "Tapez un chiffre"

if ([int]$nb -gt 10) {
    echo("Laisse-moi tranquille")
} else {
    $i = 0
    while ($i -lt [int]$nb) {
        # echo("Tutto bene")
        hello
        $i = $i + 1
    }
}