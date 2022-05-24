""" Blackjack
    Coded by TechGYQ
    www.mythosworks.com
    OC:2022.05.21-2009 """

import os
import random
import sys

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = input("Please enter a name: ")


def game_over():
    game_over.game_over = False


game_over()


def clear_screen():
    """Clears the current console."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 80)


def check_wins():
    if game_start.dealer_score == 21:
        print("House hit blackjack!")
        game_over.game_over = True
        again = input(f"Another hand {user}? ")
        if again.startswith("y"):
            game_over.game_over = False
            game_start()

        else:
            kill()

    elif game_start.player_score == 21:
        print(f"{user} hit blackjack!")
        game_over.game_over = True
        again = input(f"Another hand {user}? ")
        if again.startswith("y"):
            game_over.game_over = False
            game_start()

        else:
            kill()

    elif game_start.player_score > 21:
        print(f"{user} busts!")
        game_over.game_over = True
        again = input(f"Another hand {user}? ")
        if again.startswith("y"):
            game_over.game_over = False
            game_start()

        else:
            kill()

    elif game_start.dealer_score > 21:
        print("House busts!")
        game_over.game_over = True
        again = input(f"Another hand {user}? ")
        if again.startswith("y"):
            game_over.game_over = False
            game_start()

        else:
            kill()

    elif game_start.dealer_score < 17:
        game_start.dealer_hand.append(random.choice(cards))

    elif game_start.turns > 1:
        if game_start.dealer_score > game_start.player_score:
            print(f"House wins with a total of {game_start.dealer_score}. Better luck next time!")
            game_over.game_over = True
            again = input(f"Another hand {user}? ")
            if again.startswith("y"):
                game_over.game_over = False
                game_start()

            else:
                kill()

        elif game_start.player_score > game_start.dealer_score:
            print(f"{user} wins!")
            game_over.game_over = True
            again = input(f"Another hand {user}? ")
            if again.startswith("y"):
                game_over.game_over = False
                game_start()

            else:
                kill()

    else:
        game_loop()


def kill():
    sys.exit()


def new_card():
    game_start.turns += 1
    hit = input(f"Would you like another card {user}? ")
    if hit.startswith("y"):
        game_start.player_hand.append(random.choice(cards))
        print(f"{user} draws a {game_start.player_hand[-1]}")
        get_scores()

    else:
        get_scores()


def get_scores():
    player_cards = []
    dealer_cards = []
    for item in game_start.player_hand:
        player_cards.append(item)

    for item in game_start.dealer_hand:
        dealer_cards.append(item)

    game_start.player_score = sum(player_cards)
    game_start.dealer_score = sum(dealer_cards)
    check_wins()


def game_loop():
    print("\n")
    print(f"Your cards:{game_start.player_hand} with a total of {game_start.player_score}, House shows a {game_start.dealer_hand[0]}")
    new_card()


def game_start():
    game_start.turns = 0
    game_start.player_hand = []
    game_start.player_score = 0
    game_start.dealer_hand = []
    game_start.dealer_score = 0
    for i in range(2):
        game_start.player_hand.append(random.choice(cards))
        game_start.dealer_hand.append(random.choice(cards))

    get_scores()


game_start()
get_scores()

while not game_over.game_over:
    game_loop()
