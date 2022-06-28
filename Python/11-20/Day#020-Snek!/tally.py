from turtle import Turtle
GAME_FILE = 'snek.dat'
ALIGNMENT = 'center'
FONT = ('Arial', 16, "bold")


class ScoreBoard(Turtle):
    """ Keeps track of points! """
    def __init__(self):
        super().__init__()
        try:
            f = open(GAME_FILE, 'r')
            data = f.read()
            f.close()

        except FileNotFoundError:
            f = open(GAME_FILE, 'w+')
            data = '0'
            f.write(data)
            f.close()

        self.score = 0
        self.high_score = int(data)
        self.pu()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            f = open(GAME_FILE, 'w')
            data = str(self.high_score)
            f.write(data)
            f.close()
            self.clear()
            self.write(arg=f'Score: {self.score} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

        else:
            self.score = 0
            self.clear()
            self.write(arg=f'Score: {self.score} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def tally(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)
