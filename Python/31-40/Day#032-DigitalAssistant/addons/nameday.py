""" Birthday add-on
    Coded by TechGYQ
    www.mythosworks.com
    2023.11.14-"""

import json
import datetime as dt
import random
from random import choice


def get_nameday():
    # Reads nameday file and makes dict of birthdays.
    f = open('resources/namedays.dat', 'r')
    nameday = json.loads(f.read())
    c = open('resources/birthday_cards.dat', 'r')
    cards = json.loads(c.read())

    # Grabs today's date & makes variables.
    today = dt.datetime.now()
    year = today.year
    today = str(today)
    for key, value in nameday.items():
        if value[5:7] == today[5:7]:
            if value[9:10] == today[9:10]:
                age = int(year) - int(value[0:4])
                card = random.choice(list(cards.values()))
                card = card.replace("[NAME]", key)
                card = card.replace('[AGE]', str(age))
                return card
