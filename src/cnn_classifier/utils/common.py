import os
import yaml
import json
import joblib
import base64
from pathlib import Path
from typing import Any, List
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
import logging  # Added logger setup

# Logger setup with timestamp
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a YAML file and return its contents as a ConfigBox."""
    try:
        if os.path.getsize(path_to_yaml) == 0:
            raise ValueError(f"YAML file {path_to_yaml} is empty")
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            logger.info(f"Content of {path_to_yaml}: {content}")  # Log the content
            if not content:
                raise ValueError(f"YAML file {path_to_yaml} is empty or improperly formatted.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Cannot extrapolate Box from content in {path_to_yaml}")
    except Exception as e:
        raise e


from typing import Any  # import Any if not already imported

@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """Create directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths.
        verbose (bool, optional): If True, logs each created directory. Defaults to True.
    """
    # Ensure each item is a Path object
    for path in path_to_directories:
        if not isinstance(path, Path):
            raise TypeError(f"Expected 'Path' object, but got {type(path).__name__}")
        
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save data to a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to save in JSON format.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Loaded JSON data as a ConfigBox object.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save data to a binary file.

    Args:
        data (Any): Data to save in binary format.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load data from a binary file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Loaded binary data.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: File size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"

def decode_image(imagestring: str, filename: str):
    """Decode a base64 image string and save it as a file.

    Args:
        imagestring (str): Base64 encoded image string.
        filename (str): Path where the image will be saved.
    """
    imagedata = base64.b64decode(imagestring)
    with open(filename, "wb") as f:
        f.write(imagedata)

def encode_image_to_base64(image_path: str) -> str:
    """Encode an image file to a base64 string.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')
