from bs4 import BeautifulSoup
import requests
import pandas as pd

# TODO remove import
import Database

def qualifyingDataCollection(DATABASECONNECTION):
    """ This function collects all the qualifying data """
    # Setup DB config
    databaseCursor = DATABASECONNECTION.cursor()

    qualifying_results = pd.DataFrame()

    # Qualifying times are only available from 1983 on the f1 official website
    # TODO should be 1983, 2023
    for year in list(range(1983,2023)):
        url = 'https://www.formula1.com/en/results.html/{}/races.html'
        request = requests.get(url.format(year))
        soup = BeautifulSoup(request.text, 'html.parser')
        
        # find links to all circuits for a certain year
        year_links = []
        for page in soup.find_all('a', attrs = {'class':"resultsarchive-filter-item-link FilterTrigger"}):
            link = page.get('href')
            if f'/en/results.html/{year}/races/' in link: 
                year_links.append(link)

        # for each circuit, switch to the starting grid page and read table data into application
        year_dataframe = pd.DataFrame()
        new_url = 'https://www.formula1.com{}'
        
        for round, link in list(enumerate(year_links)):
            print("Fetching qualifying data for year: " + str(year) + " round: " + str(int(round) + 1))
            try:
                link = link.replace('race-result.html', 'starting-grid.html')
                dataframe = pd.read_html(new_url.format(link))
                dataframe = dataframe[0]
                dataframe['season'] = year
                dataframe['round'] = round+1
                for col in dataframe:
                    if 'Unnamed' in col:
                        dataframe.drop(col, axis = 1, inplace = True)

                year_dataframe = pd.concat([year_dataframe, dataframe])
            
            except ValueError as e:
                print("There is no qualifying data for year: " + str(year) + " round: " + str(int(round) + 1))
                continue
            except Exception as e:
                print("There was and error reading qualifying data, please have a look at it urgently! Stacktrace: " + str(e))
                continue

        # concatenate all tables from all years 
        qualifying_results = pd.concat([qualifying_results, year_dataframe])

    # rename dataframe columns
    # TODO rename car to constructor
    qualifying_results.rename(columns = {'Pos': 'grid', 'Driver': 'driver_name', 'Car': 'car', 'Time': 'qualifying_time'}, inplace = True)
    # drop driver number column
    qualifying_results.drop('No', axis = 1, inplace = True)

    qualifying_results = stringToMilliseconds(qualifying_results)

    if (qualifying_results.shape[0] > 0 and qualifying_results.empty != True):
        # Check data
        print(qualifying_results.head())
        print(qualifying_results.tail())
        print(qualifying_results.info())
        print(qualifying_results.describe())

        # Create/Replace qualifying table with dataframe
        qualifying_results.to_sql('qualifying', DATABASECONNECTION, if_exists='replace', index=True, index_label='qualifyingID')
        DATABASECONNECTION.commit()
        databaseCursor.close()
        databaseCursor = None
        
    else:
        print("There was an error fetching qualifying data!")

# A time coverter method to convert the qualifying times to milliseconds
def stringToMilliseconds(qualifying_results):
    """"Convert a time string in minutes to a millisecond value."""
    for index, row in qualifying_results.iterrows():
        try:
            timeInMins = str(row['qualifying_time'].value).replace('.', '').replace(':', '.')
            timeInMilli = round(float(timeInMins) * 60 * 1000)
            qualifying_results.at[index, 'qualifying_milliseconds'] = timeInMilli
            print("Added " + str(timeInMilli) + " milliseconds to row: " + str(index) + " that has data: " + str(row))
        except Exception as e:
            print("Could not convert time to milliseconds because of: " + str(e))
            qualifying_results.at[index, 'qualifying_milliseconds'] = None
            continue
    return qualifying_results


# TODO remove this testing stuff
Database.connectToDatabase()
qualifying = pd.read_sql_query('''SELECT * FROM qualifying''', Database.DATABASECONNECTION)
stringToMilliseconds(qualifying)
Database.disconnectFromDatabase()