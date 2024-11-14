# src/cnn_classifier/config/config_manager.py
from cnn_classifier.constants import *
from cnn_classifier.utils.common import read_yaml, create_directories
from cnn_classifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig
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
        print("Loaded config:", self.config)

        # Convert `artifacts_root` to Path object before passing to `create_directories`
        create_directories([Path(self.config["artifacts_root"])])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]
        return DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            source_url=config["source_url"],
            local_data_file=Path(config["local_data_file"]),
            unzip_dir=Path(config["unzip_dir"]),
        )
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        base_model_config = self.config["data_ingestion"]["prepare_base_model"]
        return PrepareBaseModelConfig(
            base_model_path=Path(base_model_config["base_model_path"]),
            updated_base_model_path=Path(base_model_config["updated_base_model_path"]),
            params_image_size=tuple(self.param["IMAGE_SIZE"]),
            params_weights=self.param["WEIGHTS"],
            param_include_top=self.param["INCLUDE_TOP"],
            params_classes=self.param["CLASSES"],
            params_learning_rate=self.param["LEARNING_RATE"]
        )
