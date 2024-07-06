from src.TextSummarizer.logging.logger import logging
from src.TextSummarizer.exception.exception import CustomException
from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.conponents.model_training import ModelTraining
import sys

class ModelTrainingPipleline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            get_training_config = config.get_model_training_config()
            model_training = ModelTraining(config=get_training_config)
            model_training.training_pipeline()
        except Exception as e:
            raise CustomException(e, sys)
        