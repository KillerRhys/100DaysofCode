import turtle


class Player(turtle.Turtle):
    """ Handles player char & movement """
    def __init__(self):
        super().__init__()
        turtle.register_shape('shake', ((-10, -2), (-2, 0), (2, 0), (2, 6), (-2, 4), (-4, 5), (-7, 7), (-10, 8)))
        self.shape('shake')
        self.pu()
        self.color('white')
        self.turtlesize(5)
        self.move_speed = 10

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.move_speed)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.move_speed)

    def move_right(self):
        self.goto(self.xcor() + self.move_speed, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - self.move_speed, self.ycor())
