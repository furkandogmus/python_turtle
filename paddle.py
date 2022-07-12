from turtle import Turtle

POSITIONS = [(0, 0), (0, 20), (0, 40)]


class Paddle(Turtle):
    def __init__(self, way):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.setheading(90)
        self.penup()
        if way == "right":
            self.goto(280, 0)
        else:
            self.goto(-287, 0)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)
