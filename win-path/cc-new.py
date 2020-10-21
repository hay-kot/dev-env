from cookiecutter.main import cookiecutter
from pathlib import Path
import json

CWD = CWD = Path(__file__).parent

CC_DIR: Path
PROJECT_DIR: Path


def set_globals():
    config = CWD.joinpath("config.json")
    with open(config, "r") as f:
        settings = json.load(f)

         
        project_dir = Path(settings["ProjectDir"])
        cc_dir = Path(settings["CookieCutterDir"])

    return cc_dir, project_dir



if __name__ == "__main__":
    CC_DIR, PROJECT_DIR = set_globals()

    print(CC_DIR, PROJECT_DIR, sep="\n")