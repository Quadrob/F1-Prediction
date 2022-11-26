from flask import request_finished
import requests
import pandas as pd

def raceDataCollection(DATABASECONNECTION, limit=1000):
    """ This function collects all the race data required by the application from the Ergast API. 
    It creates the 'races' database table, populates it with all the data, and returns the races dataframe. """
    if limit > 1000:
        print("Max limit for the API is 1000.")
        return
        
    # Setup DB config
    databaseCursor = DATABASECONNECTION.cursor()


    # Query Ergast F1 API for races data collection
    races = {'season': [],
            'round': [],
            'circuit_id': [],
            'lat': [],
            'long': [],
            'country': [],
            'date': [],
            'url': []}

    try:
        print("Fetching race data.")
        url = 'https://ergast.com/api/f1/races.json?limit={}'
        request = requests.get(url.format(limit))
        request.raise_for_status()
        json = request.json()
        offset = limit
        while offset < int(json['MRData']['total']):
            print("There are more than " + str(limit) + " races so i will make another request to get the next " + str(limit) + " races. I have to do this because of the API limiter set to a max of 1000.")
            url = 'https://ergast.com/api/f1/races.json?limit={}&offset={}'
            request = requests.get(url.format(limit, offset))
            request.raise_for_status()
            for item in request.json()['MRData']['RaceTable']['Races']:
                json['MRData']['RaceTable']['Races'].append(item)
            offset += limit
    except Exception as e:
        print('There was an error fetching race data: ' + str(e))

    for item in json['MRData']['RaceTable']['Races']:
        try:
            races['season'].append(int(item['season']))
        except:
            races['season'].append(None)

        try:
            races['round'].append(int(item['round']))
        except:
            races['round'].append(None)

        try:
            races['circuit_id'].append(item['Circuit']['circuitId'])
        except:
            races['circuit_id'].append(None)

        try:
            races['lat'].append(float(item['Circuit']['Location']['lat']))
        except:
            races['lat'].append(None)

        try:
            races['long'].append(float(item['Circuit']['Location']['long']))
        except:
            races['long'].append(None)

        try:
            races['country'].append(item['Circuit']['Location']['country'])
        except:
            races['country'].append(None)

        try:
            races['date'].append(item['date'])
        except:
            races['date'].append(None)

        try:
            races['url'].append(item['url'])
        except:
            races['url'].append(None)


    # Create dataframe
    races = pd.DataFrame(races)

    
    if (races.shape[0] > 0 and races.empty != True):
        # Check data
        print(races.head())
        print(races.tail())
        print(races.info())
        print(races.describe())

        # Create/Replace races table with dataframe
        races.to_sql('races', DATABASECONNECTION, if_exists='replace', index=True, index_label='raceID')
        DATABASECONNECTION.commit()
        databaseCursor.close()
        databaseCursor = None
    else:
        print("There was an error fetching races data!")
