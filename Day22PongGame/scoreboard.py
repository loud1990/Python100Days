from turtle import Turtle

SPACE_BETWEEN = 50
SCREEN_HEIGHT = 1000


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.display_scoreboard()

    def add_point_l(self):
        self.l_score += 1
        self.clear()
        self.display_scoreboard()

    def add_point_r(self):
        self.r_score += 1
        self.clear()
        self.display_scoreboard()

    def draw_center_line(self):
        self.penup()
        self.goto(0, -SCREEN_HEIGHT)
        self.pendown()
        self.setheading(90)
        for i in range(100):
            self.forward(SCREEN_HEIGHT / SPACE_BETWEEN)
            self.penup()
            self.forward(SCREEN_HEIGHT / SPACE_BETWEEN)
            self.pendown()
        self.penup()
        self.goto(0, 0)

    def display_scoreboard(self):
        self.clear()
        self.draw_center_line()
        self.penup()
        self.goto(0, 240)
        self.write(f"{self.l_score}                              {self.r_score}",
                   move=False, align="center", font=('Arial', 48, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=('Arial', 24, 'normal'))
