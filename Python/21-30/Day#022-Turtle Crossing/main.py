""" Turtle X-ing
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.06.25-0850 """


# Imports
import time
import turtle
from turtle import Screen
from player import Player
from mobs import TrafficControl
from scoreboard import Keeper


# Vars
INFO = "Turtle X-ing Ver: 2022.06.25(0850)"
game_on = True
turtle.colormode(255)

# Setup
player = Player()
board = Keeper()
LEVEL = board.level
mobs = 7
car = TrafficControl(mobs)
display = Screen()
display.title(INFO)
display.tracer(0)
display.setup(width=800, height=800)
display.listen()
display.onkey(player.move_up, 'Up')
display.onkey(player.move_left, 'Left')
display.onkey(player.move_right, 'Right')


while game_on:
    time.sleep(0.1)
    display.update()

    car.drive()
    for item in car.vehicles:
        if item.distance(player) < 18:
            game_on = False
            board.game_over()

    if player.ycor() > 380:
        player.goto(0, -380)
        board.next_stage()
        car.make_car(mobs)


display.exitonclick()
