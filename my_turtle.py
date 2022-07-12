from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.shapesize(2)
        self.goto(0, -290)
        self.setheading(90)
        self.speed = 10

    def move(self):
        self.forward(self.speed)

    def stop(self):
        self.speed= 0