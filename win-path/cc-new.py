import json
import os
import sys
from pathlib import Path

from cookiecutter.main import cookiecutter
from tabulate import tabulate


def is_hidden(dir_path: Path):
    if dir_path.name.startswith("."):
        return True
    else:
        return False


def select_cookiecutters(cookiecutter_dir: Path) -> dict:
    ccs = [x for x in cookiecutter_dir.iterdir() if x.is_dir() and not is_hidden(x)]

    selection = []
    table_data = []

    index = 0
    for cookie in ccs:
        cookie_data = {"index": index, "name": cookie.name, "path": cookie}

        selection.append(cookie_data)
        table_data.append([index, cookie.name])

        index += 1

    table = tabulate(
        table_data, headers=["Index", "Templates"], stralign="center", numalign="center"
    )
    print(table)

    user_select = input("\nSelect Template to Run: ")

    return selection[int(user_select)]["path"]


class AutoCC:
    def __init__(self) -> None:

        config = CWD.joinpath("config.json")
        with open(config, "r") as f:
            settings = json.load(f)

        try:

            self.install_req: bool = settings["ccSettings"]["installRequirements"]
            self.default_pkg: list = settings["ccSettings"]["defaultPackages"]
            self.gh_mode: str = settings["ccSettings"]["githubRepoMode"]
            # self.use_gh_cli: bool = settings["ccSettings"]["useGithubCLI"]
        except:
            print("One or more required settings is missing.")
            exit()

    def run_cookiecutter(self, cc: Path):
        if cc.is_dir():
            new_project = Path(cookiecutter(str(cc), output_dir=PROJECT_DIR))
            self.make_venv(new_project)

            AutoCC.create_repo(new_project)

            if self.gh_mode == "Prompt":
                user_selected_mode = input(
                    "Would you like to create a github repo? [y/n] "
                )

                if user_selected_mode == "y":
                    self.gh_mode = "Yes"
                else:
                    self.gh_mode = "No"

            if self.gh_mode == "Yes":
                AutoCC.create_github_repo(new_project)

            os.system(f"code {new_project}")

        else:
            print("No Cookie Cutter Found, Sorry!")

    def run_from_arg(self, name: str):
        cc = CC_DIR.joinpath(f"cookiecutter-{name}/")

        self.run_cookiecutter(cc)

    def make_venv(self, project_dir: Path):
        os.chdir(project_dir)
        python_path = project_dir.joinpath("./venv/Scripts/python.exe")

        arg_1 = "python -m venv ./venv"
        arg_2 = f"{python_path} -m pip install --upgrade pip"
        arg_3 = f"{python_path} -m pip install black pylint coloredlogs"
        requirements = f"{python_path} -m pip install requirements ".join(
            [str(v) for v in self.default_pkg]
        )

        args = [arg_1, arg_2, arg_3]

        for arg in args:
            print(arg)
            os.system(arg)

        if self.install_req:
            os.system(requirements)

    @staticmethod
    def create_repo(project_dir: Path):
        os.chdir(project_dir)
        os.system("git init")
        os.system("git add .")
        os.system("git commit -m 'Init'")

    @staticmethod
    def create_github_repo(project_dir: Path):
        os.chdir(project_dir)
        os.system(f"gh repo create {project_dir.name}")


if __name__ == "__main__":
    CWD = CWD = Path(__file__).parent

    # Set Settings
    config = CWD.joinpath("config.json")
    with open(config, "r") as f:
        settings = json.load(f)

    # Directories
    PROJECT_DIR = Path(settings["ProjectDir"])
    CC_DIR = Path(settings["CookieCutterDir"])

    auto_cc = AutoCC()

    try:
        ARG = sys.argv[1]  # Run Specific CookiesCutter Shortcut "cc-new python"
    except:
        ARG = None

    if ARG != None:
        auto_cc.run_from_arg(ARG)

    selected_tempalte = select_cookiecutters(CC_DIR)

    auto_cc.run_cookiecutter(selected_tempalte)
