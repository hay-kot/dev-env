import os
from pathlib import Path

from python_scripts.my_settings import config

class ScriptSetup:
    def __init__(self, json) -> None:

        self.name = json["name"].replace(".py", "")
        self.packages = json["pkgs"]
        self.args = json["args"]

        self.venv = f"./venv-{self.name}"
        self.python = config.py_venv_dir.joinpath(f"./{self.venv}/Scripts/python.exe")

    def create_venv(self):
        os.chdir(config.py_venv_dir)
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
        py_script = config.py_script_dir.joinpath(f"{self.name}.py")
        ps_script = config.ps_script_dir.joinpath(f"{self.name}.ps1")

        template = f"{self.python} {py_script}"

        if self.args > 0:
            for i in range(self.args):
                template = f"$Arg_{i} = $args[{i}] \n" + template + f" $Arg_{i}"

        with open(ps_script, "w+") as f:
            f.write(template)


if __name__ == "__main__":
    print("Starting Script Generator")
    CWD = CWD = Path(__file__).parent

    config.get_venv_settings()

    for data in config.py_setup_list:
        job = ScriptSetup(data)

        job.create_venv()
        job.create_ps()

    print("Completed")
