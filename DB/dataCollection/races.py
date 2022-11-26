# make parent dir available in child dir
# import os
# import sys
# sys.path.insert(1, os.path.join(sys.path[0], '..'))

import requests
import pandas as pd
import numpy as np

def raceDataCollection(DATABASECONNECTION):
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

    # loop through years
    # TODO should be 1950, 2023
    for year in list(range(2022, 2023)):

        print("Fetching race data for year: " + str(year))
        url = 'https://ergast.com/api/f1/{}.json'
        request = requests.get(url.format(year))
        json = request.json()

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
        print(races.info())
        print(races.describe())

        # Create/Replace races table with dataframe
        races.to_sql('races', DATABASECONNECTION, if_exists='replace', index=True, index_label='raceID')
        DATABASECONNECTION.commit()
        databaseCursor.close()
        databaseCursor = None
        
        # append the number of rounds of each season from the races dataframe
        rounds = []
        for year in np.array(races.season.unique()):
            rounds.append([year, list(races[races.season == year]['round'])])

        # return the amount of rounds for each season
        return rounds
    else:
        print("There was an error fetching races data!")