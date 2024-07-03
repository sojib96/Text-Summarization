import os
import urllib.request as request
import zipfile
from src.TextSummarizer.logging.logger import logging
from pathlib import Path
from src.TextSummarizer.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_path):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_path
            )
            logging.info(f"{filename} download! with following info: \n{headers}")
        else:
            logging.info(f"File already exists")  

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        try:
            zip_file_path = self.config.local_data_path
            unzip_path = self.config.unzip_dir

            # Ensure the directory exists
            os.makedirs(unzip_path, exist_ok=True)
            print(f"Unzipping '{zip_file_path}' into '{unzip_path}'")

            # Extract the zip file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            print("Extraction complete")

        except Exception as e:
            print(f"An error occurred: {e}")