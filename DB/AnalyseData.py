import warnings
warnings.filterwarnings("ignore", "(?s).*MATPLOTLIBDATA.*", category=UserWarning)

import Database
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
import os

# Create database connection
Database.connectToDatabase()

# Get data from database and put into dataframes
races = pd.read_sql_query('''SELECT * FROM races''', Database.DATABASECONNECTION)

results = pd.read_sql_query('''SELECT * FROM results''', Database.DATABASECONNECTION)

qualifying = pd.read_sql_query('''SELECT * FROM qualifying''', Database.DATABASECONNECTION)

driver_standings = pd.read_sql_query('''SELECT * FROM driver_standings''', Database.DATABASECONNECTION)

constructor_standings = pd.read_sql_query('''SELECT * FROM constructor_standings''', Database.DATABASECONNECTION)

weather = pd.read_sql_query('''SELECT * FROM weather''', Database.DATABASECONNECTION)


# Verify that result of SQL query is stored in the dataframe
print("Races dataframe shape (rows, columns): " + str(races.shape))
print(races.head())
print(races.tail())
print(races.info())
print(races.describe())

# Number of races
numOfRaces = races.shape[0]

# Number of wins by driver
tempDataframe = pd.merge(races, results, how='inner', on=['season', 'round', 'circuit_id']).drop(['url', 'points', 'status', 'time'], axis = 1)
print(str(tempDataframe.info()))

# driver wins
max, ham, lec, rus, other = 0, 0, 0, 0, 0

for index, result in tempDataframe.iterrows():
    if (str(result['driver']) == 'max_verstappen' and str(result['podium']) == '1'):
        max += 1
    elif (str(result['driver']) == 'hamilton' and str(result['podium']) == '1'):
        ham += 1
    elif (str(result['driver']) == 'leclerc' and str(result['podium']) == '1'):
        lec += 1
    elif (str(result['driver']) == 'russell' and str(result['podium']) == '1'):
        rus += 1
    elif (str(result['podium']) == '1'):
        other += 1

# calculate win rate for current driver
print("Hamilton win rate: " + str((float(ham) / float(numOfRaces)) * 100) + "%")
print("Verstappen win rate: " + str((float(max) / float(numOfRaces)) * 100) + "%")
print("Russell win rate: " + str((float(rus) / float(numOfRaces)) * 100) + "%")
print("Leclerc win rate: " + str((float(lec) / float(numOfRaces)) * 100) + "%")
print("Other drivers win rate: " + str((float(other) / float(numOfRaces)) * 100) + "%")

# Scatter plots show how much one variable is affected by another.
# The relationship between two variables is called their correlation negative vs positive correlation
scatter_matrix(tempDataframe[['grid', 'podium', 'fastest_lap_rank', 'fastest_lap_time', 'avg_speed']], figsize=(10, 10))

# Show scatter matrices and create an image
plt.ion()
plt.show()
print("\nPress Enter to Continue")
plt.waitforbuttonpress(0)
output_path = os.path.dirname(__file__)
plt.savefig(str(output_path) + str('\\..\\DataAnalysisImages\\Analysisplot.png'))
print("\nSaved Graph to: ../DataAnalysisImages/Analysisplot.png\n")
plt.close('all')

# Close db connections
Database.disconnectFromDatabase()
