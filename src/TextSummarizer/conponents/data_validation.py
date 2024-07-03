import os
import sys
from src.TextSummarizer.logging.logger import logging
from src.TextSummarizer.exception.exception import CustomException
from pathlib import Path
from src.TextSummarizer.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def verify(self) -> bool:
        """Verifies the data and returns True if the data is valid else False"""

        try:
            validation_status = False
            all_files = os.listdir(os.path.join('artifacts', 'data_ingestion', 'samsum_dataset'))
            print(all_files)
            for files in all_files:
                if files not in self.config.required_file:
                    validation_status = False
                    with open(self.config.status_file_path, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                        logging.info(f"Validation status upodated")  
                else:
                    validation_status = True
                    with open(self.config.status_file_path, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                        logging.info(f"Validation status upodated")   
            return validation_status
        except Exception as e:
             raise CustomException(e,sys)

        
