
from turtle import Turtle, Screen
import pandas as pd

turtle=Turtle()
screen=Screen()
stat_data= pd.read_csv("50_states.csv")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

gussed_answer=[]
while len(gussed_answer)<50:
    answer = screen.textinput(title="U.S. State Guess Game", prompt="Guess a state name:" )
    if answer not in gussed_answer:


screen.exitonclick()
