# make child or parent dir available eg: make parent dir available replace 'dataCollection' with '..'
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], 'dataCollection'))

import constructorStandings, driverStandings, qualifying, races, results, weather
import Database


def dataCollection():
    """ This is the main function to fetch all the required data for the application. """
    # Setup DB Connection
    Database.connectToDatabase()

    # Fetch and populate races table
    rounds = races.raceDataCollection(Database.DATABASECONNECTION)
    
    # Fetch and populate results table
    results.resultsDataCollection(Database.DATABASECONNECTION, rounds)
    
    # Fetch and populate driver standings table
    driverStandings.driverDataCollection(Database.DATABASECONNECTION, rounds)

    # Close and empty DB connection
    Database.disconnectFromDatabase()


# temp run file
dataCollection()
# Temp 
# pd.read_sql('select * from races;', DATABASECONNECTION)