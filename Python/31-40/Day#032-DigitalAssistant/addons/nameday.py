""" Birthday add-on
    Coded by TechGYQ
    www.mythosworks.com
    2023.11.14-"""


def get_nameday():
    nameday = {}
    with open("resources/namedays.dat") as data:
        for line in data['Nameday']:
            (key, val) = line.split()
            nameday[int(key)] = val

    return nameday
