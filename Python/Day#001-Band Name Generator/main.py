""" Band name generator
    By TechGYQ
    www.mythosworks.com
    OC:2022.04.12-2021 """

# Imports
import os
from random import choice

a_file = open("adjectives.txt", "r")
a_list = a_file.readlines()
a_file.close()
b_file = open("nouns.txt", "r")
b_list = b_file.readlines()
b_file.close()

energy = choice(a_list)
soul = choice(b_list)
band = energy.title().strip() + " " + soul.title().strip()
print(band)

# TODO: set question to try again.