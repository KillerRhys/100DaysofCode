""" TMNT Racers!
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.06.14-0838 """


# Imports
import turtle
from turtle import Turtle, Screen
import random

# Vars
colors = ["red", "blue", 'orange', 'purple']
runner_spot = 120
turtles = []
game_over = False

for color in colors:
    name = color
    name = Turtle()
    name.shape('turtle')
    name.color(color)
    name.pu()
    name.goto(-230, runner_spot)
    turtles.append(name)
    runner_spot -= 80


screen = Screen()
screen.setup(width=500, height=400)
player_bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Pick a color: ")
player_bet = player_bet.lower()
for turtle in turtles:
    turtle.speed('slowest')


while not game_over:
    for turtle in turtles:
        pace = random.randint(0, 10)
        turtle.forward(pace)
        if turtle.xcor() > 230:
            game_over = True
            winner = turtle.pencolor()
            if player_bet == winner:
                print("You called it!")
            else:
                print(f'Sorry the {winner} turtle won!')


screen.exitonclick()
