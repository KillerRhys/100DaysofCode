import requests
import os

api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
PARAMETERS = {
    "lat": 39.554920,
    "lon": -84.304611,
    "appid": os.environ.get("OWM_API_KEY"),
    "cnt": 4,
    "units": "Imperial",

}

response = requests.get(api_endpoint, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()

rain_coming = False
weather = weather_data['list']
for item in weather:
    if item['weather'][0]['id'] < 600:
        rain_coming = True

if rain_coming:
    print("It's gon rain!!")
