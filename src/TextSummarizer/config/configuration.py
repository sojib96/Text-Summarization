from src.TextSummarizer.utils.common import read_yaml, create_directories
from src.TextSummarizer.constants import *
from src.TextSummarizer.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self) -> None:
        config_file_path = CONFIG_FILE_PATH
        param_file_path = PARAMS_FILE_PATH
        self.config = read_yaml(config_file_path)
        self.param = read_yaml(param_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_folder])
        data_ingestion_config = DataIngestionConfig(
            root_folder=config.root_folder,
            source_url=config.source_url,
            local_data_path= config.local_data_path,
            unzip_dir=config.unzip_dir 
        )
        
        return data_ingestion_config

