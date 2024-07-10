from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_folder: Path
    source_url: str
    local_data_path: str
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_folder: Path
    status_file_path: Path
    required_file: list


@dataclass(frozen = True)
class DataTransformationConfig:
    root_folder: Path
    data_path: Path
    tokenizer_name: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_folder: Path
    train_data_path: Path
    model_ckeckpoint: str
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_folder: Path
    model_path: Path
    tokenizer_path: Path
    test_data_path: Path
    evaluations_result: Path