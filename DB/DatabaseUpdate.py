from asyncio.windows_events import NULL


def scrapperUpdate(databaseCursor, fullName, currentDriver, avgPoints=NULL, totalPoints=NULL, totalRaces=NULL, ratingsEA=NULL):
    """This function is mainly used by the web scrapper to update the database."""
    databaseCursor.execute('''INSERT INTO drivers(fullName,currentDriver,avgPoints,totalPoints,totalRaces,ratingEA) VALUES(?,?,?,?,?,?)''',
                           (str(fullName), int(currentDriver), float(avgPoints), float(totalPoints), int(totalRaces), int(ratingsEA)))


def racingStatsUpdate(databaseCursor, fullName, currentDriver, currentDriverPos, currentDriverTeam, currentDriverPoints):
    """This function is mainly used by the web scrapper to update the database."""
    databaseCursor.execute('''UPDATE drivers SET currentDriver=?, currentChampPos=?, driverTeamID=?, currentChampPoints=? WHERE fullName=?;''',
                           (int(currentDriver), int(currentDriverPos), int(currentDriverTeam), float(currentDriverPoints), str(fullName)))
    rowsUpdated = databaseCursor.rowcount
    if int(rowsUpdated) <= 0:
        databaseCursor.execute('''INSERT INTO drivers(fullName,currentDriver,currentChampPos,driverTeamID,currentChampPoints) VALUES(?,?,?,?,?)''',
                               (str(fullName), int(currentDriver), int(currentDriverPos), int(currentDriverTeam), float(currentDriverPoints)))
        print("Added: '" + fullName + "' to the drivers table.")


def loadoutUpdate(databaseCursor, fullName, ratingsEA=NULL):
    """This function is mainly used by the web scrapper to update the database."""
    databaseCursor.execute('''UPDATE drivers SET ratingEA=? WHERE fullName=?;''',
                           (int(ratingsEA), str(fullName)))
    rowsUpdated = databaseCursor.rowcount
    if int(rowsUpdated) <= 0:
        databaseCursor.execute('''INSERT INTO drivers(fullName,currentDriver,ratingEA) VALUES(?,?,?)''',
                               (str(fullName), 0, int(ratingsEA)))
        print("Added: '" + fullName +
              "' to the drivers table with ratingEA = " + str(ratingsEA))
