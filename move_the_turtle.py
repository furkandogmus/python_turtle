from turtle import Screen, Turtle

tim = Turtle()
tim.speed("fastest")
screen = Screen()
x = 0
def move_forward():
    tim.forward(20)


def move_backward():
    tim.back(20)


def turn_left():
    tim.left(90)


def turn_right():
    tim.right(90)


def pen_up_and_down():
    global x
    if x % 2 == 0:
        tim.penup()
        x += 1
    else:
        tim.pendown()
        x += 1


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkey(key="space", fun=pen_up_and_down)
screen.onkeypress(key="c", fun=screen.resetscreen)

screen.exitonclick()
