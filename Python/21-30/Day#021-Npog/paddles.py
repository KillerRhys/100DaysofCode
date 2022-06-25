from turtle import Turtle
UP = 90
DOWN = 270
SPEED = 10
BOUNDARY = 260
BOUNDARY_BOTTOM = -240


class Paddle(Turtle):
    """ Handles paddle creation & movement """
    def __init__(self, x, y):
        super().__init__('square')
        self.make_paddle()
        self.goto(x, y)

    def make_paddle(self):
        self.pu()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed('fastest')

    def up(self):
        if self.ycor() < BOUNDARY:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > BOUNDARY_BOTTOM:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
