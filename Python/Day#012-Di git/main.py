""" Di-gits
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.06.01-1939 """
import sys
from random import randint as ranum
import art


EASY_MODE = 9
NORMAL_MODE = 4
HARD_MODE = 2


def diff_select():
    """ Lets user select their difficulty level """
    diff = input("Please select your difficulty level. 'easy', 'normal', 'hard': ")
    if diff.startswith('e'):
        return EASY_MODE

    elif diff.startswith('n'):
        return NORMAL_MODE

    elif diff.startswith('h'):
        return HARD_MODE

    else:
        print("That's not right try again!!")
        diff_select()


def play_again():
    play = input("Want to play again: ")
    if play.startswith('y'):
        game()

    else:
        sys.exit()


def game():
    print(art.logo + "\n")
    lives = diff_select()
    game_over = False
    answer = ranum(1, 100)

    while lives > 0 and not game_over:
        guess = int(input("Guess a number between 1-100: "))
        if guess == answer:
            print(f"That's right the answer was {answer}!\n")
            game_over = True
            play_again()

        elif guess > answer:
            print(f"Whoa that's too high my friend try again! {lives} attempts left.\n")
            lives -= 1

        elif guess < answer:
            print(f"Hmm that seems to be too low! {lives} attempts left!\n")
            lives -= 1

        else:
            if lives > 0:
                print(f"That's not a valid input try again!\n")

            else:
                print(f"All out of tries too bad!\n")
                play_again()


game()