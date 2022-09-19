import sqlite3

DATABASECONNECTION = None


def connectToDatabase():
    """Create a connection to the database"""
    global DATABASECONNECTION
    DATABASECONNECTION = sqlite3.connect('DB/F1_DB.db')


def disconnectFromDatabase():
    """Disconnect from an active connection to the database"""
    global DATABASECONNECTION
    if (DATABASECONNECTION != None):
        DATABASECONNECTION.close()
        DATABASECONNECTION = None
        print("Closing database connection!")
    else:
        print("There was no active connection to close.")


def insertWeatherConditions(databaseCursor):
    """This function can be called to populate the different weather conditions"""

def createTablesIfNotExist():
    """This function can be called to create all the database tables if they do not exist"""
    connectToDatabase()
    databaseCursor = DATABASECONNECTION.cursor()
    print('Create database tables if they do not exist.')

    # create the drivers table
    databaseCursor.execute('''CREATE TABLE IF NOT EXISTS 
                        drivers(id INTEGER PRIMARY KEY,
                            fullName TEXT,
                            birthDate TEXT,
                            originContryID INTEGER,
                            seasons INTEGER,
                            currentDriver INTEGER,
                            currentChampPos INTEGER,
                            currentChampPoints REAL,
                            laps INTEGER,
                            lapsLead INTEGER,
                            driverTeamID INTEGER,
                            driverWins INTEGER,
                            podiums INTEGER,
                            poles INTEGER,
                            fastestLap INTEGER,
                            worldChamp INTEGER,
                            DNF INTEGER,
                            avgPoints REAL,
                            totalPoints REAL,
                            totalRaces INTEGER,
                            ratingF1Man22 INTEGER,
                            ratingEA INTEGER)''')
    DATABASECONNECTION.commit()

    # create the team table
    databaseCursor.execute('''CREATE TABLE IF NOT EXISTS 
                        teams(id INTEGER PRIMARY KEY,
                            fullName TEXT,
                            originContry TEXT,
                            teamFirstEntry INTEGER,
                            currentConstructor INTEGER,
                            currentChampPos INTEGER,
                            currentWins INTEGER,
                            currentChampPoints REAL,
                            teamWins INTEGER,
                            teamPodiums INTEGER,
                            worldChamp INTEGER,
                            poles INTEGER,
                            fastestLap INTEGER,
                            DNF INTEGER,
                            totalSeasons INTEGER,
                            totalPoints REAL,
                            totalRaces INTEGER,
                            avgPodiums REAL,
                            avgWins REAL,
                            avgPoints REAL)''')
    DATABASECONNECTION.commit()

    # create the track table
    databaseCursor.execute('''CREATE TABLE IF NOT EXISTS 
                        tracks(id INTEGER PRIMARY KEY,
                            fullName TEXT,
                            country TEXT,
                            racesHosted INTEGER,
                            wonFromPole INTEGER )''')
    DATABASECONNECTION.commit()

    # create the track results table
    databaseCursor.execute('''CREATE TABLE IF NOT EXISTS 
                        trackResults(id INTEGER PRIMARY KEY,
                            fullName TEXT,
                            eventYear INTEGER,
                            winner TEXT,
                            teamWinner TEXT,
                            pole TEXT,
                            teamPole TEXT)''')
    DATABASECONNECTION.commit()

    # create the country table
    databaseCursor.execute('''CREATE TABLE IF NOT EXISTS 
                        countries(id INTEGER PRIMARY KEY,
                            fullName TEXT,
                            weatherID INTEGER)''')
    DATABASECONNECTION.commit()

    # create the weather table
    databaseCursor.execute('''CREATE TABLE IF NOT EXISTS 
                        weather(id INTEGER PRIMARY KEY,
                            weatherDescription TEXT,
                            racingEaseRating INTEGER)''')
    DATABASECONNECTION.commit()

    # populate weather table
    insertWeatherConditions(databaseCursor)
    DATABASECONNECTION.commit()

    # close connection
    databaseCursor.close()
    disconnectFromDatabase()
