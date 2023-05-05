from turtle import Turtle

FONT = ("Courier", 24, "normal")
HEIGHT_SCREEN = 600
WIDTH_SCREEN = 600


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.display_scoreboard()

    def display_scoreboard(self):
        self.clear()
        self.penup()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", move=False, align="center", font=('Arial', 24, 'normal'))
        self.hideturtle()

    def next_level(self):
        self.level += 1
        self.display_scoreboard()

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(-0, 0)
        self.write("GAME OVER", move=False, align="center", font=('Arial', 24, 'normal'))
        self.hideturtle()
