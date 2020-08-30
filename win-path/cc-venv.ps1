$NewProject = Get-ChildItem | Sort-Object lastwritetime | Select-Object -Last 1

# Sets Location to CookieCutter Created Directory
Set-Location $NewProject

# Calls Custom venv alias
venv

pip install -r requirements.txt

# Opens Up Created Folder in VS Code
code %cd%