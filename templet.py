import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO , format='[%(asctime)s]:%(message)s:')

project_name = "cnn_classifier"

list_of_files = [
    "github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory;(filedir) for the file:(filename)"):


    if  (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        
