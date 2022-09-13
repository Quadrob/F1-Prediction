from asyncio.windows_events import NULL
from copyreg import constructor
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chromeDriver = NULL
currentDriverPos = []
currentDriverNames = []
currentDriverTeam = []
currentDriverPoints = []
loadoutRatingsData = []

f1ConstructorsData = []
f1ConstructorsDNFs = []
f1ConstructorsPoints = []

names = []
avgpoint = []
totalpoints = []
totalraces = []


def configChromeDriver():
    # set driver for chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    global chromeDriver
    chromeDriver = webdriver.Chrome(
        ChromeDriverManager().install(), options=chrome_options)


def disconnectChromeDriver():
    global chromeDriver
    chromeDriver.quit()
    chromeDriver = NULL
    print('Closing chrome driver!')


def racingStats():
    global chromeDriver
    global currentDriverPos
    global currentDriverNames
    global currentDriverTeam
    global currentDriverPoints
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
                        currentDriverNames.append(td.text.strip())
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
    global loadoutRatingsData
    chromeDriver.get(
        "https://www.theloadout.com/f1-manager-2022/driver-ratings")
    content = chromeDriver.page_source
    soup = BeautifulSoup(content, "html.parser")

    for div in soup.findAll('div', attrs={'class': 'entry-content'}):
        for ul in div.findAll('ul'):
            for li in ul.findAll('li'):
                substring = li.text.split(" – ")
                loadoutRatingsData.append(substring)


def formula1pointsScrapper():
    global names
    global avgpoint
    global totalpoints
    global totalraces
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


def f1ConstructorsInfo():
    chromeDriver.get(
        "https://www.formula1.com/en/teams.html")
    content = chromeDriver.page_source
    soup = BeautifulSoup(content, "html.parser")

    for div in soup.findAll('div', attrs={'class': 'container listing team-listing'}):
        for a in div.findAll('a', attrs={'class': 'listing-link'}, href=True):
            chromeDriver.get("https://www.formula1.com" + str(a['href']))
            content = chromeDriver.page_source
            soup = BeautifulSoup(content, "html.parser")
            f1ConstructorsInfoExtractor(soup)


def f1ConstructorsInfoExtractor(soup):
    global f1ConstructorsData
    tdCounter = 0
    for tbody in soup.findAll('tbody'):
        f1Constructor = []
        for tr in tbody.findAll('tr'):
            for td in tr.findAll('td'):
                match tdCounter:
                    case 0:
                        f1Constructor.append(td.text.strip())
                        tdCounter += 1
                    case 6:
                        f1Constructor.append(td.text.strip())
                        tdCounter += 1
                    case 7:
                        f1Constructor.append(td.text.strip())
                        tdCounter += 1
                    case 8:
                        f1Constructor.append(td.text.strip())
                        tdCounter += 1
                    case 9:
                        f1Constructor.append(td.text.strip())
                        tdCounter += 1
                    case 10:
                        f1Constructor.append(td.text.strip())
                        tdCounter = 0
                    case _:
                        tdCounter += 1
        f1ConstructorsData.append(f1Constructor)


def f1ConstructorDNFInfo():
    global f1ConstructorsDNFs
    teams = ['red-bull', 'ferrari', 'mercedes', 'mclaren', 'alpine-f1-team',
             'alfa-romeo', 'haas-f1-team', 'aston-martin', 'alphatauri', 'williams']
    for team in teams:
        chromeDriver.get(
            "https://www.racing-statistics.com/en/f1-constructors/compare/" + team + "/seasons/2022s")
        content = chromeDriver.page_source
        soup = BeautifulSoup(content, "html.parser")
        teamDNFs = []
        thCounter = 0
        tdCounter = 0

        for table in soup.findAll('table', attrs={'class': 'bottommargin'}):
            for tr in table.findAll('tr'):
                for th in tr.findAll('th'):
                    match thCounter:
                        case 1:
                            teamDNFs.append(th.text.strip())
                            thCounter = 0
                        case _:
                            thCounter += 1
                for td in tr.findAll('td'):
                    match tdCounter:
                        case 1:
                            teamDNFs.append(td.text.strip())
                            tdCounter = 0
                        case _:
                            tdCounter += 1
            tempDNF = []
            tempDNF.append(teamDNFs[0])
            tempDNF.append(teamDNFs[2])
            tempDNF.append(teamDNFs[4])
            tempDNF.append(teamDNFs[6])
            tempDNF.append(teamDNFs[7])
            f1ConstructorsDNFs.append(tempDNF)
            break


def f1ConstructorsPointsScrapper():
    global f1ConstructorsPoints
    teams = ['Red-bull', 'Ferrari', 'Mercedes', 'Mclaren', 'Alpine-f1-team',
             'Alfa-romeo', 'Haas-f1-team', 'Aston-martin', 'Alphatauri', 'Williams']
    for team in teams:
        chromeDriver.get(
            "https://www.formula1points.com/team/" + team)
        content = chromeDriver.page_source
        soup = BeautifulSoup(content, "html.parser")
        tableCounter = 0
        teamPoints = []
        teamPoints.append(team)

        for table in soup.findAll('table', attrs={'class': 'main-table'}):
            match tableCounter:
                case 2:
                    for tbody in table.findAll('tbody'):
                        for tr in tbody.findAll('tr'):
                            for td in tr.findAll('td'):
                                teamPoints.append(td.text.strip())
                    f1ConstructorsPoints.append(teamPoints)
                    break
                case _:
                    tableCounter += 1


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


def getTeamName(teamName):
    match teamName:
        case 'Red Bull':
            return 'Oracle Red Bull Racing'
        case 'Ferrari':
            return 'Scuderia Ferrari'
        case 'Mercedes':
            return 'Mercedes-AMG Petronas F1 Team'
        case 'McLaren':
            return 'McLaren F1 Team'
        case 'Alpine F1 Team':
            return 'BWT Alpine F1 Team'
        case 'Alfa Romeo':
            return 'Alfa Romeo F1 Team ORLEN'
        case 'Haas F1 Team':
            return 'Haas F1 Team'
        case 'Aston Martin':
            return 'Aston Martin Aramco Cognizant F1 Team'
        case 'AlphaTauri':
            return 'Scuderia AlphaTauri'
        case 'Williams':
            return 'Williams Racing'
        case _:
            print("This team name was not found: " + teamName)
            return 0
