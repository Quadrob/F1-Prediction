import requests
import pandas as pd

def resultsDataCollection(DATABASECONNECTION, rounds):
    # Setup DB config
    databaseCursor = DATABASECONNECTION.cursor()

    # Query Ergast F1 API for results data collection
    results = {'season': [],
                'round':[],
                'circuit_id':[],
                'driver': [],
                'driver_full_name': [],
                'date_of_birth': [],
                'nationality': [],
                'constructor': [],
                'constructor_nationality': [],
                'grid': [],
                'time': [],
                'status': [],
                'points': [],
                'podium': [],
                'fastest_lap_rank': [],
                'fastest_lap_time': [],
                'avg_speed': []}

    for arrayIndex in list(range(len(rounds))):
        for seasonRound in rounds[arrayIndex][1]:
        
            print("Fetching result data for year: " + str(rounds[arrayIndex][0]) + " round: " + str(seasonRound))
            url = 'http://ergast.com/api/f1/{}/{}/results.json'
            request = requests.get(url.format(rounds[arrayIndex][0], seasonRound))
            json = request.json()

            try:
                for item in json['MRData']['RaceTable']['Races'][0]['Results']:
                    try:
                        results['season'].append(int(json['MRData']['RaceTable']['Races'][0]['season']))
                    except:
                        results['season'].append(None)

                    try:
                        results['round'].append(int(json['MRData']['RaceTable']['Races'][0]['round']))
                    except:
                        results['round'].append(None)

                    try:
                        results['circuit_id'].append(json['MRData']['RaceTable']['Races'][0]['Circuit']['circuitId'])
                    except:
                        results['circuit_id'].append(None)

                    try:
                        results['driver'].append(item['Driver']['driverId'])
                    except:
                        results['driver'].append(None)

                    try:
                        fullName = str(item['Driver']['givenName']) + " " + str(item['Driver']['familyName'])
                        results['driver_full_name'].append(fullName)
                    except:
                        results['driver_full_name'].append(None)
                    
                    try:
                        results['date_of_birth'].append(item['Driver']['dateOfBirth'])
                    except:
                        results['date_of_birth'].append(None)
                        
                    try:
                        results['nationality'].append(item['Driver']['nationality'])
                    except:
                        results['nationality'].append(None)

                    try:
                        results['constructor'].append(item['Constructor']['constructorId'])
                    except:
                        results['constructor'].append(None)
                        
                    try:
                        results['constructor_nationality'].append(item['Constructor']['nationality'])
                    except:
                        results['constructor_nationality'].append(None)

                    try:
                        results['grid'].append(int(item['grid']))
                    except:
                        results['grid'].append(None)

                    try:
                        results['time'].append(int(item['Time']['millis']))
                    except:
                        results['time'].append(None)

                    try:
                        results['status'].append(item['status'])
                    except:
                        results['status'].append(None)

                    try:
                        results['points'].append(int(item['points']))
                    except:
                        results['points'].append(None)

                    # TODO I should rename this to position not podium
                    try:
                        results['podium'].append(int(item['position']))
                    except:
                        results['podium'].append(None)
                    
                    try:
                        results['fastest_lap_rank'].append(int(item['FastestLap']['rank']))
                    except:
                        results['fastest_lap_rank'].append(None)
                        
                    try:
                        timeInMins = str(item['FastestLap']['Time']['time']).replace('.', '').replace(':', '.')
                        timeInMilli = round(float(timeInMins) * 60 * 1000)
                        results['fastest_lap_time'].append(int(timeInMilli))
                    except:
                        results['fastest_lap_time'].append(None)
                        
                    try:
                        results['avg_speed'].append(float(item['FastestLap']['AverageSpeed']['speed']))
                    except:
                        results['avg_speed'].append(None)

                    
            except IndexError as e:
                print("There is no data for results year: " + str(json['MRData']['RaceTable']['season']) + " round: " + str(json['MRData']['RaceTable']['round']))
                continue
            except Exception as e:
                print("There was and error reading results data, please have a look at it urgently! Stacktrace: " + str(e))
                continue

    
    # Create dataframe
    results = pd.DataFrame(results)

    
    if (results.shape[0] > 0 and results.empty != True):
        # Check data
        print(results.head())
        print(results.info())
        print(results.describe())

        # Create/Replace results table with dataframe
        results.to_sql('results', DATABASECONNECTION, if_exists='replace', index=True, index_label='resultID')
        DATABASECONNECTION.commit()
        databaseCursor.close()
        databaseCursor = None
    else:
        print("There was an error fetching results data!")