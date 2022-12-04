# make child or parent dir available eg: make parent dir available replace 'dataCollection' with '..'
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], 'dataCollection'))
import numpy
import pandas as pd

import constructorStandings, driverStandings, qualifying, races, results, weather
import Database


def dataCollection():
    """ This is the main function to fetch all the required data for the application. """
    print("Be prepared, the data collection can take really long due to the amount of data that needs to be collected and formatted!")
    
    # Setup DB Connection
    Database.connectToDatabase()

    # Fetch and populate races table
    races.raceDataCollection(Database.DATABASECONNECTION)
    races_dataframe = pd.read_sql_query('''SELECT * FROM races''', Database.DATABASECONNECTION)
    
    # append the number of rounds of each season from the races dataframe
    rounds = []
    for year in numpy.array(races_dataframe.season.unique()):
        rounds.append([year, list(races_dataframe[races_dataframe.season == year]['round'])])

    # Fetch and populate results table
    results.resultsDataCollection(Database.DATABASECONNECTION)
    
    # Fetch and populate driver standings table
    driverStandings.driverDataCollection(Database.DATABASECONNECTION, rounds)
    
    # Fetch and populate weather table
    weather.weatherDataCollection(Database.DATABASECONNECTION, races_dataframe)

    # Fetch and populate constructor standings table
    constructorStandings.constructorDataCollection(Database.DATABASECONNECTION, rounds)
    
    # Fetch and populate qualifying table
    qualifying.qualifyingDataCollection(Database.DATABASECONNECTION)

    # Close and empty DB connection
    Database.disconnectFromDatabase()


# TODO delete temp run file
dataCollection()