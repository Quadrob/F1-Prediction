import sqlite3
from asyncio.windows_events import NULL


# class Database:
#     """A database class which holds all the functions and variables necessary for the database"""

# Global variables
DRIVERCONNECTION = NULL


def connectToDriverTable():
    """Create a connection to the drivers table"""
    global DRIVERCONNECTION
    DRIVERCONNECTION = sqlite3.connect('Database/DriverTable.db')


def disconnectToDriverTable():
    """Disconnect from an active connection to the drivers table"""
    if (DRIVERCONNECTION != NULL):
        DRIVERCONNECTION.close()
        print("Closing driver table connection.")
    else:
        print("There was no active connection to close.")


def createTables():
    """This function can be called to create all the database tables if the do not exist"""
    connectToDriverTable()
    driverCursor = DRIVERCONNECTION.cursor()
    driverCursor.execute('''CREATE TABLE IF NOT EXISTS 
                        drivers(id INTEGER PRIMARY KEY,
                            firstName TEXT, 
                            lastName TEXT, 
                            age INTEGER,
                            originContryID INTEGER,
                            firstSeason INTEGER, 
                            currentDriver INTEGER,
                            driverTeamID INTEGER
                            wins INTEGER,
                            podiums INTEGER,
                            poles INTEGER,
                            fastestLap INTEGER,
                            worldChamp INTEGER,
                            avgPoints REAL,
                            totalPoints REAL,
                            totalRaces INTEGER,
                            rating INTEGER)''')
    driverCursor.close()
    disconnectToDriverTable()


#driver season table
#county table
#team table
