""" Di-gits
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.06.01-1939 """

from random import randint as ranum
import art


easy = 10
hard = 5
insane = 1
lives = 1

diff = input("What difficulty would you like to play on? easy, hard or insane? ")
if diff.startswith("e"):
    lives = 10

elif diff.startswith("h"):
    lives = 5

elif diff.startswith('i'):
    lives = 1

else:
    print("That's not an option... probably should put you on easy champ...")
    lives = 10

game_over = False
answer = ranum(1, 100)
while lives > 0 and not game_over:
    print("\n" + art.logo +"\n")
    guess = int(input("Ok pick a number between 1-100: "))
    if guess == answer:
        print(f"Sweet you got it! The number was {answer}")
        game_over = True

    elif guess > answer:
        lives -= 1
        print(f"Sorry {guess} is too high! {lives} attempts left!")

    elif guess < answer:
        lives -= 1
        print(f"{guess} is too low! {lives} attempts left!")

    else:
        if lives > 0:
            print(f"That's not a real guess try again! {lives} attempts left!")

        else:
            print(f"Uh-oh you're out of tries my friend!")
            game_over = True

