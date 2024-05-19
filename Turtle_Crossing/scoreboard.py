from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-250,250)
        self.hideturtle()
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def Game_Over(self):

        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
