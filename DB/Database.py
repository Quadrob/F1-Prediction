import sqlite3


DATABASECONNECTION = None


def connectToDatabase():
    """Create a connection to the database"""
    global DATABASECONNECTION
    DATABASECONNECTION = sqlite3.connect('DB/F1_DB.db')
    print("Opened database connection!")


def disconnectFromDatabase():
    """Disconnect from an active connection to the database"""
    global DATABASECONNECTION
    if (DATABASECONNECTION != None):
        DATABASECONNECTION.close()
        DATABASECONNECTION = None
        print("Closing database connection!")
    else:
        print("There was no active connection to close.")


def createTablesIfNotExist():
    """This function can be called to create all the database tables if they do not exist"""
    connectToDatabase()
    databaseCursor = DATABASECONNECTION.cursor()
    print('Create database tables if they do not exist.')

    # databaseCursor.close()
    # disconnectFromDatabase()
    # exit()
    # create the races table
    databaseCursor.execute('''CREATE TABLE IF NOT EXISTS
                            races(id INTEGER PRIMARY KEY,
                            season INT,
                            round INT,
                            circuit_id TEXT,
                            lat REAL,
                            long REAL,
                            country TEXT,
                            date TEXT,
                            url TEXT)''')
    DATABASECONNECTION.commit()

    # create the drivers table
    databaseCursor.execute('''CREATE TABLE IF NOT EXISTS
                        drivers(id INTEGER PRIMARY KEY,
                            fullName TEXT,
                            birthDate TEXT,
                            country TEXT,
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
                            country TEXT,
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
                            summary TEXT,
                            weatherDescription TEXT,
                            racingEaseRating INTEGER)''')
    DATABASECONNECTION.commit()

    # populate weather table
    insertWeatherConditions(databaseCursor)
    DATABASECONNECTION.commit()

    # close connection
    databaseCursor.close()
    disconnectFromDatabase()


def insertWeatherConditions(databaseCursor):
    """This function can be called to populate the different weather conditions"""
    weatherConditions = []
    weatherConditions.append(
        [1, 'Sunny', 'The weather is sunny when there are no clouds blocking the sunlight and the temperature is warm.', 95])
    weatherConditions.append(
        [2, 'Cloudy', 'The weather is cloudy when there are lots of clouds in the sky that get in the way of the sun.', 85])
    weatherConditions.append(
        [3, 'Drizzle', 'Drizzle happens when there are large clouds in the sky that produce very fine droplets of rain.', 70])
    weatherConditions.append(
        [4, 'Snowy', 'Snowy days usually happen in winter, when precipitation falls as snow instead of rain.', 40])
    weatherConditions.append(
        [5, 'Partly Cloudy', 'Partly cloudy is a relatively difficult type of weather to define, but it exists somewhere between sunny and cloudy.', 90])
    weatherConditions.append(
        [6, 'Overcast', 'Overcast weather conditions occur whenever the sky is covered with a layer of unbroken clouds.', 80])
    weatherConditions.append(
        [7, 'Foggy', 'Fog is defined as any type of cloud that forms at ground level. There are many, many reasons why fog might form, and some areas of the world are more predisposed to fog formation than others.', 70])
    weatherConditions.append(
        [8, 'Thunder and Lightning', 'Thunder and lightning are the result of a complex series of processes in the atmosphere, and scientists still don\'t completely understand the reasons why they happen.', 70])
    weatherConditions.append(
        [9, 'Windy', 'Wind can be defined as air under motion. Air moves whenever there\'s an imbalance between the pressure in any two locations.', 75])
    weatherConditions.append(
        [10, 'Rainy', 'Rainy weather happens when there are large clouds in the sky that produce rain. ', 65])
    weatherConditions.append(
        [11, 'Hot', 'Hot weather is characterized by drought and permanent aridity that lasts all year round, a significant lack of liquid water on the ground and in the surrounding air (more precisely, aridity).', 85])
    weatherConditions.append(
        [12, 'Cold', 'Cold is the presence of low temperature, especially in the atmosphere. In common usage, cold is often a subjective perception.', 80])
    for weather in weatherConditions:
        databaseCursor.execute('''UPDATE weather SET weatherDescription=?, racingEaseRating=? WHERE summary=? AND id=?;''',
                               (str(weather[2]), int(weather[3]), str(weather[1]), int(weather[0])))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            databaseCursor.execute('''INSERT INTO weather(id,summary,weatherDescription,racingEaseRating) VALUES(?,?,?,?)''',
                                   (int(weather[0]), str(weather[1]), str(weather[2]), int(weather[3])))
            print("Added: '" + weather[1] + "' to the weather table.")
        DATABASECONNECTION.commit()
