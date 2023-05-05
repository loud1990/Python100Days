import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Constants
HEIGHT_SCREEN = 600
WIDTH_SCREEN = 600

# Setup the game
frog = Player()
scoreboard = Scoreboard()
car_man = CarManager()

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Listen for key presses
screen.listen()
screen.onkeypress(frog.move, "Up")

# Game loop
game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    if loop_count == 5:
        car_man.create_car()
        loop_count = 0
    car_man.move_cars(scoreboard.level)
    screen.update()

    # Detect collision with top wall - goto next level
    if frog.ycor() > (HEIGHT_SCREEN / 2):
        frog.penup()
        frog.to_start()
        scoreboard.next_level()

    # Detect collision with car
    for car in car_man.cars:
        if frog.distance(car) < 10:
            scoreboard.game_over()
            game_is_on = False

    loop_count += 1

screen.exitonclick()
