# Read Config and Set Globals
$ScriptDir = Split-Path $MyInvocation.MyCommand.Path -Parent

$config = (Get-Content "$ScriptDir\config.json" -Raw) | ConvertFrom-Json

$ProjectDir = $config.'ProjectDir'
$CookieCutterDir = $config.'CookieCutterDir'
# Print Project Directory
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
