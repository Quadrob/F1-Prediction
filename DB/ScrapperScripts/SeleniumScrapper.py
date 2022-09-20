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
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    global chromeDriver
    chromeDriver = webdriver.Chrome(options=chrome_options)


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
    chromeDriver.get("https://www.racing-statistics.com/en/f1-drivers")
    content = chromeDriver.page_source
    soup = BeautifulSoup(content, "html.parser")
    tdCounter = 0
    teamID = 0

    for div in soup.findAll('div', attrs={'class': 'blocks blocks2'}):
        for tr in div.findAll('tr'):
            for td in tr.findAll('td'):
                if tdCounter == 0:
                    currentDriverPos.append(td.text.strip())
                    tdCounter += 1
                elif tdCounter == 2:
                    currentDriverNames.append(td.text.strip())
                    for a in td.findAll('a', href=True):
                        currentDriverLinks.append(
                            (td.text.strip(), str(a['href'])))
                    tdCounter += 1
                elif tdCounter == 4:
                    teamID = getTeamID(td.text.strip())
                    currentDriverTeam.append(teamID)
                    tdCounter += 1
                elif tdCounter == 5:
                    currentDriverPoints.append(td.text.strip())
                    tdCounter = 0
                else:
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
                if fieldsetCounter == 1:
                    for tbody in fieldset.findAll('tbody'):
                        if tbodyCounter == 0:
                            for tr in tbody.findAll('tr'):
                                tdCounter = 0
                                statCounter = 0
                                for td in tr.findAll('td'):
                                    if tdCounter == 1:
                                        tdStats = td.text.strip().replace(
                                            " ", "").split("\n")
                                        for stat in tdStats:
                                            if statCounter == 0:
                                                driverStats.append(stat)
                                                statCounter += 1
                                            else:
                                                statCounter += 1
                                        tdCounter += 1
                                    else:
                                        tdCounter += 1
                            tbodyCounter += 1
                        else:
                            tbodyCounter += 1
                    fieldsetCounter += 1
                else:
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
    chromeDriver.get("https://www.formula1.com/en/teams.html")
    content = chromeDriver.page_source
    soup = BeautifulSoup(content, "html.parser")

    for div in soup.findAll('div',
                            attrs={'class': 'container listing team-listing'}):
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
                if tdCounter == 0:
                    f1Constructor.append(td.text.strip())
                    tdCounter += 1
                elif tdCounter == 6:
                    f1Constructor.append(td.text.strip())
                    tdCounter += 1
                elif tdCounter == 7:
                    f1Constructor.append(td.text.strip())
                    tdCounter += 1
                elif tdCounter == 8:
                    f1Constructor.append(td.text.strip())
                    tdCounter += 1
                elif tdCounter == 9:
                    f1Constructor.append(td.text.strip())
                    tdCounter += 1
                elif tdCounter == 10:
                    f1Constructor.append(td.text.strip())
                    tdCounter = 0
                else:
                    tdCounter += 1
        f1ConstructorsData.append(f1Constructor)


def f1ConstructorDNFInfo():
    global f1ConstructorsDNFs
    teams = [
        'red-bull', 'ferrari', 'mercedes', 'mclaren', 'alpine-f1-team',
        'alfa-romeo', 'haas-f1-team', 'aston-martin', 'alphatauri', 'williams'
    ]
    for team in teams:
        chromeDriver.get(
            "https://www.racing-statistics.com/en/f1-constructors/compare/" +
            team + "/seasons/2022s")
        content = chromeDriver.page_source
        soup = BeautifulSoup(content, "html.parser")
        teamDNFs = []
        thCounter = 0
        tdCounter = 0

        for table in soup.findAll('table', attrs={'class': 'bottommargin'}):
            for tr in table.findAll('tr'):
                for th in tr.findAll('th'):
                    if thCounter == 1:
                        teamDNFs.append(th.text.strip())
                        thCounter = 0
                    else:
                        thCounter += 1
                for td in tr.findAll('td'):
                    if tdCounter == 1:
                        teamDNFs.append(td.text.strip())
                        tdCounter = 0
                    else:
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
    teams = [
        'Red-bull', 'Ferrari', 'Mercedes', 'Mclaren', 'Alpine', 'Alfa-romeo',
        'Haas', 'Aston Martin', 'Alphatauri', 'Williams'
    ]
    for team in teams:
        chromeDriver.get("https://www.formula1points.com/team/" + team)
        content = chromeDriver.page_source
        soup = BeautifulSoup(content, "html.parser")
        tableCounter = 0
        tdCounter = 0
        teamPoints = []
        teamTotal = 0
        teamPoints.append(team)

        for table in soup.findAll('table', attrs={'class': 'main-table'}):
            if tableCounter == 1:
                for tbody in table.findAll('tbody'):
                    for tr in tbody.findAll('tr'):
                        for td in tr.findAll('td'):
                            if tdCounter == 1:
                                teamTotal = float(td.text.strip())
                                tdCounter += 1
                                break
                            else:
                                tdCounter += 1
                        tableCounter += 1
                        break
            elif tableCounter == 2:
                for tbody in table.findAll('tbody'):
                    for tr in tbody.findAll('tr'):
                        for td in tr.findAll('td'):
                            teamPoints.append(td.text.strip())
                teamPoints.append(teamTotal)
                f1ConstructorsPoints.append(teamPoints)
                break
            else:
                tableCounter += 1


def trackStatsScrapper():
    global trackLinks
    global trackStats
    global trackResults
    global countries
    chromeDriver.get("https://www.racing-statistics.com/en/circuits")
    content = chromeDriver.page_source
    soup = BeautifulSoup(content, "html.parser")
    tdCounter = 0

    for fieldset in soup.findAll('fieldset',
                                 attrs={'class': 'block letterboxlist'}):
        for div in fieldset.findAll('div', attrs={'class': 'letterbox'}):
            for tbody in div.findAll('tbody'):
                for tr in tbody.findAll('tr'):
                    teamLink = []
                    for td in tr.findAll('td'):
                        if tdCounter == 1:
                            teamLink.append(td.text.strip())
                            for a in td.findAll('a', href=True):
                                teamLink.append(str(a['href']))
                            trackLinks.append(teamLink)
                            tdCounter = 0
                        else:
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

        for div in soup.findAll('div',
                                attrs={
                                    'class':
                                    'layout',
                                    'itemtype':
                                    'http://schema.org/TouristAttraction'
                                }):
            for innerdiv in div.findAll('div'):
                if divCounter == 0:
                    for tbody in innerdiv.findAll('tbody'):
                        if tbodyCounter == 0:
                            for tr in tbody.findAll(
                                    'tr', attrs={'itemprop': 'address'}):
                                for td in tr.findAll('td'):
                                    trackStatsTemp.append(td.text.strip())
                                    countries.append(td.text.strip())
                            tbodyCounter += 1
                        elif tbodyCounter == 1:
                            for tr in tbody.findAll('tr'):
                                for td in tr.findAll('td'):
                                    trackStatsTemp.append(td.text.strip())
                            tbodyCounter += 1
                    trackStats.append(trackStatsTemp)
                    divCounter += 1
                elif divCounter == 4:
                    for tbody in innerdiv.findAll('tbody'):
                        for tr in tbody.findAll('tr'):
                            tdCounter = 0
                            trackResultsTemp = []
                            trackResultsTemp.append(track[0])
                            for td in tr.findAll('td'):
                                if tdCounter == 1:
                                    trackResultsTemp.append(td.text.strip())
                                    tdCounter += 1
                                elif tdCounter == 4:
                                    trackResultsTemp.append(td.text.strip())
                                    tdCounter += 1
                                elif tdCounter == 5:
                                    trackResultsTemp.append(td.text.strip())
                                    tdCounter += 1
                                elif tdCounter == 8:
                                    trackResultsTemp.append(td.text.strip())
                                    tdCounter += 1
                                elif tdCounter == 9:
                                    trackResultsTemp.append(td.text.strip())
                                    tdCounter += 1
                                else:
                                    tdCounter += 1
                            trackResults.append(trackResultsTemp)
                    divCounter += 1
                else:
                    divCounter += 1


def getTeamID(teamName):
    if teamName == 'Red Bull':
        return 1
    elif teamName == 'Ferrari':
        return 2
    elif teamName == 'Mercedes':
        return 3
    elif teamName == 'McLaren':
        return 4
    elif teamName == 'Alpine F1 Team':
        return 5
    elif teamName == 'Alfa Romeo':
        return 6
    elif teamName == 'Haas F1 Team':
        return 7
    elif teamName == 'Aston Martin':
        return 8
    elif teamName == 'AlphaTauri':
        return 9
    elif teamName == 'Williams':
        return 10
    else:
        print("This team name was not found: " + teamName)
        return 0


def getTeamName(teamName):
    if teamName == 'Red Bull':
        return 'Oracle Red Bull Racing'
    elif teamName == 'Red-bull':
        return 'Oracle Red Bull Racing'
    elif teamName == 'Ferrari':
        return 'Scuderia Ferrari'
    elif teamName == 'Mercedes':
        return 'Mercedes-AMG Petronas F1 Team'
    elif teamName == 'McLaren':
        return 'McLaren F1 Team'
    elif teamName == 'Mclaren':
        return 'McLaren F1 Team'
    elif teamName == 'Alpine F1 Team':
        return 'BWT Alpine F1 Team'
    elif teamName == 'Alpine':
        return 'BWT Alpine F1 Team'
    elif teamName == 'Alfa Romeo':
        return 'Alfa Romeo F1 Team ORLEN'
    elif teamName == 'Alfa-romeo':
        return 'Alfa Romeo F1 Team ORLEN'
    elif teamName == 'Haas F1 Team':
        return 'Haas F1 Team'
    elif teamName == 'Haas':
        return 'Haas F1 Team'
    elif teamName == 'Aston Martin':
        return 'Aston Martin Aramco Cognizant F1 Team'
    elif teamName == 'Aston-Martin':
        return 'Aston Martin Aramco Cognizant F1 Team'
    elif teamName == 'AlphaTauri':
        return 'Scuderia AlphaTauri'
    elif teamName == 'Alphatauri':
        return 'Scuderia AlphaTauri'
    elif teamName == 'Williams':
        return 'Williams Racing'
    else:
        print("This team name was not found: " + teamName)
        return teamName
