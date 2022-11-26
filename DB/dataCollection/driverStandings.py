import time
import requests
import pandas as pd

def driverDataCollection(DATABASECONNECTION, rounds):
    """ This function collects all the driver standing data from Ergast API and creats as well as populates the driver standings database table. """
    # Setup DB config
    databaseCursor = DATABASECONNECTION.cursor()

    # Query Ergast F1 API for driver standings data collection
    driver_standings = {'season': [],
                        'round':[],
                        'driver': [],
                        'driver_points': [],
                        'driver_wins': [],
                        'driver_standings_pos': []}


    for arrayIndex in list(range(len(rounds))):     
        for seasonRound in rounds[arrayIndex][1]:
        
            print("Fetching driver standing data for year: " + str(rounds[arrayIndex][0]) + " round: " + str(seasonRound))
            url = 'https://ergast.com/api/f1/{}/{}/driverStandings.json'
            request = requests.get(url.format(rounds[arrayIndex][0], seasonRound))
            json = request.json()

            # I added this sleep because of the limited amount of requests i can make on this API. I sleep for the same amount as the round i am fetching thus the timer will be longer the further in a season the application gets
            time.sleep(int(seasonRound) / 2)

            # TODO I decided not to include driver ratings becuase there are only ratings for recent drivers which will not help with the machine learning model

            try:
                for item in json['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']:
                    try:
                        driver_standings['season'].append(int(json['MRData']['StandingsTable']['StandingsLists'][0]['season']))
                    except:
                        driver_standings['season'].append(None)

                    try:
                        driver_standings['round'].append(int(json['MRData']['StandingsTable']['StandingsLists'][0]['round']))
                    except:
                        driver_standings['round'].append(None)
                                                
                    try:
                        driver_standings['driver'].append(item['Driver']['driverId'])
                    except:
                        driver_standings['driver'].append(None)
                    
                    try:
                        driver_standings['driver_points'].append(int(item['points']))
                    except:
                        driver_standings['driver_points'].append(None)
                    
                    try:
                        driver_standings['driver_wins'].append(int(item['wins']))
                    except:
                        driver_standings['driver_wins'].append(None)
                        
                    try:
                        driver_standings['driver_standings_pos'].append(int(item['position']))
                    except:
                        driver_standings['driver_standings_pos'].append(None)
                                    
            except IndexError as e:
                print("There is no data for driver standings year: " + str(json['MRData']['StandingsTable']['season']) + " round: " + str(json['MRData']['StandingsTable']['round']))
                continue
            except Exception as e:
                print("There was and error reading driver standings data, please have a look at it urgently! Stacktrace: " + str(e))
                continue


    # Create dataframe and modify it
    driver_standings = pd.DataFrame(driver_standings)
    driver_standings = lookup(driver_standings, 'driver', 'driver_points')
    driver_standings = lookup(driver_standings, 'driver', 'driver_wins')
    driver_standings = lookup(driver_standings, 'driver', 'driver_standings_pos')
    driver_standings.drop(['driver_points_after_race', 'driver_wins_after_race', 'driver_standings_pos_after_race'], axis = 1, inplace = True)

    
    if (driver_standings.shape[0] > 0 and driver_standings.empty != True):
        # Check data
        print(driver_standings.head())
        print(driver_standings.tail())
        print(driver_standings.info())
        print(driver_standings.describe())

        # Create/Replace driver standings table with dataframe
        driver_standings.to_sql('driver_standings', DATABASECONNECTION, if_exists='replace', index=True, index_label='driver_standingsID')
        DATABASECONNECTION.commit()
        databaseCursor.close()
        databaseCursor = None
        
    else:
        print("There was an error fetching driver standings data!")


# define lookup function to shift points and number of wins from previous rounds to the next round because the points are only awarded after the race
def lookup (dataframe, driver, columnName):
    """ A lookup function to shift points and number of wins from previous rounds to the next round because the points are only awarded after the race. """
    dataframe['lookup1'] = dataframe.season.astype(str) + dataframe[driver] + dataframe['round'].astype(str)
    dataframe['lookup2'] = dataframe.season.astype(str) + dataframe[driver] + (dataframe['round']-1).astype(str)
    new_dataframe = dataframe.merge(dataframe[['lookup1', columnName]], how = 'left', left_on='lookup2', right_on='lookup1')
    new_dataframe.drop(['lookup1_x', 'lookup2', 'lookup1_y'], axis = 1, inplace = True)
    new_dataframe.rename(columns = {columnName+'_x': columnName+'_after_race', columnName+'_y': columnName}, inplace = True)
    new_dataframe[columnName].fillna(0, inplace = True)
    return new_dataframe
