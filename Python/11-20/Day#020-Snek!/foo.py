from turtle import Turtle
import random
foods = ['blueberry', 'banana', 'strawberry', 'apple', 'orange']


class Food(Turtle):

    """ Handles all food related stuff! """
    def __init__(self):
        super().__init__()
        self.food = random.choice(foods)
        self.food_type(self.food)
        self.refresh()

    def food_type(self, food):
        food = self.food
        if food == "blueberry":
            self.shape('circle')
            self.penup()
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.color('blue')
            self.speed('fastest')

        elif food == "banana":
            self.shape('circle')
            self.penup()
            self.shapesize(stretch_len=0.3, stretch_wid=1)
            self.color('yellow')
            self.speed('fastest')

        elif food == "Strawberry":
            self.shape('circle')
            self.penup()
            self.shapesize(stretch_len=0.8, stretch_wid=0.5)
            self.color('red')
            self.speed('fastest')

        elif food == "apple":
            self.shape('circle')
            self.penup()
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.color('red')
            self.speed('fastest')

        elif food == "orange":
            self.shape('circle')
            self.penup()
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.color('orange')
            self.speed('fastest')

    def refresh(self):
        self.food = random.choice(foods)
        self.food_type(self.food)
        random.x = random.randint(-260, 260)
        random.y = random.randint(-260, 260)
        self.goto(random.x, random.y)

