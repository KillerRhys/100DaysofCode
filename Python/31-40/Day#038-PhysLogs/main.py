""" Phys-Logs Smart Workout Tracker
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.03.05-1804 """

# Imports.
import requests
import os
from datetime import datetime as dt

# Constants.
NUTRITIONIX_APPID = os.environ.get("NUTRITIONIX_APPID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API = os.environ.get("SHEETY_API")

# Grab date & time for workouts.
today = dt.now()
date = today.strftime("%Y/%m/%d")
time = today.strftime("%H:%M:%S")

# Headers & Parameters for Nutritionix.
NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_APPID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

NUTRITIONIX_PARAMETERS = {
    "query": input("Tell me what exercises you've done today: "),
    "weight_kg": 145,
    "height_cm": 182,
    "age": 38,
}

nutritionix_response = requests.post(NUTRITIONIX_ENDPOINT, json=NUTRITIONIX_PARAMETERS, headers=NUTRITIONIX_HEADERS)
result = nutritionix_response.json()

for exercise in result['exercises']:
    SHEETY_PARAMETERS = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheety_response = requests.post(SHEETY_API, json=SHEETY_PARAMETERS)

    print(sheety_response.text)
