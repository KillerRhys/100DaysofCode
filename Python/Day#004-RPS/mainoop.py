""" OOP Practice! """

import sys, os
from game import GamePlay
tati = GamePlay()
game_over = False

while not game_over:
    tati.game_loop()