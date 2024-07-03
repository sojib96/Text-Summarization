import os
import sys
from box.exceptions import BoxValueError
import yaml
from src.TextSummarizer.logging.logger import logging
from src.TextSummarizer.exception.exception import CustomException
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """Reads yaml file and returns a ConfigBox object"""

    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def create_directories(paths:list, verbose=True):
    """Creates directories in the given path list"""

    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")