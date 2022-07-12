import math
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(2)
        self.shape("circle")
        self.penup()
        self.color("red")
        self.left(30)

    def move(self):
        self.forward(10)
        if self.ycor() > 280:
            self.setheading(360 - self.heading())
        if self.ycor() < -280:
            self.setheading(360 - self.heading())