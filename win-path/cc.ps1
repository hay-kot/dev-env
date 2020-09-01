# Set Dump Directory for Projects
Set-Variable -Name "ProjectDir" -Value "C:\MAIN\PROJECT\DIRECTORY"  # This is where your projects will be created

# Set Directory of your CookieCutters
Set-Variable -Name "CookieCutterDir" -Value "C:\PATH\TO\COOKIECUTTERS" # This is where your CookieCutters Live
Write-Host "Default Project Dir: $ProjectDir" -ForegroundColor DarkYellow


$cookiecutterID = $args[0]
Set-Location -Path $ProjectDir

$CCPath = "$CookieCutterDir\cookiecutter-$cookiecutterID"


$CCExists = Test-Path $CCPath

if ($CCExists -eq $True) {
    cookiecutter cookiecutter-$cookiecutterID

    # Get Most Recent Folder Created
    $NewProject = Get-ChildItem | Sort-Object lastwritetime | Select-Object -Last 1

    # Sets Location to CookieCutter Created Directory
    Set-Location $NewProject

    Write-Host "Creating Virtual Environment in $NewProject" -ForegroundColor DarkYellow

    # Calls Custom venv alias
    venv

    Write-Host "Install Pip Requirements..." -ForegroundColor DarkYellow
    pip install -r requirements.txt

    # Opens Up Created Folder in VS Code
    code %cd%
}
else {
    Write-Host " "
    Write-Host "No Matching CookieCutter." -ForegroundColor DarkRed
    Write-Host " "
    Write-Host "Avaiable CookieCutters:" -Separator '-' -ForegroundColor DarkRed
    Write-Host "-----------------------" -ForegroundColor DarkRed
    Get-ChildItem $CookieCutterDir -directory -name
    Write-Host " "
}
