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

for f1Driver in SS.currentDriverStats:
    if str(f1Driver[0]) == "Esteban Ocon" or str(f1Driver[0]) == "Pierre Gasly" or str(f1Driver[0]) == "Kevin Magnussen" or str(f1Driver[0]) == "Mick Schumacher" or str(f1Driver[0]) == "Yuki Tsunoda" or str(f1Driver[0]) == "Guanyu Zhou" or str(f1Driver[0]) == "Alexander Albon" or str(f1Driver[0]) == "Nyck de Vries" or str(f1Driver[0]) == "Nicholas Latifi":
        for statNum in range(len(f1Driver)):
            if statNum == 14:
                f1Driver[statNum] = None
            elif statNum >= 6:
                f1Driver[statNum] = f1Driver[statNum + 1]

    avgPoints = float(f1Driver[9])/float(f1Driver[8])
    poles = f1Driver[3].split("(")[0]
    DatabaseUpdate.racingDriverStatsUpdate(databaseCursor, str(f1Driver[0]), int(f1Driver[6]), int(f1Driver[10]), int(f1Driver[11]), int(f1Driver[1]), int(
        f1Driver[2]), int(poles), int(f1Driver[12]), int(f1Driver[4]), int(f1Driver[13]), float(avgPoints), float(f1Driver[9]), int(f1Driver[8]))
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
for teamPoints in SS.f1ConstructorsPoints:
    teamName = SS.getTeamName(teamPoints[0])
    avgPoints = float(teamPoints[15])/float(teamPoints[3])
    DatabaseUpdate.f1TeamsPointsUpdate(databaseCursor, str(teamName), int(
        teamPoints[2]), int(teamPoints[3]), float(teamPoints[4]), float(teamPoints[5]), int(teamPoints[12]), float(teamPoints[15]), float(avgPoints))
    Database.DATABASECONNECTION.commit()


# Put data from f1 stats website into tracks and results table
SS.trackStatsScrapper()
for track in SS.trackStats:
    wonFromPole = track[14].split('x')[0]
    DatabaseUpdate.trackStatsUpdate(databaseCursor, str(track[0]), str(
        track[2]), int(track[4]), int(wonFromPole))
    Database.DATABASECONNECTION.commit()
for result in SS.trackResults:
    try:
        year = re.sub('[^0-9]', '', result[1])
        DatabaseUpdate.trackResultsUpdate(databaseCursor, str(result[0]), int(year), str(result[2]), str(
            result[3]), str(result[4]), str(result[5]))
        Database.DATABASECONNECTION.commit()
    except:
        print("No data for track '" + result[0] + "' in " + str(year))

print(SS.countries)

# Close all variables
SS.disconnectChromeDriver()
databaseCursor.close()
Database.disconnectFromDatabase()
print('Closing Scrapper!')
