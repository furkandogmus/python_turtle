import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        x, y = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(x, y)

    def random_position(self):
        x, y = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(x, y)

