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
# Split data into testing and training data
from sklearn.model_selection import train_test_split


# Get data
Database.connectToDatabase()
drivers = pd.read_sql_query(
    '''SELECT * FROM drivers d WHERE d.currentDriver = 1''', Database.DATABASECONNECTION)
tracks = pd.read_sql_query(
    '''SELECT * FROM tracks''', Database.DATABASECONNECTION)
trackResults = pd.read_sql_query(
    '''SELECT * FROM trackResults tr WHERE tr.pole IN (SELECT d.fullName FROM drivers d)''', Database.DATABASECONNECTION)
teams = pd.read_sql_query(
    '''SELECT * FROM teams t WHERE t.currentConstructor = 1''', Database.DATABASECONNECTION)
f1DataPole = pd.read_sql_query('''SELECT * FROM trackResults tr 
                            INNER JOIN drivers d
                            ON d.fullName = tr.pole
                            INNER JOIN teams tm
                            ON tm.id = d.driverTeamID
                            INNER JOIN tracks t
                            ON t.fullName = tr.fullName
                            INNER JOIN countries c
                            ON t.country = c.fullName
                            INNER JOIN weather w
                            ON w.id = c.weatherID''', Database.DATABASECONNECTION)


# Fix data columns
f1DataPole.columns.values[57] = "delete"
f1DataPole.columns.values[55] = "delete"
f1DataPole.columns.values[54] = "countryID"
f1DataPole.columns.values[51] = "delete"
f1DataPole.columns.values[50] = "delete"
f1DataPole.columns.values[49] = "trackID"
f1DataPole.columns.values[33] = "delete"
f1DataPole.columns.values[31] = "delete"
f1DataPole.columns.values[30] = "delete"
f1DataPole.columns.values[29] = "teamID"
f1DataPole.columns.values[12] = "delete"
f1DataPole.columns.values[10] = "delete"
f1DataPole.columns.values[9] = "delete"
f1DataPole.columns.values[8] = "delete"
f1DataPole.columns.values[7] = "driverID"
f1DataPole.columns.values[6] = "delete"
f1DataPole.columns.values[5] = "delete"
f1DataPole.columns.values[4] = "delete"
f1DataPole.columns.values[3] = "delete"
f1DataPole.columns.values[1] = "delete"
f1DataPole.columns.values[0] = "resultID"
f1DataPole.drop(
    ['weatherDescription', 'summary', 'delete'], axis='columns', inplace=True)
f1DataPole.sort_values(by='eventYear', ascending=True, inplace=True)


print(str(f1DataPole))
print(f1DataPole.head())
print(f1DataPole.describe())
print(f1DataPole.info())


# start preparing data to make predictions
x_all = f1DataPole.drop('driverID', axis='columns')
y_all = f1DataPole['driverID']
# print(y_all.head)


#Center to the mean and component wise scale to unit variance
columns = [['seasons', 'currentChampPoints', 'driverTeamID',
           'fastestLap', 'totalRaces', 'ratingF1Man22', 'ratingEA']]
for col in columns:
    x_all[col] = scale(x_all[col])
    # print(x_all[col])


# Shuffle and split the dataset into training and testing set.
x_train, x_test, y_train, y_test = train_test_split(x_all, y_all,
                                                    test_size=0.1,
                                                    random_state=42)
# print(str(y_test) + " == vs == " + str(y_all))


#
#
#
#
Database.disconnectFromDatabase()
