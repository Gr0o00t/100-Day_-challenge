from turtle import Screen
from car_manager import Car_manager
from player import Player
from scoreboard import Scoreboard
import time




screen = Screen()
screen.setup(600,600)
screen.tracer(0)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
time.sleep(1)


screen.onclick()