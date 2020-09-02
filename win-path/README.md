## Setup
1. [Install CookieCutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
    ```bash
    pip install --user cookiecutter
    ```
2. Put this directory and CookieCutter in your windows PATH. There are many ways to do this, just find some way to call the script without typing to whole path.
3. Change CookieCutter config to reference `./CookieCutter/custom-config.yml`

## Setup CookieCutter Scripts
1. Change Project Parent Director for ps1 scripts in `cc.ps1`

   ```powershell
   # Set Dump Directory for Projects
   Set-Variable -Name "ProjectDir" -Value "C:\MAIN\PROJECT\DIRECTORY"  # This is where your projects will be created

   # Set Directory of your CookieCutters
   Set-Variable -Name "CookieCutterDir" -Value "C:\PATH\TO\COOKIECUTTERS" # This is where your CookieCutters Live
   Write-Output "Default Project Dir: $ProjectDir"
   ```

## Description and Use
#### cc.ps1 - `cc <template>`
This is the main cookiecutter script that takes in 1 argument that is the appended name to your template. For Example, if you were to call the `cookiecutter-flask` template you would traditionally use `cookiecutter cookiecutter-flask`. With this script you call `cc flask` instead.

This assumes that your templates are located in the `C:\PATH\TO\COOKIECUTTERS` that you previously set. This script also performs some other set-up tasks associated with creating a python project enviroment

**Execution Order:**
 1. Checks if CookieCutter template exists
 2. Calls CookieCutter and takes in user inputs.
 3. Traverses into directory and creates a virtual enviroment using the venv alias in this directory
 4. Upgrade Pip
 5. Install requirements.txt
 6. Open project with VSCode

#### venv.ps1 - `venv`
Creates a virtual enviroment in the current directory while upgrading pip and installing black and pylint.

#### venv-clean.ps1 - `venv-clean`
Created a virtual enviroment in the current directory and upgrades pip
