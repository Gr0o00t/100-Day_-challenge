
from turtle import Turtle, Screen
import pandas as pd

turtle=Turtle()
screen=Screen()
data= pd.read_csv("50_states.csv")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

gussed_answer=[]
while len(gussed_answer)<50:
    answer = screen.textinput(title="U.S. State Guess Game", prompt="Guess a state name:" )
    print(answer)
    if answer not in gussed_answer and answer in data.state:
        gussed_answer.append(answer)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int.data[data.state == answer].x,int.data[data.state == answer].y)
        turtle.write(answer)
        print()

screen.exitonclick()
