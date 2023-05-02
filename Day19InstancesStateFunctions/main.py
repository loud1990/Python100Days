from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

DISTANCE = 10
ANGLE = 10

def move_forwards():
    tim.forward(DISTANCE)


def move_backwards():
    tim.back(DISTANCE)


def turn_clockwise():
    tim.setheading(tim.heading() + ANGLE)


def turn_counter_clockwise():
    tim.setheading(tim.heading() - ANGLE)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
