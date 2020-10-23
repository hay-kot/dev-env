import json
import os
from pathlib import Path


class ScriptSetup:
    def __init__(self, json) -> None:

        self.name = json["name"].replace(".py", "")
        self.packages = json["pkgs"]
        self.args = json["args"]

        self.venv = f"./venv-{self.name}"
        self.python = VENV_DIR.joinpath(f"./{self.venv}/Scripts/python.exe")

    def create_venv(self):
        os.chdir(VENV_DIR)
        python_path = self.python

        requirements = " ".join([str(v) for v in self.packages])
        arg_1 = f"python -m venv {self.venv}"
        arg_2 = f"{python_path} -m pip install --upgrade pip"
        arg_3 = f"{python_path} -m pip install black pylint"
        arg_4 = f"{python_path} -m pip install {requirements}"

        args = [arg_1, arg_2, arg_3, arg_4]

        for arg in args:
            print(arg)
            os.system(arg)

    def create_ps(self):
        py_script = PY_SCRIPT_DIR.joinpath(f"{self.name}.py")
        ps_script = PS_SCRIPT_DIR.joinpath(f"{self.name}.ps1")

        template = f"{self.python} {py_script}"

        if self.args > 0:
            for i in range(self.args):
                template = f"$Arg_{i} = $args[{i}] \n" + template + f" $Arg_{i}"

        with open(ps_script, "w+") as f:
            f.write(template)


if __name__ == "__main__":
    print("Starting Script Generator")
    CWD = CWD = Path(__file__).parent

    # Set Settings
    config = CWD.joinpath("config.json")
    with open(config, "r") as f:
        settings = json.load(f)

    PY_SCRIPT_DIR = CWD.joinpath(settings["pythonVirtualEnvs"]["pythonScripts"])
    PS_SCRIPT_DIR = CWD.joinpath(settings["pythonVirtualEnvs"]["powershellScripts"])
    VENV_DIR = CWD.joinpath(settings["pythonVirtualEnvs"]["venvDirectory"])
    SETUP_LIST = settings["pythonVirtualEnvs"]["setupList"]

    for data in SETUP_LIST:
        job = ScriptSetup(data)

        job.create_venv()
        job.create_ps()

    print("Completed")
