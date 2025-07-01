
#Here we are going to train differnet differnet models and after training we will try to see what accuracy we are getting  and r score 
#when you are trainng you data we probably think what algorithm we should be apply we should apply every model because
# we dont know which is going to give me good accuracy 

import sys
import os
from dataclasses import dataclass

# Modelling
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models



@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifact","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig() #inside this varibale i wil be able to get that path written over up 


    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info("Split Trainning and test input data")
            x_train, y_train, X_test, y_test= (

             train_array[:,:-1],
             train_array[:,-1],
             test_array[:,:-1],
             test_array[:,-1]

            )


            #Dictionary of Models
            models = {
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor()
                #"XGBRegressor": XGBRegressor(), 
                #"CatBoosting Regressor": CatBoostRegressor(verbose=False),
                #"AdaBoost Regressor": AdaBoostRegressor()
            }

            model_report:dict=evaluate_models(x_train=x_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)


            ##To get best model score from dict
            best_model_name = max(model_report, key=model_report.get)
            ## To get best model name from dict
            best_model = models[best_model_name]
            best_model_score = model_report[best_model_name]


            if best_model_score<0.6:
                raise CustomException("no best model found")
            
            logging.info("Best Model Found on both training and testing data")
             
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,  
                obj=best_model
            ) 

            predicted = best_model.predict(X_test)

            r2 = r2_score(y_test,predicted)
            return r2
        except Exception as e:
            raise CustomException(e,sys)
            
