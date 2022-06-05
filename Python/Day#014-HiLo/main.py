""" Hi-LO
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.06.02-2012 """
import sys
from random import choice as pick
import art, game_data


def challengers():
    data = game_data.data
    challenger = pick(data)
    return challenger


def play_again():
    choice = input("Want to play again?: ")
    if choice.startswith('y'):
        game_loop()

    else:
        sys.exit()


def game_loop():
    game_over = False
    score = 0
    A = challengers()
    B = challengers()
    if A == B:
        B = challengers()

    else:
        while not game_over:
            print(art.logo)
            print(f"Your current score is {score}!")
            print(f"{A['name']} is a {A['description']} from {A['country']}\n")
            print(art.vs)
            print(f"{B['name']} is a {B['description']} from {B['country']}")
            guess = input("Which has more followers A or B?: ")
            guess.upper()
            if guess == 'A' and A['follower_count'] > B['follower_count']:
                print(f"That's right! {A['name']} has {A['follower_count']} followers!")
                score += 1
                A = A
                B = challengers()
                if A == B:
                    B = challengers()
                else:
                    pass

            elif guess == 'A' and A['follower_count'] < B['follower_count']:
                print(f"Too bad {B['name']} has {B['follower_count']} followers! Better luck next time you got {score} guesses right!")
                game_over = True

            elif guess == "B" and B['follower_count'] > A['follower_count']:
                print(f"That's right! {B['name']} has {B['follower_count']} followers!")
                score += 1
                A = B
                B = challengers()
                if A == B:
                    B = challengers()
                else:
                    pass

            elif guess == "B" and B['follower_count'] < A['follower_count']:
                print(f"Too bad {A['name']} has {A['follower_count']} Followers! Better luck next time you got {score} guesses right!")
                game_over = True

            else:
                print("That's not a valid choice try again!!")


game_loop()
