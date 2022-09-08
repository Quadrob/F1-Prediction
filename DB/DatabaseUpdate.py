import sqlite3
from asyncio.windows_events import NULL
import Database


def scrapperUpdate(driverCursor, fullName, currentDriver, avgPoints=NULL, totalPoints=NULL, totalRaces=NULL, ratingsEA=NULL):
    """This function is mainly used by the web scrapper to update the database."""
    driverCursor.execute('''INSERT INTO drivers(fullName,currentDriver,avgPoints,totalPoints,totalRaces,ratingEA) VALUES(?,?,?,?,?,?)''',
                         (str(fullName), int(currentDriver), float(avgPoints), float(totalPoints), int(totalRaces), int(ratingsEA)))


def racingStatsUpdate(driverCursor, fullName, currentDriver, currentDriverPos, currentDriverTeam, currentDriverPoints):
    """This function is mainly used by the web scrapper to update the database."""
    driverCursor.execute('''INSERT INTO drivers(fullName,currentDriver,currentChampPos,driverTeamID,currentChampPoints) VALUES(?,?,?,?,?)''',
                         (str(fullName), int(currentDriver), int(currentDriverPos), int(currentDriverTeam), float(currentDriverPoints)))
