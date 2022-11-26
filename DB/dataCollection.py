# make child or parent dir available eg: make parent dir available replace 'dataCollection' with '..'
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], 'dataCollection'))
import numpy

import constructorStandings, driverStandings, qualifying, races, results, weather
import Database


def dataCollection():
    """ This is the main function to fetch all the required data for the application. """
    # Setup DB Connection
    Database.connectToDatabase()

    # Fetch and populate races table
    races_dataframe = races.raceDataCollection(Database.DATABASECONNECTION)
    
    # append the number of rounds of each season from the races dataframe
    rounds = []
    for year in numpy.array(races_dataframe.season.unique()):
        rounds.append([year, list(races_dataframe[races_dataframe.season == year]['round'])])

    # Fetch and populate results table
    results.resultsDataCollection(Database.DATABASECONNECTION, rounds)
    
    # Fetch and populate driver standings table
    driverStandings.driverDataCollection(Database.DATABASECONNECTION, rounds)
    
    # Fetch and populate constructor standings table
    constructorStandings.constructorDataCollection(Database.DATABASECONNECTION, rounds)
    
    # Fetch and populate qualifying table
    qualifying.qualifyingDataCollection(Database.DATABASECONNECTION)
    
    # Fetch and populate weather table
    weather.weatherDataCollection(Database.DATABASECONNECTION, races_dataframe)

    # Close and empty DB connection
    Database.disconnectFromDatabase()


# temp run file
dataCollection()
# Temp 
# pd.read_sql('select * from races;', DATABASECONNECTION)