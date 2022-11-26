import time
import requests
import pandas as pd


def constructorDataCollection(DATABASECONNECTION, rounds):
    """ This function collects all the constructor standing data from Ergast API and creats as well as populates the constructors standings database table. """
    # start from year 1958 because the Constructors championship was only awarded for the first time in 1958 so there is no data prior to that year
    constructor_rounds = rounds[8:]
    
    # Setup DB config
    databaseCursor = DATABASECONNECTION.cursor()

    # Query Ergast F1 API for constructor standings data collection
    constructor_standings = {'season': [],
                            'round':[],
                            'constructor': [],
                            'constructor_points': [],
                            'constructor_wins': [],
                            'constructor_standings_pos': []}


    for arrayIndex in list(range(len(constructor_rounds))):
        for seasonRound in constructor_rounds[arrayIndex][1]:
        
            print("Fetching constructor standing data for year: " + str(constructor_rounds[arrayIndex][0]) + " round: " + str(seasonRound))
            url = 'https://ergast.com/api/f1/{}/{}/constructorStandings.json'
            request = requests.get(url.format(constructor_rounds[arrayIndex][0], seasonRound))
            json = request.json()
            
            # I added this sleep because of the limited amount of requests i can make on this API. I sleep for the same amount as the round i am fetching thus the timer will be longer the further in a season the application gets
            time.sleep(int(seasonRound) / 2)

            try:    
                for item in json['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']:
                    try:
                        constructor_standings['season'].append(int(json['MRData']['StandingsTable']['StandingsLists'][0]['season']))
                    except:
                        constructor_standings['season'].append(None)

                    try:
                        constructor_standings['round'].append(int(json['MRData']['StandingsTable']['StandingsLists'][0]['round']))
                    except:
                        constructor_standings['round'].append(None)
                                                
                    try:
                        constructor_standings['constructor'].append(item['Constructor']['constructorId'])
                    except:
                        constructor_standings['constructor'].append(None)
                    
                    try:
                        constructor_standings['constructor_points'].append(int(item['points']))
                    except:
                        constructor_standings['constructor_points'].append(None)
                    
                    try:
                        constructor_standings['constructor_wins'].append(int(item['wins']))
                    except:
                        constructor_standings['constructor_wins'].append(None)
                        
                    try:
                        constructor_standings['constructor_standings_pos'].append(int(item['position']))
                    except:
                        constructor_standings['constructor_standings_pos'].append(None)

            except IndexError as e:
                print("There is no data for constructor standings year: " + str(json['MRData']['StandingsTable']['season']) + " round: " + str(json['MRData']['StandingsTable']['round']))
                continue
            except Exception as e:
                print("There was and error reading constrructor standings data, please have a look at it urgently! Stacktrace: " + str(e))
                continue


    # Create dataframe and modify it
    constructor_standings = pd.DataFrame(constructor_standings)
    constructor_standings = lookup(constructor_standings, 'constructor', 'constructor_points')
    constructor_standings = lookup(constructor_standings, 'constructor', 'constructor_wins')
    constructor_standings = lookup(constructor_standings, 'constructor', 'constructor_standings_pos')
    constructor_standings.drop(['constructor_points_after_race', 'constructor_wins_after_race','constructor_standings_pos_after_race' ], axis = 1, inplace = True)
    
    
    if (constructor_standings.shape[0] > 0 and constructor_standings.empty != True):
        # Check data
        print(constructor_standings.head())
        print(constructor_standings.tail())
        print(constructor_standings.info())
        print(constructor_standings.describe())

        # Create/Replace driver standings table with dataframe
        constructor_standings.to_sql('constructor_standings', DATABASECONNECTION, if_exists='replace', index=True, index_label='constructor_standingsID')
        DATABASECONNECTION.commit()
        databaseCursor.close()
        databaseCursor = None
        
    else:
        print("There was an error fetching constructor standings data!")


# define lookup function to shift points and number of wins from previous rounds to the next round because the points are only awarded after the race
def lookup (dataframe, team, columnName):
    """ A lookup function to shift points and number of wins from previous rounds to the next round because the points are only awarded after the race. """
    dataframe['lookup1'] = dataframe.season.astype(str) + dataframe[team] + dataframe['round'].astype(str)
    dataframe['lookup2'] = dataframe.season.astype(str) + dataframe[team] + (dataframe['round']-1).astype(str)
    new_dataframe = dataframe.merge(dataframe[['lookup1', columnName]], how = 'left', left_on='lookup2', right_on='lookup1')
    new_dataframe.drop(['lookup1_x', 'lookup2', 'lookup1_y'], axis = 1, inplace = True)
    new_dataframe.rename(columns = {columnName+'_x': columnName+'_after_race', columnName+'_y': columnName}, inplace = True)
    new_dataframe[columnName].fillna(0, inplace = True)
    return new_dataframe
