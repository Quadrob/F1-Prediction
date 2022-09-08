import sqlite3
from asyncio.windows_events import NULL


# Global variables
DRIVERCONNECTION = NULL


def connectToDriverTable():
    """Create a connection to the drivers table"""
    global DRIVERCONNECTION
    DRIVERCONNECTION = sqlite3.connect('DB/DriverTable.db')


def disconnectToDriverTable():
    """Disconnect from an active connection to the drivers table"""
    global DRIVERCONNECTION
    if (DRIVERCONNECTION != NULL):
        DRIVERCONNECTION.close()
        DRIVERCONNECTION = NULL
        print("Closing driver table connection.")
    else:
        print("There was no active connection to close.")


def createTables():
    """This function can be called to create all the database tables if the do not exist"""
    connectToDriverTable()
    driverCursor = DRIVERCONNECTION.cursor()

    # create the drivers table
    driverCursor.execute('''CREATE TABLE IF NOT EXISTS 
                        drivers(id INTEGER PRIMARY KEY,
                            fullName TEXT,
                            age INTEGER,
                            originContryID INTEGER,
                            firstSeason INTEGER, 
                            currentDriver INTEGER,
                            currentChampPos INTEGER,
                            currentChampPoints REAL,
                            driverTeamID INTEGER,
                            teamContract INTEGER,
                            driverWins INTEGER,
                            podiums INTEGER,
                            poles INTEGER,
                            fastestLap INTEGER,
                            worldChamp INTEGER,
                            DNF INTEGER,
                            avgPoints REAL,
                            totalPoints REAL,
                            totalRaces INTEGER,
                            ratingEA INTEGER,
                            ratingAutosport REAL,
                            ratingReader REAL)''')
    DRIVERCONNECTION.commit()

    # create the team table
    driverCursor.execute('''CREATE TABLE IF NOT EXISTS 
                        teams(id INTEGER PRIMARY KEY,
                            fullName TEXT,
                            age INTEGER,
                            fastestLap INTEGER,
                            worldChamp INTEGER,
                            DNF INTEGER,
                            avgPoints REAL,
                            ratingReader REAL)''')
    DRIVERCONNECTION.commit()

    # create the track table
    driverCursor.execute('''CREATE TABLE IF NOT EXISTS 
                        tracks(id INTEGER PRIMARY KEY,
                            fullName TEXT,
                            age INTEGER,
                            fastestLap INTEGER,
                            worldChamp INTEGER,
                            DNF INTEGER,
                            avgPoints REAL,
                            ratingReader REAL)''')
    DRIVERCONNECTION.commit()

    # create the country + weather table
    driverCursor.execute('''CREATE TABLE IF NOT EXISTS 
                        locations(id INTEGER PRIMARY KEY,
                            fullName TEXT,
                            age INTEGER,
                            fastestLap INTEGER,
                            worldChamp INTEGER,
                            DNF INTEGER,
                            avgPoints REAL,
                            ratingReader REAL)''')
    DRIVERCONNECTION.commit()

    # close connection
    driverCursor.close()
    disconnectToDriverTable()
