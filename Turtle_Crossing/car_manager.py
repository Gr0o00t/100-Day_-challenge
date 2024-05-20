from turtle import Turtle
import random

COLORS = ["red","orange","yellow","green","blue","purple"]
SPEED_CAR = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        self.all_cars=[]
        self.car_speed=SPEED_CAR

    def create_car(self):
        if random.randint(1,6) == 1:
            car= Turtle()
            car.penup()
            car.shape("square")
            car.goto(280,random.randint(-250,250))
            car.setheading(180)

            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def inc_speed(self):
        self.car_speed +=1




