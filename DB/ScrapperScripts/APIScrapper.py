import requests
import json


F1Manager22RatingsData = []


def f1Manager22DriverRatings():
    global F1Manager22RatingsData
    response_API = requests.get(
        'https://ratings-api.ea.com/v2/entities/f1-22-drivers-ratings')
    jsonDriversObject = json.loads(response_API.text)
    numOfDrivers = jsonDriversObject['count']
    for driverNum in range(numOfDrivers):
        driverData = []
        driverData.append(
            jsonDriversObject['docs'][driverNum]['fullNameForSearch'])

        BDate = jsonDriversObject['docs'][driverNum]['birthdate'].split(' ')
        driverData.append(BDate[0])

        driverData.append(
            jsonDriversObject['docs'][driverNum]['nationality'])
        driverData.append(
            jsonDriversObject['docs'][driverNum]['overall_rating'])
        F1Manager22RatingsData.append(driverData)
