import turtle
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.display_scoreboard()

    def add_point(self):
        self.score += 1
        self.clear()
        self.display_scoreboard()

    def display_scoreboard(self):
        self.write(f"Score = {self.score}                      High Score = {self.high_score}",
                   move=False, align="center", font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=('Arial', 24, 'normal'))
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
