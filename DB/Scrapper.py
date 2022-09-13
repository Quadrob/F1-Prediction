import re
import Database
import DatabaseUpdate
import ScrapperScripts.APIScrapper as AS
import ScrapperScripts.SeleniumScrapper as SS


# Setup scrapper config
Database.createTablesIfNotExist()
Database.connectToDatabase()
databaseCursor = Database.DATABASECONNECTION.cursor()
SS.configChromeDriver()

# Put data from the racing statistics website into the database
SS.racingStats()
for f1DriverNum in range(len(SS.currentDriverNames)):
    DatabaseUpdate.racingStatsUpdate(
        databaseCursor, SS.currentDriverNames[f1DriverNum], 1, SS.currentDriverPos[f1DriverNum], SS.currentDriverTeam[f1DriverNum], SS.currentDriverPoints[f1DriverNum])
    Database.DATABASECONNECTION.commit()

# Put data from loadout website into the databse
SS.theLoadOutDriverRatings()
for loadoutDriver in SS.loadoutRatingsData:
    if str(loadoutDriver[0]) == "Esetban Ocon":
        loadoutDriver[0] = "Esteban Ocon"
    elif str(loadoutDriver[0]) == "Sergio Perez":
        loadoutDriver[0] = "Sergio Pérez"
    elif str(loadoutDriver[0]) == "Valterri Bottas":
        loadoutDriver[0] = "Valtteri Bottas"
    elif str(loadoutDriver[0]) == "Zhou Guanyu":
        loadoutDriver[0] = "Guanyu Zhou"
    elif str(loadoutDriver[0]) == "Nico Hulkenburg":
        loadoutDriver[0] = "Nico Hülkenberg"

    DatabaseUpdate.loadoutUpdate(databaseCursor, str(
        loadoutDriver[0]), int(loadoutDriver[1]))
    Database.DATABASECONNECTION.commit()

# Put data from f1 manager 2022 website into the databse
AS.f1Manager22DriverRatings()
for f1ManagerDriver in AS.F1Manager22RatingsData:
    if str(f1ManagerDriver[0]) == "Sergio Perez":
        f1ManagerDriver[0] = "Sergio Pérez"
    elif str(f1ManagerDriver[0]) == "Carlos Sainz Jr.":
        f1ManagerDriver[0] = "Carlos Sainz"
    elif str(f1ManagerDriver[0]) == "Zhou Guanyu":
        f1ManagerDriver[0] = "Guanyu Zhou"

    DatabaseUpdate.f1ManagerUpdate(databaseCursor, str(f1ManagerDriver[0]), str(
        f1ManagerDriver[1]), int(f1ManagerDriver[2]), int(f1ManagerDriver[3]))
    Database.DATABASECONNECTION.commit()

# SS.formula1pointsScrapper()
# for f1DriverNumber in range(len(names)):
#     for loadoutName in loadoutRatingsData:
#         if str(loadoutName[0]) == str(names[f1DriverNumber]):
#             ratingEA = loadoutName[1]
#             break
#         elif str(names[f1DriverNumber]) == "Valtteri Bottas" and str(loadoutName[0]) == "Valterri Bottas":
#             ratingEA = loadoutName[1]
#             break
#         ratingEA = 0

#     print(str(names[f1DriverNumber]) + " = " + str(ratingEA))
#     DatabaseUpdate.scrapperUpdate(driverCursor, names[f1DriverNumber], currentdriver[f1DriverNumber],
#                                   avgpoint[f1DriverNumber], totalpoints[f1DriverNumber], totalraces[f1DriverNumber], ratingEA)
#     Database.DATABASECONNECTION.commit()


# Put data from f1 website into teams table
SS.f1ConstructorsInfo()
teamCurrentPos = 1
for f1Team in SS.f1ConstructorsData:
    worldChampions = f1Team[2]
    if str(worldChampions) == 'N/A':
        worldChampions = 0

    teamWins = f1Team[3].split(' (x')
    if str(teamWins[0]) == '1':
        teamWins = re.sub('[^0-9]', '', teamWins[1])
    else:
        teamWins = 0

    poles = f1Team[4]
    if str(poles) == 'N/A':
        poles = 0

    fastestLaps = f1Team[5]
    if str(fastestLaps) == 'N/A':
        fastestLaps = 0

    DatabaseUpdate.f1TeamsUpdate(databaseCursor, str(f1Team[0]), str(
        f1Team[1]), int(teamCurrentPos), int(worldChampions), int(teamWins), int(poles), int(fastestLaps))
    Database.DATABASECONNECTION.commit()
    teamCurrentPos += 1


# Put data from f1 website into teams table
SS.f1ConstructorDNFInfo()
for teamDNFs in SS.f1ConstructorsDNFs:
    teamName = SS.getTeamName(teamDNFs[0])
    teamPos = re.sub('[^0-9]', '', teamDNFs[1])
    DatabaseUpdate.f1TeamsDNFsUpdate(databaseCursor, str(teamName), int(
        teamPos), int(teamDNFs[2]), float(teamDNFs[3]), int(teamDNFs[4]))
    Database.DATABASECONNECTION.commit()


# Put data from f1 points website into teams table
SS.f1ConstructorsPointsScrapper()
# name, wins, podiums, totalraces, avg win, avg podiums, fastest lap, poles, best pos, current team, first season, last season,
#                                       num of seasons, best pos in champ, worst pos in champ
print(str(SS.f1ConstructorsPoints))


# Close all variables
SS.disconnectChromeDriver()
databaseCursor.close()
Database.disconnectFromDatabase()
print('Closing Scrapper!')