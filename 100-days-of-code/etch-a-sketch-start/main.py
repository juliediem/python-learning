import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


screen.listen()
# screen.onkey(key="space", fun=move_forwards)


# TODO Create a turtle that will allow you to press the W Key to go forwards
screen.onkey(key="w", fun=move_forwards)
# TODO S key to go backwards
screen.onkey(key="s", fun=move_backwards)
# TODO A key to go counterclockwise/left
screen.onkey(key="a", fun=move_left)
# TODO D to go right/clockwise
screen.onkey(key="d", fun=move_right)
# TODO go up and right to draw a curve
# not sure if this is just what happens?
# TODO C to clear drawing
screen.onkey(key="c", fun=screen.reset)

screen.exitonclick()
