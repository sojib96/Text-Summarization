from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.conponents.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.verify()