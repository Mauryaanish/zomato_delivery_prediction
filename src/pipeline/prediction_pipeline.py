import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self , features):
        try:
            preprocessor_path = os.path.join('artifacts' , 'preprocessor.pkl')
            model_path = os.path.join('artifacts' , 'model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)

            return pred

        except Exception as e:
            logging.info('Exception occured in prediction')
            raise CustomException(e,sys)     

class CustomData:

    def __init__(self,
                Delivery_person_Age : int,
                Weather_conditions : str,
                Road_traffic_density : str,
                Type_of_order : str,
                Type_of_vehicle : str,
                multiple_deliveries:int,
                Festival : int,
                City : str):
        
        self. Delivery_person_Age =  Delivery_person_Age
        self.Weather_conditions = Weather_conditions
        self.Road_traffic_density  = Road_traffic_density 
        self.Type_of_order = Type_of_order
        self.Type_of_vehicle = Type_of_vehicle
        self.multiple_deliveries  = multiple_deliveries
        self.Festival = Festival
        self.City = City

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Delivery_person_Age' : [self.Delivery_person_Age ],
                'Weather_conditions' : [self.Weather_conditions],
                'Road_traffic_density' : [self.Road_traffic_density],
                'Type_of_order' : [self.Type_of_order],
                'Type_of_vehicle' : [self.Type_of_vehicle],
                'multiple_deliveries' : [self.multiple_deliveries],
                'Festival' : [self.Festival],
                'City' : [self.City ]
            }

            df = pd.DataFrame(custom_data_input_dict)
            logging.info('DataFrame Gathered')
            return df
        
        except Exception as e:
            logging.info('Exception occured in prediction pipeline')
            raise CustomException(e ,sys)


         
