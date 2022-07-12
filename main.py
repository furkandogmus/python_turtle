import random
import time
from turtle import Screen

from Paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(height=600, width=600)

screen.tracer(False)
score = Score("right")
score1 = Score("left")
screen.bgcolor("black")
paddle = Paddle("right")
paddle2 = Paddle("left")
ball = Ball()

screen.listen()
screen.onkeypress(fun=paddle2.move_up, key="w")
screen.onkeypress(fun=paddle2.move_down, key="s")
screen.onkeypress(fun=paddle.move_up, key="Up")
screen.onkeypress(fun=paddle.move_down, key="Down")

screen.tracer(True)

game_is_on = True
while game_is_on:
    if abs(ball.xcor()) <= 280:
        ball.move()
        if paddle.distance(ball) < 50:
            ball.forward(20)  # to balance the distance between the paddle and the ball.
            ball.setheading(180 - ball.heading())
            ball.forward(50)
        elif paddle2.distance(ball) < 50:
            ball.forward(20)  # to balance the distance between the paddle and the ball.
            ball.setheading(180 - ball.heading())
            ball.forward(50)
    else:
        if ball.xcor() > 280:
            score.increase_score()
        elif ball.xcor() < -280:
            score1.increase_score()
        if score.score != 12 and score1.score != 12:
            screen.tracer(False)
            # set coordinates to starting points. --
            ball.goto(0, 0)
            paddle.goto(paddle.xcor(), 0)
            paddle2.goto(paddle2.xcor(), 0)
            # --
            screen.tracer(True)
            time.sleep(1)  # wait a second to start.
            ball.setheading(random.choice([180 - ball.heading(), -180 + ball.heading()]))
        else:
            score.game_over()
            game_is_on = False
screen.exitonclick()
