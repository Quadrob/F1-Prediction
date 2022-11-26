import DB.Database as Database
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from dateutil.relativedelta import *


def getData():
    # Get data from database and put into dataframes
    races = pd.read_sql_query('''SELECT * FROM races''', Database.DATABASECONNECTION)

    results = pd.read_sql_query('''SELECT * FROM results''', Database.DATABASECONNECTION)

    qualifying = pd.read_sql_query('''SELECT * FROM qualifying''', Database.DATABASECONNECTION)

    driver_standings = pd.read_sql_query('''SELECT * FROM driver_standings''', Database.DATABASECONNECTION)

    constructor_standings = pd.read_sql_query('''SELECT * FROM constructor_standings''', Database.DATABASECONNECTION)

    weather = pd.read_sql_query('''SELECT * FROM weather''', Database.DATABASECONNECTION)

    # Merge all dataframes into one dataframe to make it easier to work with
    tempDataframe1 = pd.merge(races, weather, how='inner', 
                              on=['raceID', 'season', 'round', 'circuit_id']).drop(['lat', 'long', 'weather'], axis = 1)
    
    tempDataframe2 = pd.merge(tempDataframe1, results, how='inner', 
                              on=['season', 'round', 'circuit_id', 'url']).drop(['url', 'points',  'time', 'status', 'driver_full_name', 'fastest_lap_time', 'avg_speed'], axis = 1)
    
    tempDataframe3 = pd.merge(tempDataframe2, driver_standings, how='left', 
                              on=['season', 'round', 'driver']) 
    
    tempDataframe4 = pd.merge(tempDataframe3, constructor_standings, how='left', 
                              on=['season', 'round', 'constructor']) #from 1958

    finalDataframe = pd.merge(tempDataframe4, qualifying, how='inner', 
                              on=['season', 'round', 'grid']).drop(['driver_name', 'car', 'weatherID', 'resultID', 'driver_standingsID', 'constructor_standingsID', 'qualifyingID'], axis = 1) # From 1983
    
    # Return the complete dataframe
    return finalDataframe


def getCurrentDrivers():
    year = datetime.date.today().year
    Database.connectToDatabase()
    cursor = Database.DATABASECONNECTION.cursor()
    cursor.execute('''SELECT driver FROM driver_standings WHERE season=?''', (year,))
    driver_standings = pd.DataFrame({"driver": cursor.fetchall()})
    Database.disconnectFromDatabase()
    currentDrivers = driver_standings.driver.unique()
    driverArr = []
    for driver in currentDrivers:
        driverArr.append(driver[0])
    return driverArr


def getCurrentConstructors():
    year = datetime.date.today().year
    Database.connectToDatabase()
    cursor = Database.DATABASECONNECTION.cursor()
    cursor.execute('''SELECT constructor FROM constructor_standings WHERE season=?''', (year,))
    constructor_standings = pd.DataFrame({"constructor": cursor.fetchall()})
    Database.disconnectFromDatabase()
    currentConstructors = constructor_standings.constructor.unique()
    constructorArr = []
    for constructor in currentConstructors:
        constructorArr.append(constructor[0])
    return constructorArr


def getAllCircuitsAndCountry():
    Database.connectToDatabase()
    races = pd.read_sql_query('''SELECT * FROM races''', Database.DATABASECONNECTION)
    Database.disconnectFromDatabase()
    uniqueCircuits = races.drop_duplicates(['circuit_id'])
    return uniqueCircuits[['circuit_id', 'country']]


def getTracks():
    Database.connectToDatabase()
    cursor = Database.DATABASECONNECTION.cursor()
    cursor.execute('''SELECT circuit_id FROM races''')
    races = pd.DataFrame({"track": cursor.fetchall()})
    Database.disconnectFromDatabase()
    tracks = races.track.unique()
    trackArr = []
    for driver in tracks:
        trackArr.append(driver[0])
    return trackArr


def calculateDriverAge(finalDataframe):
    finalDataframe['date'] = pd.to_datetime(finalDataframe.date)
    finalDataframe['date_of_birth'] = pd.to_datetime(finalDataframe.date_of_birth)
    finalDataframe['driver_age'] = finalDataframe.apply(lambda x: relativedelta(x['date'], x['date_of_birth']).years, axis=1)
    finalDataframe.drop(['date', 'date_of_birth'], axis = 1, inplace = True)
    return finalDataframe


def removeOrFillNulls(finalDataframe):
    for column in ['driver_points', 
                   'driver_wins', 
                   'driver_standings_pos', 
                   'constructor_points', 
                   'constructor_wins', 
                   'constructor_standings_pos',
                   'weather_warm',
                   'weather_cold',
                   'weather_dry',
                   'weather_wet',
                   'weather_cloudy',
                   'fastest_lap_rank']:
        try:
            finalDataframe[column].fillna(0, inplace = True)
            finalDataframe[column] = finalDataframe[column].map(lambda x: int(x))
        except Exception as e:
            print('Error filling nulls for column: ' + str(column) + ' because of error: ' + str(e))
        
    finalDataframe.dropna(inplace = True )
    return finalDataframe


def convertToBooleans(finalDataframe):
    for column in ['weather_warm', 'weather_cold','weather_dry', 'weather_wet', 'weather_cloudy']:
        finalDataframe[column] = finalDataframe[column].map(lambda x: bool(x))
    
    return finalDataframe


def getSecondsFromMinutes(timeString):
    if (str(timeString) != "00.000" and ":" in str(timeString)):
        timeInMins = str(timeString).split(':')
        timeInSecs = (float(timeInMins[0]) * 60) + float(timeInMins[1])
        return float(timeInSecs)
    elif (str(timeString) != "00.000" and ":" not in str(timeString)):
        return float(timeString)
    else:
        return 0

            
def calculateQualifyingTimeDifference(finalDataframe):
    finalDataframe['qualifying_time'] = finalDataframe.qualifying_time.map(lambda x: getSecondsFromMinutes(x))
    finalDataframe = finalDataframe[finalDataframe['qualifying_time'] != 0]
    finalDataframe.sort_values(['season', 'round', 'grid'], inplace = True)
    finalDataframe['qualifying_time_diff'] = finalDataframe.groupby(['season', 'round']).qualifying_time.diff()
    finalDataframe['qualifying_time'] = finalDataframe.groupby(['season', 'round']).qualifying_time_diff.cumsum().fillna(0)
    finalDataframe.drop('qualifying_time_diff', axis = 1, inplace = True)
    return finalDataframe

            
def calculateAverageSpeedDifference(finalDataframe):
    finalDataframe['avg_speed'] = finalDataframe.avg_speed.map(lambda x: float(x))
    finalDataframe = finalDataframe[finalDataframe['avg_speed'] != 0]
    finalDataframe.sort_values(['season', 'round', 'grid'], inplace = True)
    finalDataframe['avg_speed_diff'] = finalDataframe.groupby(['season', 'round']).avg_speed.diff()
    finalDataframe['avg_speed'] = finalDataframe.groupby(['season', 'round']).avg_speed_diff.cumsum().fillna(0)
    finalDataframe.drop('avg_speed_diff', axis = 1, inplace = True)
    return finalDataframe


def getDummyValues(finalDataframe):
    finalDataframe['driverFeature'] = finalDataframe['driver']
    finalDataframe['constructorFeature'] = finalDataframe['constructor']
    dummyDataframe = pd.get_dummies(finalDataframe, columns = ['driverFeature', 'circuit_id', 'country', 'nationality', 'constructorFeature', 'constructor_nationality'] )
    for column in dummyDataframe.columns: 
        if 'driverFeature' in column and dummyDataframe[column].sum() < 25:
            dummyDataframe.drop(column, axis = 1, inplace = True)
            
        if 'nationality' in column and dummyDataframe[column].sum() < 120:
            dummyDataframe.drop(column, axis = 1, inplace = True)
            
        elif 'constructorFeature' in column and dummyDataframe[column].sum() < 120:
            dummyDataframe.drop(column, axis = 1, inplace = True)
            
        elif 'circuit_id' in column and dummyDataframe[column].sum() < 60:
            dummyDataframe.drop(column, axis = 1, inplace = True)
            
        elif 'country' in column and dummyDataframe[column].sum() < 100:
            dummyDataframe.drop(column, axis = 1, inplace = True)
            
        elif 'constructor_nationality' in column and dummyDataframe[column].sum() < 120:
            dummyDataframe.drop(column, axis = 1, inplace = True)
        
        else:
            pass
        
    return dummyDataframe


def dataPreperation():
    # Set global configurations
    Database.connectToDatabase()
    np.set_printoptions(precision=5)
    # Get all the necessary data
    finalDataframe = getData()
    # Calculate driver ages
    finalDataframe = calculateDriverAge(finalDataframe)
    # Fill or remove nulls from dataset
    finalDataframe = removeOrFillNulls(finalDataframe)
    # Convert weather numbers to booleans
    finalDataframe = convertToBooleans(finalDataframe)
    # Calculate qualifying time differences
    finalDataframe = calculateQualifyingTimeDifference(finalDataframe)
    # Get dummy values and drop non-significante variables
    finalDataframe = getDummyValues(finalDataframe)
    # Close db connections
    Database.disconnectFromDatabase()
    # Return final dataframe
    return finalDataframe


def dataframeLogger(dataframe):
    print("Dataframe shape (rows, columns): " + str(dataframe.shape))
    print(dataframe.head())
    print(dataframe.tail())
    print(dataframe.info())
    print(dataframe.describe())


def saveDataframeToCSV(dataframe, filePath):
    try:
        dataframe.to_csv(filePath)
    except Exception as e:
        print(str(e))


def plotBarGraph(dataframe, picturePath):
    plt.bar(dataframe.index, dataframe.score, color ='maroon', width = 0.4)    
    plt.xlabel("Machine Learning Model")
    plt.ylabel("Success Percentage %")
    plt.title("Comparison Of Machine Learning Models")
    plt.savefig(picturePath)
    plt.show()


    