# File: src/cnn_classifier/entity/config_manager.py
import yaml
from cnn_classifier.constants import *
from cnn_classifier.utils.common import read_yaml, create_directories
from pathlib import Path
from cnn_classifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig  # Import from the new module

# class ConfigurationManager:
#     def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH) -> None:
#         # Load configurations from YAML files
#         self.config = read_yaml(config_filepath)
#         self.params = read_yaml(params_filepath)

#         # Create artifacts root directory as specified in the config
#         create_directories([Path(self.config["artifacts_root"])])

#     def get_data_ingestion_config(self):
#         config = self.config["data_ingestion"]
#         return DataIngestionConfig(
#             root_dir=Path(config["root_dir"]),
#             source_url=config["source_url"],
#             local_data_file=Path(config["local_data_file"]),
#             unzip_dir=Path(config["unzip_dir"]),
#         )

#     # def get_prepare_base_model_config(self):
#     #     config = self.config["data_ingestion"]["prepare_base_model"]  # Access the nested "prepare_base_model"
#     #     return PrepareBaseModelConfig(
#     #     root_dir=Path(config["root_dir"]),
#     #     base_model_path=Path(config["base_model_path"]),
#     #     updated_base_model_path=Path(config["updated_base_model_path"])
    
    
#     def get_prepare_base_model_config(self):
#         config = self.config["data_ingestion"]["prepare_base_model"]
#         params = self.params

#         # Example code in ConfigurationManager
#         return PrepareBaseModelConfig(
#             root_dir=Path(config["root_dir"]),
#             base_model_path=Path(config["base_model_path"]),
#             updated_base_model_path=Path(config["updated_base_model_path"]),
#             image_size=tuple(params["IMAGE_SIZE"]),
#             weights=params["WEIGHTS"],
#             include_top=params["INCLUDE_TOP"],
#             params_classes=params["CLASSES"],
#             params_learning_rate=params["LEARNING_RATE"]
#         )

    
import yaml
class ConfigurationManager:
    def __init__(self):
        # Load the configuration and parameters (config.yaml and param.yaml)
        self.config = self.load_yaml('d:/project/chicken-fecal-classification_project/config/config.yaml')
        self.params = self.load_yaml('d:/project/chicken-fecal-classification_project/param.yaml')

    def load_yaml(self, file_path: str) -> dict:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config["data_ingestion"]["prepare_base_model"]
        params = self.params

        return PrepareBaseModelConfig(
            root_dir=Path(config["root_dir"]),
            base_model_path=Path(config["base_model_path"]),
            updated_base_model_path=Path(config["updated_base_model_path"]),
            image_size=tuple(params["IMAGE_SIZE"]),
            weights=params["WEIGHTS"],
            include_top=params["INCLUDE_TOP"],
            params_classes=params["CLASSES"],  # Ensure this is passed
            params_learning_rate=params["LEARNING_RATE"]  # Ensure this is passed
        )


    
