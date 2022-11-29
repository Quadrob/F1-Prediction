import pandas as pd
import Pages.Settings as settings


def emptyDriverDataframe(dataframe):
    for column in dataframe:
        if column.startswith('weather_') or column.startswith('circuit_id_') or column.startswith('country_'):
            dataframe.drop(column, axis = 1, inplace = True)
    return dataframe

def emptyDriver(dataframe):
    for column in dataframe:
        if column.startswith('weather_'):
            dataframe.loc[:, column] = False
        if column.startswith('circuit_id_'):
            dataframe.loc[:, column] = 0
        if column.startswith('country_'):
            dataframe.loc[:, column] = 0
    return dataframe

def fillDriver(dataframe, season, weather, circuit):
    country = settings.CIRCUITCOUNTRYDICT.loc[settings.CIRCUITCOUNTRYDICT['circuit_id'] == circuit]['country'].values[0]
    for column in dataframe:
        if 'season' in column:
            dataframe.loc[:, column] = season
        if str(weather).lower() in column:
            dataframe.loc[:, column] = True
        if str(circuit) in column:
            dataframe.loc[:, column] = 1
        if str(country) in column:
            dataframe.loc[:, column] = 1
    return dataframe

def fillDriverQualifyingResults(dataframe, qualifyingResults):
    dataframe = dataframe.drop(['grid', 'qualifying_time'], axis=1)
    dataframe = pd.merge(dataframe,qualifyingResults[['predicted','results_time', 'driver']],on='driver', how='left')
    dataframe = dataframe.rename(columns = {'predicted':'grid'})
    dataframe = dataframe.rename(columns = {'results_time':'qualifying_time'})
    return dataframe

def fillDriverChampionship(dataframe, driver, season, points, wins):
    for column in dataframe:
        if 'season' in column:
            dataframe.loc[:, column] = season

    dataframe.loc[dataframe['driver'] == driver, ['driver_points']] = points
    dataframe.loc[dataframe['driver'] == driver, ['driver_wins']] = wins
    return dataframe
    
def emptyConstructorDataframe(dataframe):
    for column in dataframe:
        if column.startswith('weather_') or column.startswith('circuit_id_') or column.startswith('country_'):
            dataframe.drop(column, axis = 1, inplace = True)
    return dataframe

def emptyConstructor(dataframe):
    for column in dataframe:
        if column.startswith('weather_'):
            dataframe.loc[:, column] = False
        if column.startswith('circuit_id_'):
            dataframe.loc[:, column] = 0
        if column.startswith('country_'):
            dataframe.loc[:, column] = 0
    return dataframe

def fillConstructor(dataframe, season, weather, circuit):
    country = settings.CIRCUITCOUNTRYDICT.loc[settings.CIRCUITCOUNTRYDICT['circuit_id'] == circuit]['country'].values[0]
    for column in dataframe:
        if 'season' in column:
            dataframe.loc[:, column] = season
        if str(weather).lower() in column:
            dataframe.loc[:, column] = True
        if str(circuit) in column:
            dataframe.loc[:, column] = 1
        if str(country) in column:
            dataframe.loc[:, column] = 1
    return dataframe

def fillConstructorQualifyingResults(dataframe, qualifyingResults):
    dataframe = dataframe.drop(['grid', 'qualifying_time'], axis=1)
    dataframe = pd.merge(dataframe,qualifyingResults[['predicted','results_time', 'constructor']],on='constructor', how='left')
    dataframe = dataframe.rename(columns = {'predicted':'grid'})
    dataframe = dataframe.rename(columns = {'results_time':'qualifying_time'})
    return dataframe

def fillConstructorChampionship(dataframe, constructor, season, points, wins):
    for column in dataframe:
        if 'season' in column:
            dataframe.loc[:, column] = season

    dataframe.loc[dataframe['constructor'] == constructor, ['constructor_points']] = points
    dataframe.loc[dataframe['constructor'] == constructor, ['constructor_wins']] = wins
    return dataframe






