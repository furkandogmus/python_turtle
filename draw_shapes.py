
import random
import turtle
from turtle import Turtle
import colorgram

colors = colorgram.extract("indir.jpg", 38)
turtle.colormode(255)
mex = Turtle()
mex.speed("fastest")
mex.hideturtle()
mex.pensize(20)


def random_color():
    color = colors[random.randint(0, 37)]
    rgb = color.rgb
    return rgb


def draw_shape(n):
    for _ in range(n):
        mex.forward(100)
        mex.right((360 / n))


def dashed_forward(i):
    for _ in range(int(i / 20)):
        mex.forward(10)
        mex.penup()
        mex.forward(10)
        mex.pendown()


def random_walk():
    mex.forward(random.randint(30, 50))
    mex.pencolor(random_color())
    if random.randint(0, 1):
        mex.left(90)
    else:
        mex.right(90)


def draw_spirograph():
    for _ in range(360):
        mex.left(2)
        mex.circle(100)
        mex.color(random_color())


def draw_dot():
    mex.penup()
    mex.setx(-350)
    mex.sety(-300)
    for y in range(-260, 400, 40):
        for x in range(-350, 350, 40):
            mex.setx(x)
            mex.dot(20, random_color())
        mex.sety(y)
