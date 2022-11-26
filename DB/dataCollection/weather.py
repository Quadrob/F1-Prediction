import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def weatherDataCollection(DATABASECONNECTION, races):
    """ This function collects all the weather data """
    # Setup DB config
    databaseCursor = DATABASECONNECTION.cursor()

    weather = races.iloc[:,[0,1,2]]
    info = []
    
    # create chrome driver
    driver = configChromeDriver()

    # read weather data from wikipedia tables
    for link in races.url:
        print("Checking for weather information for: " + str(link))
        try:
            dataframe = pd.read_html(link)[0]
            if 'Weather' in list(dataframe.iloc[:,0]):
                tableRow = list(dataframe.iloc[:,0]).index('Weather')
                info.append(dataframe.iloc[tableRow,1])
            else:
                dataframe = pd.read_html(link)[1]
                if 'Weather' in list(dataframe.iloc[:,0]):
                    tableRow = list(dataframe.iloc[:,0]).index('Weather')
                    info.append(dataframe.iloc[tableRow,1])
                else:
                    dataframe = pd.read_html(link)[2]
                    if 'Weather' in list(dataframe.iloc[:,0]):
                        tableRow = list(dataframe.iloc[:,0]).index('Weather')
                        info.append(dataframe.iloc[tableRow,1])
                    else:
                        dataframe = pd.read_html(link)[3]
                        if 'Weather' in list(dataframe.iloc[:,0]):
                            tableRow = list(dataframe.iloc[:,0]).index('Weather')
                            info.append(dataframe.iloc[tableRow,1])
                        else:
                            # navigate to link with chrome driver
                            driver.get(link)

                            # click italian language button
                            button = driver.find_element_by_link_text('Italiano')
                            button.click()
                            
                            # find weather in italian with selenium
                            clima = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[9]/td').text
                            info.append(clima)
                                    
        except:
            info.append('Weather data not found')

    # close chrome webdriver
    driver = disconnectChromeDriver(driver)
    
    # append column with weather information to dataframe
    weather['weather'] = info

    # set up a dictionary to convert weather information into keywords for ease in the database
    weather_dict = {'weather_warm': ['soleggiato', 'clear', 'warm', 'hot', 'sunny', 'fine', 'mild', 'sereno'],
                    'weather_cold': ['cold', 'fresh', 'chilly', 'cool'],
                    'weather_dry': ['dry', 'asciutto'],
                    'weather_wet': ['showers', 'wet', 'rain', 'pioggia', 'damp', 'thunderstorms', 'rainy'],
                    'weather_cloudy': ['overcast', 'nuvoloso', 'clouds', 'cloudy', 'grey', 'coperto']}

    # map new dataframe according to weather dictionary
    weather_df = pd.DataFrame(columns = weather_dict.keys())
    for col in weather_df:
        weather_df[col] = weather['weather'].map(lambda x: 1 if any(i in weather_dict[col] for i in x.lower().split()) else 0)

    # create final dataframe with all the required columns
    weather_info = pd.concat([weather, weather_df], axis = 1)
    
    if (weather_info.shape[0] > 0 and weather_info.empty != True):
        # Check data
        print(weather_info.head())
        print(weather_info.info())
        print(weather_info.describe())

        # Create/Replace weather table with dataframe
        weather_info.to_sql('weather', DATABASECONNECTION, if_exists='replace', index=True, index_label='weatherID')
        DATABASECONNECTION.commit()
        databaseCursor.close()
        databaseCursor = None
        
    else:
        print("There was an error fetching weather data!")



def configChromeDriver():
    """ This function is used to configure chrome web driver and return an instance. """
    # set driver for chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    # chromeDriver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # TODO Use the below chrome driver for running in the Replit host enviroment
    chromeDriver = webdriver.Chrome(options=chrome_options)
    print('Creating chrome driver!')
    return chromeDriver

def disconnectChromeDriver(chromeDriver):
    """ This function is used to destroy an instnce of the chrome web driver. """
    chromeDriver.quit()
    chromeDriver = None
    print('Closing chrome driver!')
    return chromeDriver
