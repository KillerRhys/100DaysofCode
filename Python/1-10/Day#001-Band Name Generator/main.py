""" Band name generator
    By TechGYQ
    www.mythosworks.com
    OC:2022.04.12-2021 """

# Imports
import os
import sys
from Rocker import BandGenerator
yoi = BandGenerator()
getting_name = True


while getting_name:
    answer = input("Want to get an awesome name?! ")
    if answer.startswith('y'):
        yoi.name()
        print()

    else:
        sys.exit()