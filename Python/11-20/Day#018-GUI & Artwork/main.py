""" Artsy
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.06.12-1352 """
import turtle
from turtle import Turtle, Screen

import colorgram
import random

colors = colorgram.extract('image.jpg', 2 ** 32)
color_palette = []

for count in range(len(colors)):
    rgb = colors[count]
    r = rgb.rgb.r
    g = rgb.rgb.g
    b = rgb.rgb.b
    new_color = (r, g, b)
    color_palette.append(new_color)

del color_palette[:4]

turtle.colormode(255)
leo = Turtle()
leo.shape("turtle")
leo.color('blue')
leo.speed(0)
leo.pensize(20)
move = 50
leo.pu()
y = -500


for _ in range(10):
    leo.setx(-600)
    leo.sety(y)
    y += 110
    for _ in range(10):
        leo.dot(40, random.choice(color_palette))
        leo.fd(130)

leo.hideturtle()
screen = Screen()
screen.exitonclick()
