""" Blackjack
    Coded by TechGYQ
    www.mythosworks.com
    OC:2022.05.21-2009 """

import os
from random import choice as pick
import sys


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = pick(cards)
    return card


def clear_screen():
    """Clears the current console."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 80)


def get_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def game_check(player_score, dealer_score):
    if player_score == dealer_score:
        return "It's a draw!"

    elif dealer_score == 0:
        return "House has blackjack!"

    elif player_score == 0:
        return "Blackjack! You win!"

    elif player_score > 21:
        return "Bust! You lose!"

    elif dealer_score > 21:
        return "House busts!"

    elif player_score > dealer_score:
        return f"You win with {player_score}"

    else:
        return "House wins!"


def kill():
    sys.exit()


def new_hand():
    game_over = False
    player_cards = []
    dealer_cards = []

    for i in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())


def game_loop():
    player_cards = []
    dealer_cards = []
    game_over = False

    for i in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        player_score = get_score(player_cards)
        dealer_score = get_score(dealer_cards)
        print(f"You hand: {player_cards}, Totaling: {player_score}")
        print(f"House is showing a {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
            new_hand()

        else:
            hit = input("Would you like another card? ")
            if hit.startswith("y"):
                player_cards.append(deal_card())

            else:
                game_over = True
                new_hand()

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = get_score(dealer_cards)

    print(game_check(player_score, dealer_score))


while input("Play another hand? ") == "y":
    clear_screen()
    game_loop()
