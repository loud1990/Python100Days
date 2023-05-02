'''# Turtle draw shapes program
from turtle import Turtle, Screen
import random

SIDE_LENGTH = 100
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
shape_sides = 3


def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        timmy_the_turtle.forward(SIDE_LENGTH)
        timmy_the_turtle.right(angle)


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"]

while shape_sides < 11:
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(shape_sides)
    shape_sides += 1

screen = Screen()
screen.exitonclick()

''' # End of turtle draw shapes program
'''
# Turtle random walk program

from turtle import Screen
import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
LENGTH = 20


def pick_direction():
    return random.choice(directions)


def pick_color():
    return random.choice(colours)


t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed(0)
tim.pensize(15)
for i in range(200):
    tim.color(random_color())
    tim.setheading(pick_direction())
    tim.forward(LENGTH)


screen = Screen()
screen.exitonclick()

'''

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
RADIUS = 50
heading = 0


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for i in range(0,36):
    tim.color(random_color())
    tim.circle(RADIUS)
    heading += 10
    tim.setheading(heading)
screen = t.Screen()
screen.exitonclick()

########### Challenge 5 - Spirograph ########





