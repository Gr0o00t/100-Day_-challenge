from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time




screen = Screen()
screen.setup(600,600)
screen.tracer(0)

player_1=Player()
screen.listen()
screen.onkey(player_1.move,"Up")

car_manager=CarManager()
level= Scoreboard()



game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    level.update_score()
    # Turtle collision with car
    for car in car_manager.all_cars:
        if car.distance(player_1) < 20:
            game_is_on = False


    if player_1.Finish_race():
        level.score = level.score + 1
        car_manager.inc_speed()


screen.exitonclick()