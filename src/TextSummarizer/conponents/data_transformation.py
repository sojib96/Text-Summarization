import os
import sys
from src.TextSummarizer.logging.logger import logging
from src.TextSummarizer.exception.exception import CustomException
from src.TextSummarizer.entity.config_entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk


class DataTransformation:

    def __init__(self, config:DataTransformationConfig) -> None:
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def convert_dataset_to_feature(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length=1024, truncation=True)
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        try:
            dataset_samsum = load_from_disk(self.config.data_path)
            logging.info(f"Data loading successful")  
            dataset_samsum_pt = dataset_samsum.map(self.convert_dataset_to_feature, batched = True)
            logging.info(f"Data mapping successful") 
            dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_folder,"samsum_dataset"))
            logging.info(f"Data is saved to disk")
        except Exception as e:
            raise CustomException(e,sys)