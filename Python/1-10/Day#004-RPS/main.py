""" Rock, Paper, Scissors (RPS)
    Coded by TechGYQ
    www.mythosworks.com
    OC:2022.05.05-1853 """

logo = """
$$$$$$$\                      $$\                                         
$$  __$$\                     $$ |                                        
$$ |  $$ | $$$$$$\   $$$$$$$\ $$ |  $$\                                   
$$$$$$$  |$$  __$$\ $$  _____|$$ | $$  |                                  
$$  __$$< $$ /  $$ |$$ /      $$$$$$  /                                   
$$ |  $$ |$$ |  $$ |$$ |      $$  _$$<                                    
$$ |  $$ |\$$$$$$  |\$$$$$$$\ $$ | \$$\                                   
\__|  \__| \______/  \_______|\__|  \__|                                  
                                                                          
                                                                          
                                                                          
$$$$$$$\                                                                  
$$  __$$\                                                                 
$$ |  $$ |$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\                           
$$$$$$$  |\____$$\ $$  __$$\ $$  __$$\ $$  __$$\                          
$$  ____/ $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|                         
$$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |                               
$$ |     \$$$$$$$ |$$$$$$$  |\$$$$$$$\ $$ |                               
\__|      \_______|$$  ____/  \_______|\__|                               
                   $$ |                                                   
                   $$ |                                                   
                   \__|                                                   
 $$$$$$\            $$\                                                   
$$  __$$\           \__|                                                  
$$ /  \__| $$$$$$$\ $$\  $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$$\ 
\$$$$$$\  $$  _____|$$ |$$  _____|$$  _____|$$  __$$\ $$  __$$\ $$  _____|
 \____$$\ $$ /      $$ |\$$$$$$\  \$$$$$$\  $$ /  $$ |$$ |  \__|\$$$$$$\  
$$\   $$ |$$ |      $$ | \____$$\  \____$$\ $$ |  $$ |$$ |       \____$$\ 
\$$$$$$  |\$$$$$$$\ $$ |$$$$$$$  |$$$$$$$  |\$$$$$$  |$$ |      $$$$$$$  |
 \______/  \_______|\__|\_______/ \_______/  \______/ \__|      \_______/ """

# Imports
from random import choice as pick
import  sys

# Globals
WINS = 0
LOSSES = 0
DRAWS = 0
GAMES = 0
moves = ["ROCK", "PAPER", "SCISSORS"]
gameOver = False


def intro():
    print(logo)
    print(f'Games Played: {GAMES}, Wins: {WINS}, Losses: {LOSSES}, Draws: {DRAWS}')


while not gameOver:
    GAMES = WINS + LOSSES + DRAWS
    intro()
    p_choice = input("'Rock', 'Paper', or 'Scissors'? ")
    p_choice = p_choice.upper()
    c_choice = pick(moves)
    print(p_choice, c_choice)

    if p_choice.startswith("R"):
        if c_choice == "ROCK":
            print("Rocking out, but it's a draw!!")
            DRAWS += 1

        elif c_choice == "PAPER":
            print("Oh no you got covered!")
            LOSSES += 1

        elif c_choice == "SCISSORS":
            print("Smashed those choppers!")
            WINS += 1

    elif p_choice.startswith("P"):
        if c_choice == "ROCK":
            print("And just like that they disappeared!")
            WINS += 1

        elif c_choice == "PAPER":
            print("Make some confetti to celebrate a draw...")
            DRAWS += 1

        elif c_choice == "SCISSORS":
            print("Ouch that was a deep cut!")
            LOSSES += 1

    elif p_choice.startswith("S"):
        if c_choice == "ROCK":
            print("You got smashed!")
            LOSSES += 1

        elif c_choice == "PAPER":
            print("Sliced & Diced!")
            WINS += 1

        elif c_choice == "SCISSORS":
            print("Stalemate!")
            DRAWS += 1

    elif p_choice.startswith("Q"):
        intro()
        print("Thanks for playing!!")
        sys.exit()

    else:
        print("Um... That is not a valid selection! Try again!!")
        intro()
