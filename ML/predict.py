import pandas as pd
import numpy as np
from ML.model import *
from ML.preparation import *
from sklearn.preprocessing import StandardScaler
import DB.dataPreperation as data
import Pages.Settings as settings


def predictDriverQualifying(queue, season, track, weather):
    np.set_printoptions(precision=5)
    scaler = StandardScaler()
    dataframe = settings.FINALDATAFRAME.copy()
    
    # Prepare training data for model
    train = dataframe
    X_train = train.drop(['driver', 'grid', 'podium', 'fastest_lap_rank', 'qualifying_time', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_points', 'driver_wins', 'driver_standings_pos', 'round', 'raceID'], axis = 1)
    X_train = pd.DataFrame(scaler.fit_transform(X_train), columns = X_train.columns)
    y_train = train.grid

    # Prepare prediction data for model
    test = dataframe.loc[dataframe['driver'].isin(data.getCurrentDrivers())]
    test = test.drop_duplicates(subset=['driver'], keep='last')
    test = emptyDriver(test)
    test = fillDriver(test, season, weather, track)
    X_test = test.drop(['driver', 'grid', 'podium', 'fastest_lap_rank', 'qualifying_time', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_points', 'driver_wins', 'driver_standings_pos', 'round', 'raceID'], axis = 1)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
    y_test = test['driver']
    
    results = performLinearRegressionDriver(X_train, y_train, X_test, y_test)
    #results = performXGBoostTesting(X_train, y_train, X_test, y_test)
    
    calculateQualifyingTimeDifferenceFromResults(results)
    queue.put(results)


def predictDriverRace(queue, season, track, weather):
    predictDriverQualifying(queue, season, track, weather)
    qualifyingResults = queue.get()
    queue.queue.clear()
    
    np.set_printoptions(precision=5)
    scaler = StandardScaler()
    dataframe = settings.FINALDATAFRAME.copy()
    
    # Prepare training data for model
    train = dataframe
    X_train = train.drop(['driver', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_points', 'driver_wins', 'driver_standings_pos', 'round', 'raceID'], axis = 1)
    X_train = pd.DataFrame(scaler.fit_transform(X_train), columns = X_train.columns)
    y_train = train.podium

    # Prepare prediction data for model
    test = dataframe.loc[dataframe['driver'].isin(data.getCurrentDrivers())]
    test = test.drop_duplicates(subset=['driver'], keep='last')
    test = emptyDriver(test)
    test = fillDriver(test, season, weather, track)
    test = fillDriverQualifyingResults(test, qualifyingResults)
    X_test = test.drop(['driver', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_points', 'driver_wins', 'driver_standings_pos', 'round', 'raceID'], axis = 1)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
    y_test = test['driver']
    
    results = performLinearRegressionDriver(X_train, y_train, X_test, y_test)
    #results = performXGBoostTesting(X_train, y_train, X_test, y_test)
    queue.put(results)


def predictDriverChampion(queue, driver, season, points, wins):    
    np.set_printoptions(precision=5)
    scaler = StandardScaler()
    dataframe = settings.FINALDATAFRAME.copy()
    train = pd.DataFrame()
    for season in dataframe.season.unique():
        newDataframe = dataframe.loc[dataframe.season == season]
        train = pd.concat([train, newDataframe.query('round == round.max()')])
        
    # Prepare training data for model
    train = emptyDriverDataframe(train)
    X_train = train.drop(['round', 'driver', 'grid', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_standings_pos', 'raceID'], axis = 1)
    X_train = pd.DataFrame(scaler.fit_transform(X_train), columns = X_train.columns)
    y_train = train.driver_standings_pos

    # Prepare prediction data for model
    test = train.loc[train['driver'].isin(data.getCurrentDrivers())]
    test = test.drop_duplicates(subset=['driver'], keep='last')
    test = fillDriverChampionship(test, driver, season, points, wins)
    X_test = test.drop(['round', 'driver', 'grid', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_standings_pos', 'raceID'], axis = 1)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
    y_test = test['driver']
    
    results = performXGBoostDriver(X_train, y_train, X_test, y_test)
    queue.put(results)


def predictConstructorQualifying(queue, season, track, weather):
    np.set_printoptions(precision=5)
    scaler = StandardScaler()
    dataframe = settings.FINALDATAFRAME.copy()
    
    # Prepare training data for model
    train = dataframe
    X_train = train.drop(['driver', 'grid', 'podium', 'fastest_lap_rank', 'qualifying_time', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_points', 'driver_wins', 'driver_standings_pos', 'round', 'raceID'], axis = 1)
    X_train = pd.DataFrame(scaler.fit_transform(X_train), columns = X_train.columns)
    y_train = train.grid

    # Prepare prediction data for model
    test = dataframe.loc[dataframe['constructor'].isin(data.getCurrentConstructors())]
    test = test.drop_duplicates(subset=['constructor'], keep='last')
    test = emptyConstructor(test)
    test = fillConstructor(test, season, weather, track)
    X_test = test.drop(['driver', 'grid', 'podium', 'fastest_lap_rank', 'qualifying_time', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_points', 'driver_wins', 'driver_standings_pos', 'round', 'raceID'], axis = 1)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
    y_test = test['constructor']
    
    results = performLinearRegressionConstructor(X_train, y_train, X_test, y_test)
    #results = performXGBoostTesting(X_train, y_train, X_test, y_test)
    
    calculateQualifyingTimeDifferenceFromResults(results)
    queue.put(results)


def predictConstructorRace(queue, season, track, weather):
    predictConstructorQualifying(queue, season, track, weather)
    qualifyingResults = queue.get()
    queue.queue.clear()
    
    np.set_printoptions(precision=5)
    scaler = StandardScaler()
    dataframe = settings.FINALDATAFRAME.copy()
    
    # Prepare training data for model
    train = dataframe
    X_train = train.drop(['driver', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_points', 'driver_wins', 'driver_standings_pos', 'round', 'raceID'], axis = 1)
    X_train = pd.DataFrame(scaler.fit_transform(X_train), columns = X_train.columns)
    y_train = train.podium

    # Prepare prediction data for model
    test = dataframe.loc[dataframe['constructor'].isin(data.getCurrentConstructors())]
    test = test.drop_duplicates(subset=['constructor'], keep='last')
    test = emptyConstructor(test)
    test = fillConstructor(test, season, weather, track)
    test = fillConstructorQualifyingResults(test, qualifyingResults)
    X_test = test.drop(['driver', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_points', 'driver_wins', 'driver_standings_pos', 'round', 'raceID'], axis = 1)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
    y_test = test['constructor']
    
    #results = performLinearRegressionDriver(X_train, y_train, X_test, y_test)
    results = performXGBoostConstructor(X_train, y_train, X_test, y_test)
    queue.put(results)


def predictConstructorChampion(queue, constructor, season, points, wins):    
    np.set_printoptions(precision=5)
    scaler = StandardScaler()
    dataframe = settings.FINALDATAFRAME.copy()
    train = pd.DataFrame()
    for season in dataframe.season.unique():
        newDataframe = dataframe.loc[dataframe.season == season]
        train = pd.concat([train, newDataframe.query('round == round.max()')])
        
    # Prepare training data for model
    train = emptyConstructorDataframe(train)
    X_train = train.drop(['round', 'driver', 'grid', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'driver_wins', 'driver_points', 'driver_standings_pos', 'raceID'], axis = 1)
    X_train = pd.DataFrame(scaler.fit_transform(X_train), columns = X_train.columns)
    y_train = train.constructor_standings_pos

    # Prepare prediction data for model
    test = train.loc[train['constructor'].isin(data.getCurrentConstructors())]
    test = test.drop_duplicates(subset=['constructor'], keep='last')
    test = fillConstructorChampionship(test, constructor, season, points, wins)
    X_test = test.drop(['round', 'driver', 'grid', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'driver_wins', 'driver_points', 'driver_standings_pos', 'raceID'], axis = 1)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
    y_test = test['constructor']
    
    results = performXGBoostConstructor(X_train, y_train, X_test, y_test)
    queue.put(results)


def calculateQualifyingTimeDifferenceFromResults(finalDataframe):
    finalDataframe.sort_values(['results'], inplace = True)
    finalDataframe['results_diff'] = finalDataframe.results.diff()
    finalDataframe['results_time'] = finalDataframe.results_diff.cumsum().fillna(0)
    finalDataframe['results_time'] = finalDataframe.results_time.div(10).round(3)
    finalDataframe.drop('results_diff', axis = 1, inplace = True)
    return finalDataframe


def predictDriverPairing(queue):
    np.set_printoptions(precision=5)
    scaler = StandardScaler()
    dataframe = settings.FINALDATAFRAME.copy()
    train = pd.DataFrame()
    for season in dataframe.season.unique():
        newDataframe = dataframe.loc[dataframe.season == season]
        train = pd.concat([train, newDataframe.query('round == round.max()')])
        
    # Prepare training data for model
    train = emptyDriverDataframe(train)
    X_train = train.drop(['round', 'driver', 'grid', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_standings_pos', 'raceID'], axis = 1)
    X_train = pd.DataFrame(scaler.fit_transform(X_train), columns = X_train.columns)
    y_train = train.driver_standings_pos

    # Prepare prediction data for model
    test = train.loc[train['driver'].isin(data.getCurrentDrivers())]
    test = test.drop_duplicates(subset=['driver'], keep='last')
    test = emptyDriverDataframe(test)
    X_test = test.drop(['round', 'driver', 'grid', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'constructor_wins', 'constructor_points', 'driver_standings_pos', 'raceID'], axis = 1)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
    y_test = test['driver']
    
    results = performXGBoostDriver(X_train, y_train, X_test, y_test)
    queue.put(results)


def predictConstructorPairing(queue):    
    np.set_printoptions(precision=5)
    scaler = StandardScaler()
    dataframe = settings.FINALDATAFRAME.copy()
    train = pd.DataFrame()
    for season in dataframe.season.unique():
        newDataframe = dataframe.loc[dataframe.season == season]
        train = pd.concat([train, newDataframe.query('round == round.max()')])
        
    # Prepare training data for model
    train = emptyConstructorDataframe(train)
    X_train = train.drop(['round', 'driver', 'grid', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'driver_wins', 'driver_points', 'driver_standings_pos', 'raceID'], axis = 1)
    X_train = pd.DataFrame(scaler.fit_transform(X_train), columns = X_train.columns)
    y_train = train.constructor_standings_pos

    # Prepare prediction data for model
    test = train.loc[train['constructor'].isin(data.getCurrentConstructors())]
    test = test.drop_duplicates(subset=['constructor'], keep='last')
    test = emptyConstructorDataframe(test)
    X_test = test.drop(['round', 'driver', 'grid', 'podium', 'fastest_lap_rank', 'constructor', 'constructor_standings_pos', 'driver_wins', 'driver_points', 'driver_standings_pos', 'raceID'], axis = 1)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
    y_test = test['constructor']
    
    results = performXGBoostConstructor(X_train, y_train, X_test, y_test)
    results = pd.DataFrame(results)
    completeResults = pd.DataFrame()
    for constructor in results['constructor']:
        newDataframe = results.loc[results['constructor'] == constructor]
        completeResults = pd.concat([completeResults, newDataframe], ignore_index=True)
        completeResults = pd.concat([completeResults, newDataframe], ignore_index=True)
    queue.put(completeResults)




