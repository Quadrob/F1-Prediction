import DB.Database as Database
#data preprocessing
import pandas as pd
#produces a prediction model in the form of an ensemble of weak prediction models, typically decision tree
import xgboost as xgb
#the outcome (dependent variable) has only a limited number of possible values.
#Logistic Regression is used when response variable is categorical in nature.
from sklearn.linear_model import LogisticRegression
#A random forest is a meta estimator that fits a number of decision tree classifiers
#on various sub-samples of the dataset and use averaging to improve the predictive
#accuracy and control over-fitting.
from sklearn.ensemble import RandomForestClassifier
#a discriminative classifier formally defined by a separating hyperplane.
from sklearn.svm import SVC
# Visualising distribution of data.
import matplotlib.pyplot as plt
# Scatter matrix is plotting each of the columns specified against each other column.
from pandas.plotting import scatter_matrix
# Standardising the data.
from sklearn.preprocessing import scale
# Core time library for python
import time
from dateutil.relativedelta import *
import os


def getData():
    # Get data from database and put into dataframes
    races = pd.read_sql_query('''SELECT * FROM races''', Database.DATABASECONNECTION)

    results = pd.read_sql_query('''SELECT * FROM results''', Database.DATABASECONNECTION)

    qualifying = pd.read_sql_query('''SELECT * FROM qualifying''', Database.DATABASECONNECTION)

    driver_standings = pd.read_sql_query('''SELECT * FROM driver_standings''', Database.DATABASECONNECTION)

    constructor_standings = pd.read_sql_query('''SELECT * FROM constructor_standings''', Database.DATABASECONNECTION)

    weather = pd.read_sql_query('''SELECT * FROM weather''', Database.DATABASECONNECTION)

    # Merge all dataframes into one dataframe to make it easier to work with
    # TODO dont exclude country, fastest lap, avg speed for different analysis
    tempDataframe1 = pd.merge(races, weather, how='inner', 
                              on=['raceID', 'season', 'round', 'circuit_id']).drop(['lat', 'long', 'country', 'weather'], axis = 1)
    
    tempDataframe2 = pd.merge(tempDataframe1, results, how='inner', 
                              on=['season', 'round', 'circuit_id', 'url']).drop(['url', 'points', 'status', 'time', 'fastest_lap_rank', 'fastest_lap_time', 'avg_speed'], axis = 1)
    
    tempDataframe3 = pd.merge(tempDataframe2, driver_standings, how='left', 
                              on=['season', 'round', 'driver']) 
    
    tempDataframe4 = pd.merge(tempDataframe3, constructor_standings, how='left', 
                              on=['season', 'round', 'constructor']) #from 1958

    finalDataframe = pd.merge(tempDataframe4, qualifying, how='inner', 
                              on=['season', 'round', 'grid']).drop(['driver_name', 'car', 'qualifying_milliseconds'], axis = 1) # From 1983
    
    # Return the complete dataframe
    return finalDataframe


def calculateDriverAge(final_df):
    final_df['date'] = pd.to_datetime(final_df.date)
    final_df['date_of_birth'] = pd.to_datetime(final_df.date_of_birth)
    final_df['driver_age'] = final_df.apply(lambda x: relativedelta(x['date'], x['date_of_birth']).years, axis=1)
    final_df.drop(['date', 'date_of_birth'], axis = 1, inplace = True)
    return final_df



def main():
    # Get all the necessary data
    final_df = getData()
    # Calculate driver ages
    final_df = calculateDriverAge(final_df)
    # Verify that result of SQL query is stored in the dataframe
    print("Final dataframe shape (rows, columns): " + str(final_df.shape))
    print(final_df.head())
    print(final_df.tail())
    print(final_df.info())
    print(final_df.describe())

    # Save dataframe to a csv
    final_df.to_csv("TestingDataframe", encoding='utf-8')



if __name__ == "__main__":
    # Create database connection
    Database.connectToDatabase()

    # Call the main function to run the application
    main()
    
    # Close db connections
    Database.disconnectFromDatabase()