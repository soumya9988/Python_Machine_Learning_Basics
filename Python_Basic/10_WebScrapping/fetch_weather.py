import json
import requests

# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.openweathermap.org/data/2.5/weather?id=4719457&appid=83fb3a2054436c4d844fac1c7bb099f6'
response = requests.get(url)
try:
    response.raise_for_status()
    json_to_python = json.loads(response.text)
    print(json_to_python)

    place = json_to_python['name']

    weather_data  = json_to_python['main']['temp']
    print(weather_data)
    current_temp_in_cel = weather_data - 273.15

    weather_desc = json_to_python['weather'][0]['description']

    print('Current temperature %s is %d '% (place, int(current_temp_in_cel)))
    print('Currently the weather is', weather_desc)

except Exception as ex:
    print('Error while opening weather app:', ex)


