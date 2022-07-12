from turtle import Turtle

FONT = ["Arial", 24, "normal"]


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-230, 260)
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.level+=1
        self.write(f"Level: {self.level}", font=FONT, align="center")
