import json
from pathlib import Path

CWD = Path(__file__).parent
DEV_ENV = CWD.parent
CONFIG_FILE = DEV_ENV.joinpath("config.json")


def read_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


class MySettings:
    def __init__(self) -> None:

        self.all_settings = read_config()

        self.project_dir = Path(self.all_settings["ProjectDir"])
        self.cc_dir = Path(self.all_settings["CookieCutterDir"])

    def dump_settings(self):
        self.all_settings = None

    def get_script_settings(self):
        self.all_settings = read_config()

        script_settings = self.all_settings["pythonScripts"]

        self.install_req: bool = script_settings["ccSettings"]["installRequirements"]
        self.default_pkg: list = script_settings["ccSettings"]["defaultPackages"]
        self.gh_mode: str = script_settings["ccSettings"]["githubRepoMode"]

    def get_venv_settings(self):
        self.all_settings = read_config()

        venv_settings = self.all_settings["pythonVirtualEnvs"]

        self.py_script_dir = DEV_ENV.joinpath(venv_settings["pythonScripts"])
        self.py_venv_dir = DEV_ENV.joinpath(venv_settings["venvDirectory"])
        self.py_setup_list: list = venv_settings["setupList"]

        self.ps_script_dir = DEV_ENV.joinpath(venv_settings["powershellScripts"])


config = MySettings()

if __name__ == "__main__":
    settings = MySettings()
    settings.get_script_settings()
    settings.get_venv_settings()
