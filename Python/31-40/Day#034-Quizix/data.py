""" Question Fetch API Call
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.01.22-2030 """

import requests
PARAMETERS = {
    "amount" : 10,
    "type" : "boolean",
}

# Open Trivia Database API.
API_URL = "https://opentdb.com/api.php"


# Function to grab 10 new questions.
def get_questions():
    response = requests.get(url=API_URL, params=PARAMETERS)
    response.raise_for_status()
    question_data = response.json()["results"]
    return question_data
