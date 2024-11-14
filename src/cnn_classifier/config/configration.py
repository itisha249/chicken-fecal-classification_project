from cnn_classifier.constants import *
from cnn_classifier.utils.common import read_yaml,create_directories
from cnn_classifier.entity.config_entity import DataIngestionConfig

from pathlib import Path

class configurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
    ) -> None:
        self.config = read_yaml(config_filepath)
        self.param = read_yaml(params_filepath)

        # Debug print to verify structure of self.config
        print("Loaded config:", self.config)  # Check if 'data_ingestion' and 'artifacts_root' keys exist

        # Convert `artifacts_root` to Path object before passing to `create_directories`
        create_directories([Path(self.config["artifacts_root"])])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]  # Use dictionary-style access
        return DataIngestionConfig(
             root_dir=Path(
                 config["root_dir"]),
                 source_url=config["source_url"],
                local_data_file=Path(config["local_data_file"]),
                unzip_dir=Path(config["unzip_dir"]),
           
            
            
        )
