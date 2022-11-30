import json


import requests



class NoSuchLocation(Exception):
    pass


API = "Ng5QD9BVcbmuDsBPvawXb7QVIekwn0M3"


key = ""

zipcode = input("Enter ZIP: ")


def get_location(zipcode):

    location_url = 'https://dataservice.accuweather.com/locations/v1/' \
                   'postalcodes/search?apikey=' + API + '&q=' + zipcode
    print(location_url)
    response = requests.get(location_url)

    try:
        key = response.json()[0].get('Key')
    except IndexError:
        raise NoSuchLocation()
    return key



def get_conditions(key):
    conditions_url = 'https://dataservice.accuweather.com/currentconditions/v1/' + key + '?apikey=' + API
    response = requests.get(conditions_url)
    json_version = response.json()
    weatherText = json_version[0].get('WeatherText')
    print("Current Conditions: " + weatherText)


def get_forecast(location_key):
    forecast_url = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/' + location_key + '?apikey=' + API
    print(forecast_url)

    response = requests.get(forecast_url)
    json_version = response.json()
    for i in json_version["DailyForecasts"]:
        print("Forecast for: " + i['Date'] + "  ")

        print("Low Temperature: " + int(i['Temperature']['Minimum']['Value']))
        print("High Temperature: " + int(i['Temperature']['Maximum']['Value']))

        print('------------------------------------------------------------')



try:
    location_key = get_location(zipcode)
    get_conditions(location_key)
    get_forecast(location_key)

except NoSuchLocation:
    print("Unable to get the location")
