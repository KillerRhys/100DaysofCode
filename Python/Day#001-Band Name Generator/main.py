""" Band name generator
    By TechGYQ
    www.mythosworks.com
    OC:2022.04.12-2021 """

# Imports
import os
import sys
from random import choice


def new_name():
    choice = input("Want to try again?: ")
    if choice.startswith('y'):
        name_loop()

    else:
        sys.exit()


def name_loop():
    print("Welcome to band name generator here we go!!\n")
    a_file = open("adjectives.txt", "r")
    a_list = a_file.readlines()
    a_file.close()
    b_file = open("nouns.txt", "r")
    b_list = b_file.readlines()
    b_file.close()

    energy = choice(a_list)
    soul = choice(b_list)
    band = energy.title().strip() + " " + soul.title().strip()
    print(f"Your most awesome band name is...: {band}!! \n")
    new_name()


name_loop()