""" Npog Ver: 1.0
    Coded by TechGYQ
    www.MythosWorks.com
    2022.06.20-1755 """

from turtle import Screen
from paddles import Paddle
from scoreboard import ScoreBoard
from shuttle import Pong
import time


info = 'NPOG Ver: 1.0'
display = Screen()
display.setup(width=800, height=600)
display.title(info)
display.bgcolor('black')
display.tracer(0)
p1 = Paddle(-350, 0)
p2 = Paddle(350, 0)
arena = ScoreBoard()
ball = Pong()
display.listen()
display.onkeypress(key='w', fun=p1.up)
display.onkeypress(key='s', fun=p1.down)
display.onkeypress(key='Up', fun=p2.up)
display.onkeypress(key="Down", fun=p2.down)
game_on = True


while game_on:
    time.sleep(ball.move_speed)
    display.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(p2) < 50 and ball.xcor() > 320 or ball.distance(p1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed * 0.8

    if ball.xcor() > 380:
        ball.reset_pos()
        arena.p1_scored()
        ball.move_speed = 0.1

    if ball.xcor() < -380:
        ball.reset_pos()
        arena.p2_scored()
        ball.move_speed = 0.1

display.exitonclick()
