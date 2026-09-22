from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

import os
import sys

from networksecurity.constant.training_pipeline import SAVE_MODEL_DIR, MODEL_FILE_NAME

class NetworkModel:
    def __init__(self, processor, model):
        try:
            self.processor = processor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
        
    def predict(self, x):
        try:
            x_transform = self.processor.transform(x)
            y_hat = self.model.predict(x_transform)
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e