import random
from turtle import Turtle, Screen

STARTING_X_POS = -230
STARTING_Y_POS = -100
DISTANCE_BETWEEN = 20
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

x_pos = STARTING_X_POS
y_pos = STARTING_Y_POS

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
current_color = 0

turtles = []

for turt in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[current_color])
    new_turtle.penup()
    new_turtle.goto(x=x_pos, y=y_pos)
    new_turtle.pendown()
    y_pos += DISTANCE_BETWEEN
    current_color += 1
    turtles.append(new_turtle)


def check_bet():
    if user_bet == winner:
        return True
    else:
        return False


race_on = True
winner = turtles[0].color()
while race_on:
    for tur in turtles:
        rand_distance = random.randint(0, 10)
        tur.forward(rand_distance)
        if tur.xcor() >= (SCREEN_WIDTH / 2):
            print(f"{tur.pencolor()} is the winner!")
            winner = tur.pencolor()
            race_on = False
            if check_bet():
                print("You win!")
            else:
                print("You lose...")

screen.exitonclick()
