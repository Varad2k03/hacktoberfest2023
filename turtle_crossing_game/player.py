from turtle import Turtle

PLAYER_SPEED = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.starting_position()

    def starting_position(self):
        self.goto(0, -280)

    def move(self):
        self.forward(PLAYER_SPEED)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        return False

        