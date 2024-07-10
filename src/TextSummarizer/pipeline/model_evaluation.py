from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.conponents.model_evaluation import ModelEvaluation
from src.TextSummarizer.logging.logger import logging 
class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_component = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_component.evaluate()