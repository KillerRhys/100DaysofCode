""" Shake's Shakedown!
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.07.02-1000 """


from turtle import Screen
from time import sleep
from player import Player


display = Screen()
display.setup(800, 800)
display.title("Shake's Shakedown")
display.tracer(0)
display.bgcolor('teal')
player = Player()
game_over = False
display.listen()
display.onkeypress(player.move_up, 'Up')
display.onkeypress(player.move_down, 'Down')
display.onkeypress(player.move_right, 'Right')
display.onkeypress(player.move_left, 'Left')


while not game_over:
    display.update()
    sleep(0.1)

# TODO Classes = player, item, tally & data directory

display.exitonclick()