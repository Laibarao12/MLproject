# When working with different teams, data can be collected and stored in various databases like Hadoop, MongoDB, etc.
# As a data scientist, your first task is to read data from these sources.
# Here, we'll start with local data sources (e.g. CSV files).
# This data might be created by the big data team or the cloud team.
# Our aim is to read the data and split it into train/test splits.

import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation

# -----------------------------
# CONFIGURATION CLASS
# -----------------------------
@dataclass
class DataIngestionConfig:
    """
    Holds configuration for paths where data will be saved.
    """
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")


# -----------------------------
# MAIN DATA INGESTION CLASS
# -----------------------------
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method/component.")

        try:
            # READ SOURCE DATA
            df = pd.read_csv(
                'C:/Users/1/Downloads/Data Science Course/Projects/Endtoend Machine Learning project with Azur and AWS Deployment/NoteBook/Data/stud.csv'
            )
            logging.info('Read the dataset as dataframe.')

            # CREATE ARTIFACTS FOLDER IF NEEDED
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # SAVE RAW DATA
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Saved raw data.")

            # TRAIN-TEST SPLIT
            logging.info("Train-test split initiated.")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed.")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
