""" Hangman
    Coded by TechGYQ
    www.mythosworks.com
    OC:2022.05.10-2004 """

# Imports
import random
import hangman_art
import re
import sys


# List Build
word_list = open("words.txt", "r")
words = word_list.readlines()
word_list.close()


# Funcs
def get_word():
    get_word.letters = []
    get_word.puzz = random.choice(words)
    get_word.l = len(get_word.puzz)
    for i in range(get_word.l-1):
        get_word.letters.append("_")

    get_word.slits = " ".join(get_word.letters)


def game_start():
    print(hangman_art.logo)
    game_start.already_guessed = []
    game_start.game_over = False
    game_start.life = 5
    get_word()
    play()


def play():
    while not game_start.game_over:
        print(hangman_art.stages[game_start.life])
        print(get_word.slits)
        print(f"{get_word.l - 1} letters.")
        guess = input(f"Pick a letter? You have {game_start.life} attempts left! ")
        guess = guess.lower()
        print(game_start.already_guessed)

        if guess in game_start.already_guessed:
            print("You've tried that already!")

        elif guess in get_word.puzz:
            print("Correct!")
            x = [i.start() for i in re.finditer(guess, get_word.puzz)]
            for item in x:
                get_word.letters[item] = guess
            get_word.slits = " ".join(get_word.letters)
            game_start.already_guessed.append(guess)

        else:
            print("Nope")
            game_start.life -= 1
            game_start.already_guessed.append(guess)
            print(hangman_art.stages[game_start.life])

            if game_start.life == 0:
                game_start.game_over = True
                print(hangman_art.logo)
                print(f"Sorry the word was {get_word.puzz}!")
                con = input("Want to play again?! ")
                con = con.lower()
                if con.startswith("y"):
                    game_start()
                else:
                    sys.exit()


game_start()