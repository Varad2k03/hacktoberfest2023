from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = Car()
scoreboard = Scoreboard()


screen.onkeypress(player.move, "Up")

game_is_on = True

while(game_is_on):
    cars.create_car()
    cars.move()

    # Detecting collision with player
    for car in cars.all_car:
        if player.distance(car) < 20 or (player.distance(car)<36 and (player.ycor()-car.ycor()) in range(-23, 23)):
            game_is_on = False
            scoreboard.game_over()
        

    if player.is_at_finish_line():
        scoreboard.level_up()
        cars.increase_speed()
        player.starting_position()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()