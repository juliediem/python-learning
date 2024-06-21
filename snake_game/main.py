import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


def snake_body():
    segments = []
    for i in range(0, 3):
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        x_cor = -20
        snake_part.setx(x_cor * i)
        snake_part.sety(0)
        print(snake_part.pos())
        segments.append(snake_part)
    return segments


new_snake = snake_body()
print(new_snake)

game_is_on = True
while game_is_on:
    for seg in new_snake:
        seg.forward(20)



screen.exitonclick()
