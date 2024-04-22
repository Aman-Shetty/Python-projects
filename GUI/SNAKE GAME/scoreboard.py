from turtle import Turtle

Alignment = "center"
Font = ("Calibri", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=Alignment, font=Font)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt0", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=Alignment, font=Font)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
