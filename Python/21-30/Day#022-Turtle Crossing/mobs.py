from turtle import Turtle
from random import randint


class TrafficControl:
    """ Creates car and car variations """
    def __init__(self, mobs):
        self.mobs = mobs
        self.vehicles = []
        self.make_car(self.mobs)

    def make_car(self, mobs):
        self.mobs = mobs
        while self.mobs > 0:
            new_car = Turtle(visible=False)
            new_car.speed('fastest')
            new_car.shape('square')
            new_r = randint(1, 255)
            new_g = randint(1, 255)
            new_b = randint(1, 255)
            new_color = (new_r, new_g, new_b)
            new_car.pu()
            new_car.color(new_color)
            new_car.shapesize(stretch_wid=1.5, stretch_len=2.5)
            new_y = randint(-300, 400)
            new_x = randint(450, 650)
            new_car.goto(new_x, new_y)
            self.vehicles.append(new_car)
            self.mobs -= 1
        for car in self.vehicles:
            car.showturtle()

    def drive(self):
        for car in self.vehicles:
            car_speed = randint(1, 40)
            new_x = car.xcor() - car_speed
            car.goto(new_x, car.ycor())
            if car.xcor() < -400:
                car.goto(randint(450, 650), randint(-300, 400))
