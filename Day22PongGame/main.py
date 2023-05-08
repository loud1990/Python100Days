from turtle import Turtle, Screen
import time
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

# Constants go here
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Display the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # don't update the screen all the time, this eliminates the straggling segment look

screen.listen()

# Set up paddle
right_paddle = Paddle(((SCREEN_WIDTH / 2) - 20), 0)
left_paddle = Paddle(((-SCREEN_WIDTH / 2) + 20), 0)

# Set up scoreboard
scoreboard = Scoreboard()
scoreboard.draw_center_line()

# Set up ball
ball = Ball()

# Listen for key presses to move paddles
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

screen.update()

# Start running the game
game_on = True
while game_on:
    screen.update() # only update the screen once all of the segments have moved forward
    time.sleep(0.05)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > ((SCREEN_HEIGHT / 2) - 20) or ball.ycor() < ((-SCREEN_HEIGHT / 2) + 20):
        ball.wall_bounce()

    if ball.xcor() > ((SCREEN_WIDTH / 2) - 20):
        scoreboard.l_score += 1
        scoreboard.display_scoreboard()
        print("score")
        ball.reset()

    if ball.xcor() < ((-SCREEN_WIDTH / 2) + 20):
        scoreboard.r_score += 1
        scoreboard.display_scoreboard()
        print("score")
        ball.reset()

    # TODO fix left paddle collision
    # Detect collision with paddle
    if left_paddle.distance(ball) < 30 and ball.xcor() > ((SCREEN_WIDTH / 2) - 20) or right_paddle.distance(ball) < 30 and ball.xcor() < ((SCREEN_WIDTH / 2) - 20):
        ball.paddle_bounce()

    '''
    # Detect collision with food
    if paddle.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_point()
        snake.extend()

    # Detect collision with wall
    if paddle.head.xcor() > MAX_WIDTH or paddle.head.xcor() < -MAX_WIDTH or paddle.head.ycor() > MAX_HEIGHT or paddle.head.ycor() < -MAX_HEIGHT:
        print("Game Over")
        scoreboard.game_over()
        game_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
'''
screen.exitonclick()
