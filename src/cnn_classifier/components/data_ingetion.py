import os
import urllib.request as request
import zipfile 
from cnn_classifier import logger
from cnn_classifier.utils.common import get_size
from cnn_classifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


import os
import zipfile
from pathlib import Path
import logging

# Assuming the logger is configured
logger = logging.getLogger(__name__)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(self.config.source_url, self.config.local_data_file)
            logger.info(f"{filename} downloaded with the following info:\n{headers}")
        else:
            file_size = os.path.getsize(self.config.local_data_file)
            logger.info(f"File already exists of size: {file_size} bytes")

    def extract_zip_file(self):
        """
        Extract the zip file into the data directory.
        """
        # Ensure `unzip_path` is a Path object
        unzip_path = Path(self.config.unzip_dir)  # Explicitly cast to Path object
        print(f"Unzip path: {unzip_path}")  # Debug print
        print(f"Local data file: {self.config.local_data_file}")  # Debug print

        # Create the directory if it doesn't exist
        os.makedirs(unzip_path, exist_ok=True)
        print(f"Directory created or already exists at: {unzip_path}")  # Debug print

        # Check if the local data file exists before extracting
        if not os.path.exists(self.config.local_data_file):
            print(f"File does not exist: {self.config.local_data_file}")
            return

        try:
            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)  # Extract all files into the unzip path
                logger.info(f"Extracted zip file to: {unzip_path}")
        except Exception as e:
            print(f"Error during extraction: {e}")
            raise e  # Reraise exception to be caught elsewhere
