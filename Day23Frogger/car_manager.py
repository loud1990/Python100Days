import random
from turtle import Turtle
from random import choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.penup()
        new_car.goto(280, random.randint(-230, 230))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_cars(self, level):
        for car in self.cars:
            car.forward(MOVE_INCREMENT * level + STARTING_MOVE_DISTANCE)
