from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self, level):
        self.clear()
        self.goto(-280, 250)
        self.write(level, align="center", font=FONT)

    def gameover(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER!!!",align="center",font=FONT)


