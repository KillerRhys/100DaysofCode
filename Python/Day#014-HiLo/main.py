""" Hi-LO
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.06.02-2012 """

from random import choice as pick
import art, game_data


def challengers():
    data = game_data.data
    A = pick(data)
    B = pick(data)
    name = A['name']
    count = A['follower_count']
    desc = A['description']
    country = A['country']
    name2 = B['name']
    count2 = B['follower_count']
    desc2 = B['description']
    country2 = B['country']
    return name, count, desc, country, name2, count2, desc2, country2


def game_loop():
    game_over = False
    score = 0
    while not game_over:
        print(f"")


print(challengers())