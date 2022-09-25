def racingStatsUpdate(databaseCursor, fullName, currentDriver, currentDriverPos, currentDriverTeam, currentDriverPoints):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE drivers SET currentDriver=?, currentChampPos=?, driverTeamID=?, currentChampPoints=? WHERE fullName=?;''',
                               (int(currentDriver), int(currentDriverPos), int(currentDriverTeam), float(currentDriverPoints), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            databaseCursor.execute('''INSERT INTO drivers(fullName,currentDriver,currentChampPos,driverTeamID,currentChampPoints) VALUES(?,?,?,?,?)''',
                                   (str(fullName), int(currentDriver), int(currentDriverPos), int(currentDriverTeam), float(currentDriverPoints)))
            print("Added: '" + fullName + "' to the drivers table.")
    else:
        print('Cant run method without a full driver name')


def racingDriverStatsUpdate(databaseCursor, fullName, seasons=None, laps=None, lapsLead=None, driverWins=None, podiums=None, poles=None, fastestLap=None, worldChamp=None, DNF=None, avgPoints=None, totalPoints=None, totalRaces=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE drivers SET seasons=?, laps=?, lapsLead=?, driverWins=?, podiums=?, poles=?, fastestLap=?, worldChamp=?, DNF=?, avgPoints=?, totalPoints=?, totalRaces=? WHERE fullName=?;''',
                               (int(seasons), int(laps), int(lapsLead), int(driverWins), int(podiums), int(poles), int(fastestLap), int(worldChamp), int(DNF), float(avgPoints), float(totalPoints), int(totalRaces), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            print("Failed to update driver: '" + fullName + "'")
    else:
        print('Cant run method without a full driver name')


def loadoutUpdate(databaseCursor, fullName, ratingsEA=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE drivers SET ratingEA=? WHERE fullName=?;''',
                               (int(ratingsEA), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            databaseCursor.execute('''INSERT INTO drivers(fullName,currentDriver,ratingEA) VALUES(?,?,?)''',
                                   (str(fullName), 0, int(ratingsEA)))
            print("Added: '" + fullName +
                  "' to the drivers table with ratingEA = " + str(ratingsEA))
    else:
        print('Cant run method without a full driver name')


def f1ManagerUpdate(databaseCursor, fullName, birthDate=None, ratingF1Man22=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE drivers SET birthDate=?, ratingF1Man22=? WHERE fullName=?;''',
                               (str(birthDate), int(ratingF1Man22), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            print("Failed to update driver: '" + fullName + "'")
    else:
        print('Cant run method without a full driver name')


def f1TeamsUpdate(databaseCursor, fullName, teamFirstEntry=None, currentChampPos=None, worldChamp=None, teamWins=None, poles=None, fastestLap=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE teams SET teamFirstEntry=?, currentConstructor=?, currentChampPos=?, worldChamp=?, teamWins=?, poles=?, fastestLap=? WHERE fullName=?;''',
                               (int(teamFirstEntry), 1, int(currentChampPos), int(worldChamp), int(teamWins), int(poles), int(fastestLap), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            databaseCursor.execute('''INSERT INTO teams(fullName,teamFirstEntry,currentConstructor,currentChampPos,worldChamp,teamWins,poles,fastestLap) VALUES(?,?,?,?,?,?,?,?)''',
                                   (str(fullName), int(teamFirstEntry), 1, int(currentChampPos), int(worldChamp), int(teamWins), int(poles), int(fastestLap)))
            print("Added: '" + fullName + "' to the teams table.")
    else:
        print('Cant run method without a full driver name')


def f1TeamsDNFsUpdate(databaseCursor, fullName, currentChampPos=None, currentWins=None, currentChampPoints=None, DNF=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE teams SET currentChampPos=?, currentWins=?, currentChampPoints=?, DNF=? WHERE fullName=?;''',
                               (int(currentChampPos), int(currentWins), float(currentChampPoints), int(DNF), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            print("Failed to update team: " + str(fullName))
    else:
        print('Cant run method without a full driver name')


def f1TeamsPointsUpdate(databaseCursor, fullName, teamPodiums=None, totalRaces=None, avgWins=None, avgPodiums=None, totalSeasons=None, totalPoints=None, avgPoints=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE teams SET teamPodiums=?, totalRaces=?, avgWins=?, avgPodiums=?, totalSeasons=?, totalPoints=?, avgPoints=? WHERE fullName=?;''',
                               (int(teamPodiums), int(totalRaces), float(avgWins), float(avgPodiums), int(totalSeasons), float(totalPoints), float(avgPoints), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            print("Failed to update team: " + str(fullName))
    else:
        print('Cant run method without a full driver name')


def trackResultsUpdate(databaseCursor, fullName, eventYear=None, winner=None, teamWinner=None, pole=None, teamPole=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE trackResults SET winner=?, teamWinner=?, pole=?, teamPole=? WHERE fullName=? AND eventYear=?;''',
                               (str(winner), str(teamWinner), str(pole), str(teamPole), str(fullName), int(eventYear)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            databaseCursor.execute('''INSERT INTO trackResults(fullName,eventYear,winner,teamWinner,pole,teamPole) VALUES(?,?,?,?,?,?)''',
                                   (str(fullName), int(eventYear), str(winner), str(teamWinner), str(pole), str(teamPole)))
            print("Added: '" + fullName + "' to the track results table.")
    else:
        print('Cant run method without a full driver name')


def trackStatsUpdate(databaseCursor, fullName, country=None, racesHosted=None, wonFromPole=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE tracks SET country=?, racesHosted=?, wonFromPole=? WHERE fullName=?;''',
                               (str(country), int(racesHosted), int(wonFromPole), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            databaseCursor.execute('''INSERT INTO tracks(fullName,country,racesHosted,wonFromPole) VALUES(?,?,?,?)''',
                                   (str(fullName), str(country), int(racesHosted), int(wonFromPole)))
            print("Added: '" + fullName + "' to the tracks table.")
    else:
        print('Cant run method without a full driver name')


def countriesUpdate(databaseCursor, fullName):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE countries SET fullName=? WHERE fullName=?;''',
                               (str(fullName), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            databaseCursor.execute('''INSERT INTO countries(fullName) VALUES(?)''',
                                   (str(fullName),))
            print("Added: '" + fullName + "' to the countries table.")
    else:
        print('Cant run method without a full name')


def driverCountryUpdate(databaseCursor, fullName, country=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE drivers SET country=? WHERE fullName=?;''',
                               (str(country), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            print("Failed to update driver: '" + fullName + "'")
    else:
        print('Cant run method without a full driver name')


def teamCountryUpdate(databaseCursor, fullName, country=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE teams SET country=? WHERE fullName=?;''',
                               (str(country), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            print("Failed to update team: '" + fullName + "'")
    else:
        print('Cant run method without a full team name')


def countryWeatherUpdate(databaseCursor, fullName, weatherID=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE countries SET weatherID=? WHERE fullName=?;''',
                               (int(weatherID), str(fullName)))
        rowsUpdated = databaseCursor.rowcount
        if int(rowsUpdated) <= 0:
            print("Failed to update country: '" + fullName + "'")
    else:
        print('Cant run method without a full country name')
