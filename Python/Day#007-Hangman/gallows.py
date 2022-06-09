""" OOP Practice Hangman refactor """

import random
import hangman_art
import re
import sys


class Hanged():
    words = open('words.txt', 'r').readlines()
