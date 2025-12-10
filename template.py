# Through using this file we are able to create file structures needed for our ML project
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

project_name = "ML Project"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "configs/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    # 1. Convert the filepath string to a Path object for clean path manipulation
    filepath = Path(filepath)

    # 2. Separate the directory name and the file name
    filedir, filename = os.path.split(filepath)

    # 3. Create the directories if filedir is not empty and doesn't exist
    if filedir != "":
        # os.makedirs creates all intermediate directories needed
        os.makedirs(filedir, exist_ok=True)
        print(f"Created directory: {filedir}")

    # 4. Create an empty file if it doesn't exist and is not a directory path
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Open in write mode ('w') and close immediately to create an empty file
        with open(filepath, "w") as f:
            pass
        print(f"Created empty file: {filepath}")
    else:
        print(f"{filepath} already exists")