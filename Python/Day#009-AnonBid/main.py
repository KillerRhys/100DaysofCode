""" AnonBid
    Coded by TechGYQ
    www.mythosworks.com
    OC:2022.05.18-2020 """

import os
from art import logo as img

bids = {}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 80)


def grab_winner():
    highest = 0
    winner = ""
    for key in bids:
        if bids[key] > highest:
            highest = bids[key]
            winner = key
        else:
            highest = highest
            print(f"{winner} won with a bid of ${bids[winner]:.2f}")


def app_run():
    clear_screen()
    print(img + "\n"* 1)
    name = input("Please enter your name. \n")
    bid = float(input("Please enter your bid. \n"))
    bids[name] = bid
    nxt = input("Is there another bidder? \n")
    nxt.lower()
    if nxt.startswith("y"):
        app_run()

    else:
        grab_winner()

app_run()
