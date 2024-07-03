from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_folder: Path
    source_url: str
    local_data_path: str
    unzip_dir: Path