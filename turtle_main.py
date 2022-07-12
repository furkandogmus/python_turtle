import level
from level import Level
from my_turtle import MyTurtle
from turtle import Screen

from car import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(False)
car = Car()
my_turtle = MyTurtle()
level_board = Level()
screen.tracer(True)
screen.listen()
game_is_on = True
screen.onkeypress(fun=my_turtle.move, key="w")
cars = []
while game_is_on:
    if my_turtle.ycor() >= 280:
        level_board.update_level()
        screen.tracer(False)
        my_turtle.goto(0, -280)
        for car in cars:
            car.hideturtle()
        cars =[]
    if len(cars) < 50:
        screen.tracer(False)
        car = Car()
        cars.append(car)
        screen.tracer(True)
    else:
        cars = cars[1:]
    for car in cars:
        if car.distance(my_turtle) > 50:
            car.move_up(level_board.level *10)
        else:
            my_turtle.stop()
            game_is_on = False
screen.exitonclick()
