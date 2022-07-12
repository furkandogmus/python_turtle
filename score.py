from turtle import Turtle

FONT = ("Arial", 24)


class Score(Turtle):
    def __init__(self, way):
        super().__init__()
        self.id = way
        self.hideturtle()
        self.penup()
        if way == "right":
            self.goto(-20, 260)
        else:
            self.goto(20, 260)
        self.color("white")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(self.score, font=FONT, align="center")

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")
