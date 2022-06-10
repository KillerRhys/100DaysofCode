""" OOP Practice Hangman refactor """

import random
import hangman_art
import re
import sys


class Hanged():
    """ Main Game Code, Creates List, Picks word & handles gameplay"""

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.games = 0
        self.lives = 5
        self.guessed = []
        self.word_list = open('words.txt', 'r')
        self.words = self.word_list.readlines()
        self.word_list.close()
        self.puzzword = random.choice(self.words)
        self.count = len(self.puzzword) - 1
        self.letters = []
        for i in range(self.count):
            self.letters.append('_')

        self.places = " ".join(self.letters)
        print(hangman_art.logo)

    def state_reset(self):
        self.lives = 5
        self.guessed = []
        self.word_list = open('words.txt', 'r')
        self.words = self.word_list.readlines()
        self.word_list.close()
        self.puzzword = random.choice(self.words)
        self.count = len(self.puzzword) - 1
        self.letters = []
        for i in range(self.count):
            self.letters.append('_')

        self.places = " ".join(self.letters)
        print(hangman_art.logo)

    def begin_game(self):
        print(hangman_art.stages[self.lives], f"\nWins: {self.wins}, Losses: {self.losses}, Played: {self.games}")
        print(self.letters)
        print(f"{self.count} letters remaining.")
        guess = input(f"You have {self.lives} left, select a letter: ")
        guess = guess.lower()
        print(self.guessed)

        if guess in self.guessed:
            print("You've tried that already!")

        elif guess in self.puzzword:
            print(f"{guess} is in there!")
            self.count -= 1
            x = [i.start() for i in re.finditer(guess, self.puzzword)]
            for item in x:
                self.letters[item] = guess
            self.places = " ".join(self.letters)
            self.guessed.append(guess)
            if self.count == 0:
                print(f"You're right the word was {self.puzzword}")
                self.wins += 1
                self.games += 1
                self.state_reset()

        else:
            print(f"Nope there are no {guess}'s!")
            self.lives -= 1
            self.guessed.append(guess)

            if self.lives == 0:
                print(hangman_art.logo)
                print(f"Sorry the word was {self.puzzword}")
                self.losses += 1
                self.games += 1
                self.state_reset()
