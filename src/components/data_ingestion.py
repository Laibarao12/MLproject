#when we will be working with different people everyone will be collecting data and storing it in difffernet datbases like hadoop, mongoDB, so m as a data scientist will be reading data as first from different data sources
#There are many type of data sources here we will be startig with first with local data sources

#this data source can be created by big data team or from cloud team

#our aim is to read that data split that data ito train test split 
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#i will be using a decorator to use this data ingestionConfig



@dataclass
class DataIngestionConfig: #Configuration = settings or instructions for how your program should work.
    train_data_path: str=os.path.join('artifacts',"train.csv") 
    # i will make sure that i will make artifacct folder so that i will be able to see my output
    # So thi siwll be the path initaiilly we will b givingn to our
    # data ingestion component  and data ingestion component output 
    # will save all the file in tis path, train data will be saved be in this path
    test_data_path: str=os.path.join('artifacts',"test.csv") #similarly for test data
    raw_data_path: str=os.path.join('artifacts',"data.csv")#Raw data
    
    # THese are the inputs that im giving tomy data ingestion component
    # and now data ingestion componnet knows where to save the in train,test adn raw path
    # Why this data ingestion config is called?
class DataIngestion:
     def __init__(self):
          self.ingestion_config= DataIngestionConfig()# this will xonsist of those three paths /values
     def initiate_data_ingestion(self):
          logging.info("Entered the data ingestion mehod or component")
          try:
              df=pd.read_csv('C:/Users/1/Downloads/Data Science Course/Projects/Endtoend Machine Learning project with Azur and AWS Deployment/NoteBook/Data/stud.csv') # we can read from anywhere mongodoba nda nayhing but here we are reading with csv 
              logging.info('Read the dataset as dataframe')
              #lets create artifact folder
              os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

              df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

              logging.info("Tran test split initiated")
              train_Set, test_set = train_test_split(df, test_size=0.2, random_state=42)

              train_Set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
              test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

              logging.info("INgestion of the data is completed")

              return(
                   self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path
              )
              #✅ The purpose of the return in your function is to tell the caller “Here are the paths you will actually use next.”
          except Exception as e:
               raise CustomException(e,sys)
          
if __name__ =="__main__":
     obj = DataIngestion()
     obj.initiate_data_ingestion()         
