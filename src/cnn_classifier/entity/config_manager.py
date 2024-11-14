# File: src/cnn_classifier/entity/config_manager.py

from cnn_classifier.constants import *
from cnn_classifier.utils.common import read_yaml, create_directories
from pathlib import Path
from cnn_classifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig  # Import from the new module

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH) -> None:
        # Load configurations from YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Create artifacts root directory as specified in the config
        create_directories([Path(self.config["artifacts_root"])])

    def get_data_ingestion_config(self):
        config = self.config["data_ingestion"]
        return DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            source_url=config["source_url"],
            local_data_file=Path(config["local_data_file"]),
            unzip_dir=Path(config["unzip_dir"]),
        )

    def get_prepare_base_model_config(self):
        config = self.config["prepare_base_model"]
        return PrepareBaseModelConfig(
            root_dir=Path(config["root_dir"]),
            base_model_path=Path(config["base_model_path"]),
            updated_base_model_path=Path(config["updated_base_model_path"])
        )
