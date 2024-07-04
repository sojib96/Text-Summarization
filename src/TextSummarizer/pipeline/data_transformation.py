from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.conponents.data_transformation import DataTransformation


class DataTransformationTrainingPipleline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        DataTransformation(config=data_transformation_config).convert()