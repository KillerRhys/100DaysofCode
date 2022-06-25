from turtle import Turtle
NET_LOCATIONS = [(0, 270), (0, 190), (0, 110), (0, 30), (0, -50), (0, -130), (0, -210), (0, -290)]
SCORE_LOCATIONS = [(-100, 260), (100, 260)]
NETS = []
SCORES = []


class ScoreBoard(Turtle):
    """ Handles score keeping and field layout """
    def __init__(self):
        super().__init__('square')
        self.p1_score = 0
        self.p2_score = 0
        self.setup_arena()

    def setup_arena(self):
        for position in NET_LOCATIONS:
            new_net = Turtle('square')
            new_net.color('white')
            new_net.penup()
            new_net.shapesize(stretch_wid=0.3, stretch_len=2.0)
            new_net.setheading(90)
            new_net.goto(position)
            NETS.append(new_net)

        for location in SCORE_LOCATIONS:
            new_label = Turtle()
            new_label.pu()
            new_label.hideturtle()
            new_label.color('white')
            new_label.goto(location)
            SCORES.append(new_label)

        SCORES[0].write(arg=self.p1_score, align='center', font=('Arial', 28, 'bold'))
        SCORES[1].write(arg=self.p2_score, align='center', font=('Arial', 28, 'bold'))

    def p1_scored(self):
        self.p1_score += 1
        SCORES[0].clear()
        SCORES[0].write(arg=self.p1_score, align='center', font=('Arial', 28, 'bold'))

    def p2_scored(self):
        self.p2_score += 1
        SCORES[1].clear()
        SCORES[1].write(arg=self.p2_score, align='center', font=('Arial', 28, 'bold'))
