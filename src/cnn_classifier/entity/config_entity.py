# File: src/cnn_classifier/entity/config_entities.py

from pathlib import Path

class DataIngestionConfig:
    def __init__(self, root_dir: Path, source_url: str, local_data_file: Path, unzip_dir: Path) -> None:
        self.root_dir = root_dir
        self.source_url = source_url
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir


class PrepareBaseModelConfig:
    def __init__(
        self,
        root_dir: Path,
        base_model_path: Path,
        updated_base_model_path: Path,
        image_size: tuple,  # (224, 224, 3)
        weights: str,       # 'imagenet'
        include_top: bool,  # False
        params_classes: int,     # number of classes, e.g., 2
        params_learning_rate: float  # learning rate, e.g., 0.01
    ) -> None:
        self.root_dir = root_dir
        self.base_model_path = base_model_path
        self.updated_base_model_path = updated_base_model_path
        self.image_size = image_size
        self.weights = weights
        self.include_top = include_top
        self.params_classes = params_classes
        self.params_learning_rate = params_learning_rate
