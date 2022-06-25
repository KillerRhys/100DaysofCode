from turtle import Turtle
from random import choice
COLORS = ['blue', 'red', 'orange', 'purple']
MOVE_SPEED = 20


class Player(Turtle):
    """ Handles player creation & movement """
    def __init__(self):
        super().__init__('turtle')
        self.color(choice(COLORS))
        self.speed('fastest')
        self.pu()
        self.x = 0
        self.y = -380
        self.setheading(90)
        self.goto(self.x, self.y)

    def move_up(self):
        new_y = self.ycor() + MOVE_SPEED
        self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - MOVE_SPEED
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_SPEED
        self.goto(new_x, self.ycor())
