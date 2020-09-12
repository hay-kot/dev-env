#!/bin/bash
$Repo = $args[0]
Set-Variable -Name "ProjectDir" -Value "C:\MAIN\PROJECT\DIRECTORY"  # This is where your projects will be created

Set-Location -Path $ProjectDir

git clone $Repo

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