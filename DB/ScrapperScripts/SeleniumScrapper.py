from copyreg import constructor
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chromeDriver = None
currentDriverPos = []
currentDriverNames = []
currentDriverTeam = []
currentDriverPoints = []
currentDriverLinks = []
currentDriverStats = []
loadoutRatingsData = []

f1ConstructorsData = []
f1ConstructorsDNFs = []
f1ConstructorsPoints = []

trackLinks = []
trackStats = []
trackResults = []

countries = []


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
    chromeDriver = None
    print('Closing chrome driver!')


def racingStats():
    global currentDriverPos
    global currentDriverNames
    global currentDriverTeam
    global currentDriverPoints
    global currentDriverLinks
    global currentDriverStats
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
                        for a in td.findAll('a', href=True):
                            currentDriverLinks.append(
                                (td.text.strip(), str(a['href'])))
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

    for driverLink in currentDriverLinks:
        chromeDriver.get(driverLink[1])
        content = chromeDriver.page_source
        soup = BeautifulSoup(content, "html.parser")
        fieldsetCounter = 0
        tbodyCounter = 0
        tdCounter = 0
        statCounter = 0
        driverStats = []
        driverStats.append(str(driverLink[0]))

        for div in soup.findAll('div', attrs={'class': 'blocks blocks2'}):
            for fieldset in div.findAll('fieldset', attrs={'class': 'block'}):
                match fieldsetCounter:
                    case 1:
                        for tbody in fieldset.findAll('tbody'):
                            match tbodyCounter:
                                case 0:
                                    for tr in tbody.findAll('tr'):
                                        tdCounter = 0
                                        statCounter = 0
                                        for td in tr.findAll('td'):
                                            match tdCounter:
                                                case 1:
                                                    tdStats = td.text.strip().replace(" ", "").split("\n")
                                                    for stat in tdStats:
                                                        match statCounter:
                                                            case 0:
                                                                driverStats.append(
                                                                    stat)
                                                                statCounter += 1
                                                            case _:
                                                                statCounter += 1
                                                    tdCounter += 1
                                                case _:
                                                    tdCounter += 1
                                    tbodyCounter += 1
                                case _:
                                    tbodyCounter += 1
                        fieldsetCounter += 1
                    case _:
                        fieldsetCounter += 1
            currentDriverStats.append(driverStats)
            break


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
    teams = ['Red-bull', 'Ferrari', 'Mercedes', 'Mclaren', 'Alpine',
             'Alfa-romeo', 'Haas', 'Aston Martin', 'Alphatauri', 'Williams']
    for team in teams:
        chromeDriver.get(
            "https://www.formula1points.com/team/" + team)
        content = chromeDriver.page_source
        soup = BeautifulSoup(content, "html.parser")
        tableCounter = 0
        tdCounter = 0
        teamPoints = []
        teamTotal = 0
        teamPoints.append(team)

        for table in soup.findAll('table', attrs={'class': 'main-table'}):
            match tableCounter:
                case 1:
                    for tbody in table.findAll('tbody'):
                        for tr in tbody.findAll('tr'):
                            for td in tr.findAll('td'):
                                match tdCounter:
                                    case 1:
                                        teamTotal = float(td.text.strip())
                                        tdCounter += 1
                                        break
                                    case _:
                                        tdCounter += 1
                            tableCounter += 1
                            break
                case 2:
                    for tbody in table.findAll('tbody'):
                        for tr in tbody.findAll('tr'):
                            for td in tr.findAll('td'):
                                teamPoints.append(td.text.strip())
                    teamPoints.append(teamTotal)
                    f1ConstructorsPoints.append(teamPoints)
                    break
                case _:
                    tableCounter += 1


def trackStatsScrapper():
    global trackLinks
    global trackStats
    global trackResults
    global countries
    chromeDriver.get(
        "https://www.racing-statistics.com/en/circuits")
    content = chromeDriver.page_source
    soup = BeautifulSoup(content, "html.parser")
    tdCounter = 0

    for fieldset in soup.findAll('fieldset', attrs={'class': 'block letterboxlist'}):
        for div in fieldset.findAll('div', attrs={'class': 'letterbox'}):
            for tbody in div.findAll('tbody'):
                for tr in tbody.findAll('tr'):
                    teamLink = []
                    for td in tr.findAll('td'):
                        match tdCounter:
                            case 1:
                                teamLink.append(td.text.strip())
                                for a in td.findAll('a', href=True):
                                    teamLink.append(str(a['href']))
                                trackLinks.append(teamLink)
                                tdCounter = 0
                            case _:
                                tdCounter += 1

    for track in trackLinks:
        chromeDriver.get(track[1])
        content = chromeDriver.page_source
        soup = BeautifulSoup(content, "html.parser")
        divCounter = 0
        tbodyCounter = 0
        tdCounter = 0
        trackStatsTemp = []
        trackStatsTemp.append(track[0])
        trackResultsTemp = []

        for div in soup.findAll('div', attrs={'class': 'layout', 'itemtype': 'http://schema.org/TouristAttraction'}):
            for innerdiv in div.findAll('div'):
                match divCounter:
                    case 0:
                        for tbody in innerdiv.findAll('tbody'):
                            match tbodyCounter:
                                case 0:
                                    for tr in tbody.findAll('tr', attrs={'itemprop': 'address'}):
                                        for td in tr.findAll('td'):
                                            trackStatsTemp.append(
                                                td.text.strip())
                                            countries.append(td.text.strip())
                                    tbodyCounter += 1
                                case 1:
                                    for tr in tbody.findAll('tr'):
                                        for td in tr.findAll('td'):
                                            trackStatsTemp.append(
                                                td.text.strip())
                                    tbodyCounter += 1
                        trackStats.append(trackStatsTemp)
                        divCounter += 1
                    case 4:
                        for tbody in innerdiv.findAll('tbody'):
                            for tr in tbody.findAll('tr'):
                                tdCounter = 0
                                trackResultsTemp = []
                                trackResultsTemp.append(track[0])
                                for td in tr.findAll('td'):
                                    match tdCounter:
                                        case 1:
                                            trackResultsTemp.append(
                                                td.text.strip())
                                            tdCounter += 1
                                        case 4:
                                            trackResultsTemp.append(
                                                td.text.strip())
                                            tdCounter += 1
                                        case 5:
                                            trackResultsTemp.append(
                                                td.text.strip())
                                            tdCounter += 1
                                        case 8:
                                            trackResultsTemp.append(
                                                td.text.strip())
                                            tdCounter += 1
                                        case 9:
                                            trackResultsTemp.append(
                                                td.text.strip())
                                            tdCounter += 1
                                        case _:
                                            tdCounter += 1
                                trackResults.append(trackResultsTemp)
                        divCounter += 1
                    case _:
                        divCounter += 1


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
        case 'Red-bull':
            return 'Oracle Red Bull Racing'
        case 'Ferrari':
            return 'Scuderia Ferrari'
        case 'Mercedes':
            return 'Mercedes-AMG Petronas F1 Team'
        case 'McLaren':
            return 'McLaren F1 Team'
        case 'Mclaren':
            return 'McLaren F1 Team'
        case 'Alpine F1 Team':
            return 'BWT Alpine F1 Team'
        case 'Alpine':
            return 'BWT Alpine F1 Team'
        case 'Alfa Romeo':
            return 'Alfa Romeo F1 Team ORLEN'
        case 'Alfa-romeo':
            return 'Alfa Romeo F1 Team ORLEN'
        case 'Haas F1 Team':
            return 'Haas F1 Team'
        case 'Haas':
            return 'Haas F1 Team'
        case 'Aston Martin':
            return 'Aston Martin Aramco Cognizant F1 Team'
        case 'Aston-Martin':
            return 'Aston Martin Aramco Cognizant F1 Team'
        case 'AlphaTauri':
            return 'Scuderia AlphaTauri'
        case 'Alphatauri':
            return 'Scuderia AlphaTauri'
        case 'Williams':
            return 'Williams Racing'
        case _:
            print("This team name was not found: " + teamName)
            return teamName
