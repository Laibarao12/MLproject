import sys
import os

import numpy as np
import pandas as pd
import dill ## used for saving the pkl file another way
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

##will save the pkl file 
def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys)        
    

def evaluate_models(x_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(x_train, y_train)

            best_model = gs.best_estimator_

            y_train_pred = best_model.predict(x_train)
            y_test_pred = best_model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            model_name = list(models.keys())[i]
            report[model_name] = test_model_score

            # replace the unfitted model with the best estimator
            models[model_name] = best_model


        return report

    except Exception as e:
        raise CustomException(e, sys)
