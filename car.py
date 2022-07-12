import random
from my_turtle import Turtle

colors = ["red", "green", "blue", "purple", "pink", "black", "grey", "yellow", "orange"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(colors))
        self.penup()
        self.speed("fastest")
        self.setheading(180)
        self.goto(300, random.randint(-230, 260))

    def move_up(self, speed):
        self.forward(speed-5)

    def delete(self):
        self.delete()
