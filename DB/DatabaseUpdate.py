

def scrapperUpdate(databaseCursor, fullName, currentDriver, avgPoints=None, totalPoints=None, totalRaces=None, ratingsEA=None):
    """This function is mainly used by the web scrapper to update the database."""
    databaseCursor.execute('''INSERT INTO drivers(fullName,currentDriver,avgPoints,totalPoints,totalRaces,ratingEA) VALUES(?,?,?,?,?,?)''',
                           (str(fullName), int(currentDriver), float(avgPoints), float(totalPoints), int(totalRaces), int(ratingsEA)))


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


def f1ManagerUpdate(databaseCursor, fullName, birthDate=None, originContryID=None, ratingF1Man22=None):
    """This function is mainly used by the web scrapper to update the database."""
    if fullName != None:
        databaseCursor.execute('''UPDATE drivers SET birthDate=?, originContryID=?, ratingF1Man22=? WHERE fullName=?;''',
                               (str(birthDate), int(originContryID), int(ratingF1Man22), str(fullName)))
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

    # 1 cur pos, 2 cur wins, 3 cur points, 4 dnf


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
