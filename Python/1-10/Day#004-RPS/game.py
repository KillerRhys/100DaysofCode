""" RPS OOP Practice """
import sys
from random import choice as pick
from art import logo as ls


class GamePlay:
    wins = 0
    losses = 0
    draws = 0
    games = wins + losses + draws
    moves = ["ROCK", "PAPER", "SCISSORS"]

    def intro(self):
        print(ls)
        print(f"Games Played: {self.games}, Wins: {self.wins}, Losses: {self.losses}, Draws: {self.draws}\n")

    def game_loop(self):
        self.games = self.wins + self.losses + self.draws
        self.intro()
        p_choice = input(self.moves)
        p_choice = p_choice.upper()
        c_choice = pick(self.moves)
        player_wins = self.check_wins(p_choice, c_choice)
        if player_wins == "Yes":
            print(f"You win! {p_choice} beats {c_choice}!")
            self.wins += 1

        elif player_wins == "No":
            print(f"You lost!! {c_choice} trumps {p_choice}...")
            self.losses += 1

        elif player_wins == "Draw":
            print(f"It's a draw! {p_choice} vs. {c_choice}")
            self.draws += 1

    def check_wins(self, p_choice, c_choice):
        if p_choice == "ROCK" and c_choice == "PAPER" or p_choice == "PAPER" and c_choice == "SCISSORS" or p_choice == "SCISSORS" and c_choice == "ROCK":
            return "No"

        elif p_choice == "ROCK" and c_choice == "SCISSORS" or p_choice == "PAPER" and c_choice == "ROCK" or p_choice == "SCISSORS" and c_choice == "PAPER":
            return "Yes"

        else:
            return "Draw"

    def play_again(self):
        again = input("Play another game? ")
        if again.startswith('y'):
            self.game_loop()
        else:
            self.intro()
            sys.exit()
