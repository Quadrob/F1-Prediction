from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# set driver for chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
names = []
avgpoint = []
totalpoints = []
totalraces = []
currentdriver = []
loadOutRatings = []


def theLoadOutDriverRatings():
    driver.get("https://www.theloadout.com/f1-manager-2022/driver-ratings")
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    for div in soup.findAll('div', attrs={'class': 'entry-content'}):

        for ul in div.findAll('ul'):

            for li in ul.findAll('li'):
                substring = li.text.split(" – ")
                print(substring)


def formula1pointsScrapper():
    driver.get("https://www.formula1points.com/analysis")
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    for table in soup.findAll('table', attrs={'class': 'main-table dataTable', 'id': 'sortingoption'}):

        for row in table.findAll('tr', attrs={'role': 'row'}):
            tdCount = 0
            # get if its a current driver
            if (row.find('th', attrs={'id': 'current'})):
                currentdriver.append(1)
            else:
                currentdriver.append(0)
            # get name
            for a in row.findAll('a'):
                names.append(a.text.strip())
            # get stats
            for td in row.findAll('td'):
                if (tdCount == 0):
                    avgpoint.append(td.text.strip())
                    tdCount += 1
                elif (tdCount == 1):
                    totalpoints.append(td.text.strip())
                    tdCount += 1
                elif (tdCount == 2):
                    totalraces.append(td.text.strip())
                    tdCount = 0


theLoadOutDriverRatings()

try:
    driver.quit()
    driver.close()
except:
    print('Closing Scrapper!')
