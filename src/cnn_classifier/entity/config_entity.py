from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path



from cnn_classifier.constants import *
from cnn_classifier.utils.common import read_yaml, create_directories
from cnn_classifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig  # Ensure PrepareBaseModelConfig exists in config_entity
from pathlib import Path

# class configurationManager:
#     def __init__(
#         self,
#         config_filepath=CONFIG_FILE_PATH,
#         params_filepath=PARAMS_FILE_PATH,
#     ) -> None:
#         self.config = read_yaml(config_filepath)
#         self.param = read_yaml(params_filepath)

#         # Debug print to verify structure of self.config
#         print("Loaded config:", self.config)  # Check if 'data_ingestion' and 'artifacts_root' keys exist

#         # Convert `artifacts_root` to Path object before passing to `create_directories`
#         create_directories([Path(self.config["artifacts_root"])])

#     def get_data_ingestion_config(self) -> DataIngestionConfig:
#         config = self.config["data_ingestion"]  # Use dictionary-style access
#         return DataIngestionConfig(
#             root_dir=Path(config["root_dir"]),
#             source_url=config["source_url"],
#             local_data_file=Path(config["local_data_file"]),
#             unzip_dir=Path(config["unzip_dir"]),
#         )
    
#     def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
#         # Ensure 'prepare_base_model' exists in 'data_ingestion' in the config
#         base_model_config = self.config["data_ingestion"]["prepare_base_model"]
#         return PrepareBaseModelConfig(
#             base_model_path=Path(base_model_config["base_model_path"]),
#             updated_base_model_path=Path(base_model_config["updated_base_model_path"]),
#             params_image_size=tuple(self.param["IMAGE_SIZE"]),
#             params_weights=self.param["WEIGHTS"],
#             param_include_top=self.param["INCLUDE_TOP"],
#             params_classes=self.param["CLASSES"],
#             params_learning_rate=self.param["LEARNING_RATE"]
#         )

# src/cnn_classifier/entity/config_entity.py

from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class PrepareBaseModelConfig:
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: tuple
    params_weights: str
    param_include_top: bool
    params_classes: int
    params_learning_rate: float

