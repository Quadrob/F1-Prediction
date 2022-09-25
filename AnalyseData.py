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


# Get data
Database.connectToDatabase()
drivers = pd.read_sql_query('''SELECT * FROM drivers d
                            INNER JOIN trackResults tr
                            ON d.fullName = tr.winner''',
                            Database.DATABASECONNECTION)
tracks = pd.read_sql_query(
    '''SELECT * FROM tracks''', Database.DATABASECONNECTION)
trackResults = pd.read_sql_query(
    '''SELECT * FROM trackResults''', Database.DATABASECONNECTION)
teams = pd.read_sql_query(
    '''SELECT * FROM teams t WHERE t.currentConstructor = 1''', Database.DATABASECONNECTION)

# Verify that result of SQL query is stored in the dataframe
print(drivers.head())
print(tracks.head())
print(teams.head())
print(drivers.info())
print(drivers.describe())

# Number of races
numOfRaces = drivers.shape[0]

# Number of factors/features
numOfFactors = drivers.shape[1] - 1

# Number of wins by driver
ham = len(drivers[drivers.winner == 'Lewis Hamilton'])
max = len(drivers[drivers.winner == 'Max Verstappen'])
rus = len(drivers[drivers.winner == 'George Russell'])

# calculate win rate for current driver
print("Hamilton win rate: " + str((float(ham) / float(numOfRaces)) * 100) + "%")
print("Verstappen win rate: " + str((float(max) / float(numOfRaces)) * 100) + "%")
print("Russell win rate: " + str((float(rus) / float(numOfRaces)) * 100) + "%")

# Scatter plots show how much one variable is affected by another.
# The relationship between two variables is called their correlation negative vs positive correlation
scatter_matrix(drivers[['seasons', 'currentChampPos', 'currentChampPoints', 'laps', 'lapsLead',
               'driverTeamID', 'driverWins', 'podiums', 'poles', 'fastestLap', 'worldChamp', 'DNF',
                        'avgPoints', 'totalPoints', 'totalRaces', 'ratingF1Man22', 'ratingEA']], figsize=(10, 10))

# add a column to dataframe
f1_data = drivers
f1_data["wonFromPole"] = tracks['wonFromPole']
scatter_matrix(f1_data[['seasons', 'currentChampPoints', 'lapsLead', 'driverTeamID', 'driverWins', 'podiums', 'poles',
               'fastestLap', 'worldChamp', 'DNF', 'totalPoints', 'totalRaces', 'ratingF1Man22', 'ratingEA', 'wonFromPole']], figsize=(10, 10))

# Show scatter matrices
plt.show()

# Close db connections
Database.disconnectFromDatabase()
