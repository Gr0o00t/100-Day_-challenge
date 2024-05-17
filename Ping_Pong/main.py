from turtle import Turtle,Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

Starting_POSITIONS = [(-280,0),(280,0)]

player_1=Paddle()
player_2=Paddle()
score=Scoreboard()
ball=Ball()

screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping_Pong")
screen.tracer(0)

player_1.create_paddle()
player_1.position(-360,0)
player_2.create_paddle()
player_2.position(360,0)


game_is_on = 'True'
while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()