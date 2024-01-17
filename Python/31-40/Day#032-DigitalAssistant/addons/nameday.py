""" Birthday add-on
    Coded by TechGYQ
    www.mythosworks.com
    2023.11.14-"""

import json
import datetime as dt
import random


def get_nameday():
    # Reads nameday file and makes dict of birthdays.
    f = open('resources/namedays.dat', 'r')
    nameday = json.loads(f.read())
    b = open('resources/blackbook.dat', 'r')
    addresses = json.loads(b.read())
    c = open('resources/birthday_cards.dat', 'r')
    cards = json.loads(c.read())

    # Grabs today's date & makes variables.
    birthdays_today = []
    birthdays_this_month = []
    cards_to_send = []
    postman = []
    today = dt.datetime.now()
    year = today.year
    today = str(today)
    for key, value in nameday.items():
        if value[5:7] == today[5:7]:
            birthdays_this_month.append(key)
            if value[9:10] == today[9:10]:
                birthdays_today.append(key)
                age = int(year) - int(value[0:4])
                address = addresses[key]
                postman.append(address)
                card = random.choice(list(cards.values()))
                card = card.replace("[NAME]", key)
                card = card.replace('[AGE]', str(age))
                cards_to_send.append(card)

    if len(birthdays_today) != 0:
        return cards_to_send, birthdays_today, postman

    else:
        return cards_to_send, birthdays_this_month, postman
