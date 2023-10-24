from turtle import Turtle
import random

CARS_SPEED = 5
INCREASE_SPEED = 5
COLOR = ("Red", "Blue", "yellow", "Purple", "orange")

class Car():
    def __init__(self):
        self.all_car = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLOR))
            new_car.penup()
            starting_y = random.randint(-250, 250)
            new_car.goto(300, starting_y)
            self.all_car.append(new_car)

    def move(self):
        for car in self.all_car:
            if car.xcor()<-300:
                self.all_car.remove(car)
                car.hideturtle()
            car.backward(CARS_SPEED)

    def increase_speed(self):
        global CARS_SPEED
        CARS_SPEED += INCREASE_SPEED
