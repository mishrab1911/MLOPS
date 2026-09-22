import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig, ModelTrainerConfig
from networksecurity.entity.config_entity import DataTransformationConfig
if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        data_ingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifacts = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed")
        print(dataingestionartifacts)
        
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifacts, data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifacts = data_validation.initiate_data_validation()
        logging.info("Data Validation completed")
        print(data_validation_artifacts)
        
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifacts, data_transformation_config)
        logging.info("Initiate the data transformation")
        data_transformation_artifacts = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation completed")
        print(data_transformation_artifacts)
        
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,
                                     data_transformation_artifact= data_transformation_artifacts)
        logging.info("Initiate the model training")
        model_trainer_artifacts = model_trainer.initiate_model_trainer()
        logging.info("Model Training completed")
        print(model_trainer_artifacts)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)
