import requests
import pandas as pd

def resultsDataCollection(DATABASECONNECTION, limit=1000):
    """ This function collects all the results data of each race from Ergast API and creats as well as populates the results database table. """
    if limit > 1000:
        print("Max limit for the API is 1000.")
        return
        
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
                'url': [],
                'fastest_lap_rank': [],
                'fastest_lap_time': [],
                'avg_speed': []}

    try:
        print("Fetching results data.")
        url = 'https://ergast.com/api/f1/results.json?limit={}'
        request = requests.get(url.format(limit))
        request.raise_for_status()
        json = request.json()
        offset = limit
        while offset < int(json['MRData']['total']):
            print("There are more results so I will make another request to get the next " + str(limit) + " resuts.")
            url = 'https://ergast.com/api/f1/results.json?limit={}&offset={}'
            request = requests.get(url.format(limit, offset))
            request.raise_for_status()
            for item in request.json()['MRData']['RaceTable']['Races']:
                json['MRData']['RaceTable']['Races'].append(item)
            offset += limit
    except Exception as e:
        print('There was an error fetching result data: ' + str(e))

    try:
        for item in json['MRData']['RaceTable']['Races']:
            for result in item['Results']:
                try:
                    results['season'].append(int(item['season']))
                except:
                    results['season'].append(None)

                try:
                    results['round'].append(int(item['round']))
                except:
                    results['round'].append(None)

                try:
                    results['circuit_id'].append(item['Circuit']['circuitId'])
                except:
                    results['circuit_id'].append(None)

                try:
                    results['driver'].append(result['Driver']['driverId'])
                except:
                    results['driver'].append(None)

                try:
                    fullName = str(result['Driver']['givenName']) + " " + str(result['Driver']['familyName'])
                    results['driver_full_name'].append(fullName)
                except:
                    results['driver_full_name'].append(None)
                
                try:
                    results['date_of_birth'].append(result['Driver']['dateOfBirth'])
                except:
                    results['date_of_birth'].append(None)
                    
                try:
                    results['nationality'].append(result['Driver']['nationality'])
                except:
                    results['nationality'].append(None)

                try:
                    results['constructor'].append(result['Constructor']['constructorId'])
                except:
                    results['constructor'].append(None)
                    
                try:
                    results['constructor_nationality'].append(result['Constructor']['nationality'])
                except:
                    results['constructor_nationality'].append(None)

                try:
                    results['grid'].append(int(result['grid']))
                except:
                    results['grid'].append(None)

                try:
                    results['time'].append(int(result['Time']['millis']))
                except:
                    results['time'].append(None)

                try:
                    results['status'].append(result['status'])
                except:
                    results['status'].append(None)

                try:
                    results['points'].append(int(result['points']))
                except:
                    results['points'].append(None)

                # TODO I should rename this to position not podium
                try:
                    results['podium'].append(int(result['position']))
                except:
                    results['podium'].append(None)

                try:
                    results['url'].append(item['url'])
                except:
                    results['url'].append(None)
                
                try:
                    results['fastest_lap_rank'].append(int(result['FastestLap']['rank']))
                except:
                    results['fastest_lap_rank'].append(None)
                    
                try:
                    timeInMins = str(result['FastestLap']['Time']['time']).replace('.', '').replace(':', '.')
                    timeInMilli = round(float(timeInMins) * 60 * 1000)
                    results['fastest_lap_time'].append(int(timeInMilli))
                except:
                    results['fastest_lap_time'].append(None)
                    
                try:
                    results['avg_speed'].append(float(result['FastestLap']['AverageSpeed']['speed']))
                except:
                    results['avg_speed'].append(None)
            
    except IndexError as e:
        print("There is no data for results year: " + str(json['MRData']['RaceTable']['season']) + " round: " + str(json['MRData']['RaceTable']['round']))
    except Exception as e:
        print("There was and error reading results data, please have a look at it urgently! Stacktrace: " + str(e))


    # Create dataframe
    results = pd.DataFrame(results)

    
    if (results.shape[0] > 0 and results.empty != True):
        # Check data
        print(results.head())
        print(results.tail())
        print(results.info())
        print(results.describe())

        # Create/Replace results table with dataframe
        results.to_sql('results', DATABASECONNECTION, if_exists='replace', index=True, index_label='resultID')
        DATABASECONNECTION.commit()
        databaseCursor.close()
        databaseCursor = None
    else:
        print("There was an error fetching results data!")
        