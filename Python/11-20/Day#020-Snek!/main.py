""" Snek!
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.06.14-2100 """

import time
from turtle import Screen
from snake import Snake
from foo import Food
from tally import ScoreBoard

foods = ['blueberry', 'banana', 'strawberry', 'apple', 'orange']
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snek!")
screen.tracer(0)
Playing = True

snake = Snake()
food = Food()
board = ScoreBoard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

while Playing:
    screen.update()
    time.sleep(0.1)
    # snake.snake_skin()

    snake.move()

    if snake.head.distance(food) < 15:
        board.tally()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.phoenix()
        board.game_reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.phoenix()
            board.game_reset()

screen.exitonclick()
