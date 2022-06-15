import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
leo = Turtle()
leo.shapesize(2)
leo.pensize(2)
screen = Screen()
pen_is_down = True


def new_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    leo.color(new_color)
    leo.pencolor(new_color)


def pen_control():
    global pen_is_down
    if pen_is_down:
        leo.penup()
        pen_is_down = False
    else:
        leo.pendown()
        pen_is_down = True


def reset_screen():
    screen.resetscreen()
    leo.shapesize(2)
    leo.pensize(2)


def move_forward():
    leo.fd(10)


def move_backward():
    leo.backward(10)


def turn_left():
    leo.lt(5)


def turn_right():
    leo.rt(5)


screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='d', fun=turn_right)
screen.onkey(key='space', fun=pen_control)
screen.onkey(key='n', fun=new_color)
screen.onkeypress(key='c', fun=reset_screen)


screen.listen()
screen.exitonclick()
