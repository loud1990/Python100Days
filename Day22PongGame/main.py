from turtle import Turtle, Screen
import time
from paddle import Paddle
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
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

screen.update()

# Start running the game
game_on = True
while game_on:
    screen.update() # only update the screen once all of the segments have moved forward
    time.sleep(0.1)

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
