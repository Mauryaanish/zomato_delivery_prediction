import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass




## initialize The data ingestion Configuration

@dataclass

class DataIngestionconfig:
    train_data_path = os.path.join('artifacts' , 'train.csv')
    test_data_path = os.path.join('artifacts' , 'test.csv')
    raw_data_path = os.path.join('artifacts' , 'raw.csv')

## create a class for data ingestion

class  DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion Method Starts')

        try:
            df = pd.read_csv(os.path.join('notebooks/data/data', 'zomato_dataset.csv'))
            logging.info('Data Claeing Part Starts')

            # Drop Id and Delivery person id 
            df.drop(labels = ['ID' , 'Delivery_person_ID'] , axis = 1 , inplace = True)

            #replace the nan value with mean

            df['Delivery_person_Age'].mean()
            df['Delivery_person_Age'] = df['Delivery_person_Age'].fillna(value =29)

            # replace the nan value with mean
            df['Delivery_person_Ratings'].mean()
            df['Delivery_person_Ratings'] = df['Delivery_person_Ratings'].fillna(value = 4.6)

            # replace nan value with mode 
            df['Weather_conditions'].mode()
            df["Weather_conditions"] = df['Weather_conditions'].fillna(value = 'Fog')

            # replace nan value with mode
            df['Road_traffic_density'].mode()
            df['Road_traffic_density'] = df['Road_traffic_density'].fillna(value = 'Low')

            # replace nan value with mode
            df["City"].mode()
            df["City"] = df["City"].fillna(value= 'Metropolitian')

            # Replace nan value with mode
            df['multiple_deliveries'].mode()
            df["multiple_deliveries"] = df['multiple_deliveries'].fillna(value=1)

            # replace nan value with mode
            festival_mode = df['Festival'].mode
            df['Festival'] = df['Festival'].fillna(value=festival_mode)

            # This are columns not corelated Target Feature so drop this columns

            df.drop(labels = ['Restaurant_latitude' , 'Restaurant_longitude' , 'Delivery_location_latitude' , 'Delivery_location_longitude'  , 'Order_Date', 'Time_Orderd' ,'Time_Order_picked' ,'Vehicle_condition' , 'Delivery_person_Ratings'] , axis =1 , inplace=True)

            logging.info('Data Cleaing Part Is Done ')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path) , exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path , index=False)

            logging.info('Train Test Split')

            train_set,test_set = train_test_split(df , test_size=0.3 , random_state=40)
            train_set.to_csv(self.ingestion_config.train_data_path , index = False , header = True)
            test_set.to_csv(self.ingestion_config.test_data_path , index = False , header = True)

            logging.info('Ingetion Of data Is complete')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path )



        except Exception as e:
            logging.info('Exception Occured at data Ingetion Stage')
            raise CustomException(e,sys) 

