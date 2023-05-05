# Define the paddle class
from turtle import Turtle

STARTING_X_POS = 350
STARTING_Y_POS = 0
MOVE_SPEED = 40


class Paddle(Turtle):

    def __init__(self, start_x, start_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(start_x, start_y)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_SPEED)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_SPEED)

