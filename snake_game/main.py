import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


def snake_body():
    for i in range(0, 3):
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        x_cor = -20
        snake_part.setx(x_cor * i)

snake = snake_body()
segments = [snake]

game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(20)

screen.exitonclick()
