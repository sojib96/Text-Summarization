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