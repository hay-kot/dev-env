## Setup
1. [Install CookieCutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
    ```bash
    pip install --user cookiecuter
    ```
2. Put this directory and CookieCutter in your windows PATH. 
3. Change CookieCutter config to reference `./CookieCutter/custom-config.yml`

## Setup CookieCutter Scripts
1. Change Project Parent Director for ps1 scripts
   ```powershell
   Set-Variable -Name "ProjectDir" -Value "D:\PATH\TO\PROJECT"
   ```

## Descriptions
#### venv.ps1
Creates a virtual enviroment in the current directory while upgrading pip and installing black and pylint.

#### venv-clean.ps1
Created a virtual enviroment in the current directory and upgrades pip