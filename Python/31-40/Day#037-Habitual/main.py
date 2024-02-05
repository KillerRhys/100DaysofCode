""" Habitual: The Habit Tracker
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.02.04-1647 """

# Imports.
import requests
import os
from datetime import datetime as dt

# Constants.
USERNAME = "techgyq"
TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# Setup account.
create_user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(PIXELAENDPOINT, json=create_user_parameters)
# print(response.text)

# Create graph.
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": "graph0",
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "ajisai",

}

# response = requests.post(GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# Post data to graph.
today = dt.today()
DATA_ENDPOINT = f"{GRAPH_ENDPOINT}/graph0"
pixel_post = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "80",
}

# response = requests.post(DATA_ENDPOINT, json=pixel_post, headers=HEADERS)
# print(response.text)

# Update / Delete pixels.
UPDATE_ENDPOINT = f"{DATA_ENDPOINT}/20240203"
update_data = {
    "quantity": "90",
}

# response = requests.put(UPDATE_ENDPOINT, json=update_data, headers=HEADERS)
# print(response.text)

# response = requests.delete(UPDATE_ENDPOINT, headers=HEADERS)
# print(response.text)
