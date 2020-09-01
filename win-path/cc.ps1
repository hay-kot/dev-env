# Set Dump Directory for Projects
Set-Variable -Name "ProjectDir" -Value "C:\MAIN\PROJECT\DIRECTORY"  # This is where your projects will be created

# Set Directory of your CookieCutters
Set-Variable -Name "CookieCutterDir" -Value "C:\PATH\TO\COOKIECUTTERS" # This is where your CookieCutters Live
Write-Output "Default Project Dir: $ProjectDir"


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

    Write-Output "Creating Virtual Environment in $NewProject"

    # Calls Custom venv alias
    venv

    Write-Output ""
    pip install -r requirements.txt

    # Opens Up Created Folder in VS Code
    code %cd%
}
else {
    Write-Host " "
    Write-Host "No Matching CookieCutter." -ForegroundColor Red
    Write-Host " "
    Write-Host "Avaiable CookieCutters:" -Separator '-' -ForegroundColor Cyan
    Write-Host "-----------------------" -ForegroundColor Cyan
    Get-ChildItem $CookieCutterDir -directory -name
    Write-Host " "
}
