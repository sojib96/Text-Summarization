from src.TextSummarizer.utils.common import read_yaml, create_directories
from src.TextSummarizer.constants import *
from src.TextSummarizer.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig

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
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_folder])
        data_validation_config = DataValidationConfig(
            root_folder = config.root_folder,
            status_file_path = config.status_file_path,
            required_file=config.required_file
            )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_folder])

        data_transformation_config = DataTransformationConfig(
            root_folder=config.root_folder,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )

        return data_transformation_config
    
    def get_model_training_config(self) -> ModelTrainerConfig:
        config = self.config.data_training
        param = self.param.TrainingArguments

        create_directories([config.root_folder])

        model_training_config = ModelTrainerConfig(
            root_folder=config.root_folder,
            train_data_path = config.train_data_path,
            model_ckeckpoint = config.model_ckeckpoint,
            num_train_epochs = param.num_train_epochs,
            warmup_steps = param.warmup_steps,
            per_device_train_batch_size = param.per_device_train_batch_size,
            weight_decay = param.weight_decay,
            logging_steps = param.logging_steps,
            evaluation_strategy = param.evaluation_strategy,
            eval_steps = param.eval_steps,
            save_steps = param.save_steps,
            gradient_accumulation_steps = param.gradient_accumulation_steps,
        )
        return model_training_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directories([config.root_folder])

        model_evaluation_config = ModelEvaluationConfig(
            root_folder=config.root_folder,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            test_data_path = config.test_data_path,
            evaluations_result = config.evaluations_result
        )

        return model_evaluation_config
