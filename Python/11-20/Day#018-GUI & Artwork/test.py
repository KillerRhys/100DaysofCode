import turtle
from turtle import Turtle, Screen
import random

leo = Turtle()
leo.shape('turtle')
leo.color('blue')
turtle.colormode(255)

# runs = 4
# Square Challenge
# while runs > 0:
#     leo.fd(100)
#     leo.rt(90)
#     runs -= 1


# runs = 15
# # Dotted line
# while runs > 0:
#     leo.pd()
#     leo.fd(12)
#     leo.pu()
#     leo.fd(12)
#     runs -= 1


# Drawing new shapes
# colors = ['red', 'blue', 'green', 'black', 'orange', 'purple', 'pink', 'brown']
# shapes = [3, 4, 5, 6, 7, 8, 9, 10]
# count = 0
# for item in shapes:
#     turns = item
#     degree = 360 / item
#     leo.color(colors[count])
#     count += 1
#     while turns > 0:
#         leo.fd(100)
#         leo.rt(degree)
#         turns -= 1


# Random Walk Challenge
# leo.pensize(10)
# leo.speed(0)
# turtle.colormode((255))
# dirs = [0, 90, 180, 360]
# steps = 200
# while steps > 0:
#         dir = random.choice(dirs)
#         steps -= 1
#         leo.pencolor((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)))
#         leo.fd(15)
#         leo.setheading(dir)



# # Spirograph
# leo.speed(0)
# leo.pensize(3)
# space = 7
# for _ in range(int(360 / space)):
#     leo.pencolor((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)))
#     leo.circle(100)
#     leo.setheading(leo.heading() + space)


# Picaso!
""" Draw Picaso! """


screen = Screen()
screen.exitonclick()
