# demo2.ps1

function createFolder() {
    # cette fonction prend un paramètre en entrée
    param($username)
    #echo($username)

    # création du dossier utilisateur
    New-Item -Path "./$username" -ItemType Directory

    # création d'un fichier dans le dossier utilisateur
    New-Item -Path "./$username/credentials.txt" -ItemType File

    # écriture dans le fichier credentials.txt
    $credentials = "username:$username;password:1234"
    Set-Content -Path "./$username/credentials.txt" -Value $credentials


}

$users = @("Chris", "Gab", "Ale")
foreach($user in $users) {
    createFolder($user)
}