from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 16, "bold")


class ScoreBoard(Turtle):
    """ Keeps track of points! """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 50
        self.pu()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.write(arg=f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f'Game Over \nFinal Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def tally(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)
