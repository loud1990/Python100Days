import random
import time
from turtle import Turtle, Screen
from snake import Snake

STARTING_X_POS = 0
STARTING_Y_POS = 0
DISTANCE_BETWEEN = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

x_pos = STARTING_X_POS
y_pos = STARTING_Y_POS

# Screen setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # don't update the screen all the time, this eliminates the straggling segment look


'''
# Snake setup
for i in range(3):
    new_snake = Turtle(shape="square")
    new_snake.color("white")
    new_snake.penup()
    new_snake.goto(x=x_pos- DISTANCE_BETWEEN, y=y_pos)
    x_pos -= DISTANCE_BETWEEN
    snakes.append(new_snake)
'''
snake = Snake()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

# Start running the game
game_on = True
while game_on:
    screen.update() # only update the screen once all of the segments have moved forward
    time.sleep(0.1)
    snake.move()

    '''
    for seg in range(len(snakes) - 1, 0, -1):
        new_x = snakes[seg - 1].xcor()
        new_y = snakes[seg - 1].ycor()
        snakes[seg].goto(new_x, new_y)
    snakes[0].forward(DISTANCE_BETWEEN)
'''

screen.exitonclick()
