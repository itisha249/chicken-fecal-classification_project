from pathlib import Path

# CONFIG_FILE_PATH = Path("config/config.yaml")
# PARAMS_FILE_PATH = Path("param.yaml")
# Set the project root dynamically
project_root = Path("d:/project/chicken-fecal-classification_project")

# Define paths relative to the project root
CONFIG_FILE_PATH = project_root / "config/config.yaml"
PARAMS_FILE_PATH = project_root / "param.yaml"
