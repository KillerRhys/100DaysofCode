from turtle import Turtle


class Keeper(Turtle):
    """ Keeps Level score & prints game over! """
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.hideturtle()
        self.color('black')
        self.goto(-340, 350)
        self.write(f'Level: {self.level}', align='center', font=('Arial', 20, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over!', align='center', font=('Arial', 40, 'bold'))
        self.goto(0, -50)
        self.write(f"You reached Level: {self.level}!", align='center', font=('Arial', 40, 'bold'))

    def next_stage(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=('Arial', 20, 'bold'))


