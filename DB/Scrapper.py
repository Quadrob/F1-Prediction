import Database
import DatabaseUpdate
import ScrapperScripts.APIScrapper as AS
import ScrapperScripts.SeleniumScrapper as SS


# Setup scrapper config
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
print(AS.F1Manager22RatingsData)

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


try:
    SS.chromeDriver.quit()
    SS.chromeDriver.close()
    databaseCursor.close()
    Database.disconnectFromDatabase()
except:
    print('Closing Scrapper!')
