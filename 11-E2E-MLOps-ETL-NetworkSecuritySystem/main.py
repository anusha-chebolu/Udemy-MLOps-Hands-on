from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == '__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")
        data_ingestion_aritfact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(data_ingestion_aritfact)


        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_ingestion_aritfact, data_validation_config )
        logging.info("Initiate the data validation")
        data_validation_aritfact = data_validation.initiate_data_validation()
        print(data_validation_aritfact)
        logging.info("Data Validation Completed")


        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(data_validation_aritfact, data_transformation_config )
        logging.info("Initiate the data transformation")
        data_transformation_aritfact = data_transformation.initiate_data_transformation()
        print(data_transformation_aritfact)
        logging.info("Data Transformation Completed")


    except Exception as e:
        raise NetworkSecurityException(e, sys)