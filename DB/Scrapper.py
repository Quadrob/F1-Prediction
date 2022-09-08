from asyncio.windows_events import NULL
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import Database
import DatabaseUpdate


def configChromeDriver():
    # set driver for chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    global chromeDriver
    chromeDriver = webdriver.Chrome(
        ChromeDriverManager().install(), options=chrome_options)


def racingStats():
    chromeDriver.get(
        "https://www.racing-statistics.com/en/f1-drivers")
    content = chromeDriver.page_source
    soup = BeautifulSoup(content, "html.parser")
    tdCounter = 0
    teamID = 0

    for div in soup.findAll('div', attrs={'class': 'blocks blocks2'}):
        for tr in div.findAll('tr'):
            for td in tr.findAll('td'):
                match tdCounter:
                    case 0:
                        currentDriverPos.append(td.text.strip())
                        tdCounter += 1
                    case 2:
                        currentDriverName.append(td.text.strip())
                        tdCounter += 1
                    case 4:
                        teamID = getTeamID(td.text.strip())
                        currentDriverTeam.append(teamID)
                        tdCounter += 1
                    case 5:
                        currentDriverPoints.append(td.text.strip())
                        tdCounter = 0
                    case _:
                        tdCounter += 1


def theLoadOutDriverRatings():
    chromeDriver.get(
        "https://www.theloadout.com/f1-manager-2022/driver-ratings")
    content = chromeDriver.page_source
    soup = BeautifulSoup(content, "html.parser")

    for div in soup.findAll('div', attrs={'class': 'entry-content'}):
        for ul in div.findAll('ul'):
            for li in ul.findAll('li'):
                substring = li.text.split(" – ")
                loadout.append(substring)


def formula1pointsScrapper():
    chromeDriver.get("https://www.formula1points.com/analysis")
    content = chromeDriver.page_source
    soup = BeautifulSoup(content, "html.parser")
    tdCounter = 0

    for table in soup.findAll('table', attrs={'class': 'main-table dataTable', 'id': 'sortingoption'}):
        for row in table.findAll('tr', attrs={'role': 'row'}):
            for a in row.findAll('a'):
                names.append(a.text.strip())

            for td in row.findAll('td'):
                match tdCounter:
                    case 0:
                        avgpoint.append(td.text.strip())
                        tdCounter += 1
                    case 1:
                        totalpoints.append(td.text.strip())
                        tdCounter += 1
                    case 2:
                        totalraces.append(td.text.strip())
                        tdCounter = 0


def getTeamID(teamName):
    match teamName:
        case 'Red Bull':
            return 1
        case 'Ferrari':
            return 2
        case 'Mercedes':
            return 3
        case 'McLaren':
            return 4
        case 'Alpine F1 Team':
            return 5
        case 'Alfa Romeo':
            return 6
        case 'Haas F1 Team':
            return 7
        case 'Aston Martin':
            return 8
        case 'AlphaTauri':
            return 9
        case 'Williams':
            return 10
        case _:
            print("This team name was not found: " + teamName)
            return 0


# Start of the scrapper
currentDriverPos = []
currentDriverName = []
currentDriverTeam = []
currentDriverPoints = []

loadout = []

names = []
avgpoint = []
totalpoints = []
totalraces = []

ratingEA = 0
chromeDriver = NULL


Database.connectToDriverTable()
driverCursor = Database.DRIVERCONNECTION.cursor()
configChromeDriver()

racingStats()
for f1DriverNum in range(len(currentDriverName)):
    DatabaseUpdate.racingStatsUpdate(
        driverCursor, currentDriverName[f1DriverNum], 1, currentDriverPos[f1DriverNum], currentDriverTeam[f1DriverNum], currentDriverPoints[f1DriverNum])
    Database.DRIVERCONNECTION.commit()
    print("Added: '" +
          currentDriverName[f1DriverNum] + "' to the drivers table.")

theLoadOutDriverRatings()
formula1pointsScrapper()

# send the data to the db
for f1DriverNumber in range(len(names)):
    for loadoutName in loadout:
        if str(loadoutName[0]) == str(names[f1DriverNumber]):
            ratingEA = loadoutName[1]
            break
        elif str(names[f1DriverNumber]) == "Valtteri Bottas" and str(loadoutName[0]) == "Valterri Bottas":
            ratingEA = loadoutName[1]
            break
        ratingEA = 0

    # print(str(names[f1DriverNumber]) + " = " + str(ratingEA))
    # DatabaseUpdate.scrapperUpdate(driverCursor, names[f1DriverNumber], currentdriver[f1DriverNumber],
    #                               avgpoint[f1DriverNumber], totalpoints[f1DriverNumber], totalraces[f1DriverNumber], ratingEA)
    Database.DRIVERCONNECTION.commit()


try:
    chromeDriver.quit()
    chromeDriver.close()
    driverCursor.close()
    Database.disconnectToDriverTable()
except:
    print('Closing Scrapper!')
