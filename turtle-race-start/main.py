#
import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet","Which turtle will win the race? Enter a color")
colors = ["red","orange","yellow","green","blue"]
all_turtles=[]

for i in range(0,5):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230,-100+50*i)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()