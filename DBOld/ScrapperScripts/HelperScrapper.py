
def getTeamCountry(teamName):
	if teamName == 'Oracle Red Bull Racing':
		return 'Austria'
	elif teamName == 'Scuderia Ferrari':
		return 'Italy'
	elif teamName == 'Mercedes-AMG Petronas F1 Team':
		return 'Germany'
	elif teamName == 'McLaren F1 Team':
		return 'United Kingdom of Great Britain and Northern Ireland'
	elif teamName == 'BWT Alpine F1 Team':
		return 'France'
	elif teamName == 'Alfa Romeo F1 Team ORLEN':
		return 'Switzerland'
	elif teamName == 'Haas F1 Team':
		return 'United States of America'
	elif teamName == 'Aston Martin Aramco Cognizant F1 Team':
		return 'United Kingdom of Great Britain and Northern Ireland'
	elif teamName == 'Scuderia AlphaTauri':
		return 'Italy'
	elif teamName == 'Williams Racing':
		return 'United Kingdom of Great Britain and Northern Ireland'
	else:
		print("This team name was not found: " + teamName)
		return None


def getDriverCountry(driverName):
	if driverName == 'Max Verstappen':
		return 'Netherland'
	elif driverName == 'Charles Leclerc':
		return 'Monaco'
	elif driverName == 'Sergio Pérez':
		return 'Mexico'
	elif driverName == 'George Russell':
		return 'United Kingdom of Great Britain and Northern Ireland'
	elif driverName == 'Carlos Sainz':
		return 'Spain'
	elif driverName == 'Lewis Hamilton':
		return 'United Kingdom of Great Britain and Northern Ireland'
	elif driverName == 'Lando Norris':
		return 'United Kingdom of Great Britain and Northern Ireland'
	elif driverName == 'Esteban Ocon':
		return 'France'
	elif driverName == 'Fernando Alonso':
		return 'Spain'
	elif driverName == 'Valtteri Bottas':
		return 'Finland'
	elif driverName == 'Pierre Gasly':
		return 'France'
	elif driverName == 'Kevin Magnussen':
		return 'Denmark'
	elif driverName == 'Sebastian Vettel':
		return 'Germany'
	elif driverName == 'Daniel Ricciardo':
		return 'Australia'
	elif driverName == 'Mick Schumacher':
		return 'Germany'
	elif driverName == 'Yuki Tsunoda':
		return 'Japan'
	elif driverName == 'Guanyu Zhou':
		return 'China'
	elif driverName == 'Lance Stroll':
		return 'Canada'
	elif driverName == 'Alexander Albon':
		return 'Thailand'
	elif driverName == 'Nyck de Vries':
		return 'Netherland'
	elif driverName == 'Nicholas Latifi':
		return 'Canada'
	elif driverName == 'Nico Hülkenberg':
		return 'Germany'
	else:
		print("This driver name was not found: " + driverName)
		return None


def getCountryWeatherID(country):
	if country == 'Austria':
		return 3
	if country == 'Australia':
		return 5
	if country == 'Morocco':
		return 5
	if country == 'United Kingdom of Great Britain and Northern Ireland':
		return 2
	if country == 'Portugal':
		return 5
	if country == 'Italy':
		return 6
	if country == 'Mexico':
		return 1
	if country == 'Brazil':
		return 11
	if country == 'Argentina':
		return 1
	if country == 'Germany':
		return 1
	if country == 'Bahrain':
		return 11
	if country == 'Azerbaijan':
		return 1
	if country == 'India':
		return 11
	if country == 'France':
		return 1
	if country == 'Switzerland':
		return 12
	if country == 'Spain':
		return 1
	if country == 'Monaco':
		return 2
	if country == 'Belgium':
		return 10
	if country == 'Canada':
		return 3
	if country == 'United States of America':
		return 6
	if country == 'Netherland':
		return 9
	if country == 'Japan':
		return 10
	if country == 'Vietnam':
		return 5
	if country == 'Hungary':
		return 9
	if country == 'Turkey':
		return 3
	if country == 'Saudi Arabia':
		return 9
	if country == 'Korea (Republic of)':
		return 2
	if country == 'South Africa':
		return 1
	if country == 'Qatar':
		return 11
	if country == 'Singapore':
		return 6
	if country == 'Sweden':
		return 12
	if country == 'Malaysia':
		return 11
	if country == 'China':
		return 5
	if country == 'Russia':
		return 9
	if country == 'Abu Dhabi':
		return 11
	if country == 'Thailand':
		return 11
	if country == 'Denmark':
		return 12
	if country == 'Finland':
		return 12
	else:
		print("This country was not found: " + country)
		return 0
