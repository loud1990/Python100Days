from turtle import Turtle

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.speed("fast")
        self.x_move = 10
        self.y_move = 10

    def reset(self):
        self.penup()
        self.goto(0, 0)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
