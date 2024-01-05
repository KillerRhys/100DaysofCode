""" Birthday add-on
    Coded by TechGYQ
    www.mythosworks.com
    2023.11.14-"""

import json


def get_nameday():
    f = open('resources/namedays.dat', 'r')
    nameday = json.loads(f.read())

    return nameday
