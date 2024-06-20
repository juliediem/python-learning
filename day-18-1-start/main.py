#####Turtle Intro######

import turtle as t
import random
# tim = t.Turtle()
turtle = t.Turtle()
turtle.speed("fastest")
# tim.shape("turtle")
# tim.color("plum")



######## Challenge 1 - Draw a Square ############
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

#This is for the turtle to poop
# for i in range(0,10):
#     tim.forward(20)
#     tim.penup()
#     tim.forward(20)
#     tim.pendown()

# #Triangle
# tim.forward(100)
# tim.left(120)
# tim.forward(100)
# tim.left(120)
# tim.forward(100)

# colors = ["hot pink","violet","cornflower blue","dark sea green","dark olive green","sandy brown","dark orange","orange red"]
t.colormode(255)


# #Random Walk exercise
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tuple_colors = (r,g,b)
    return tuple_colors
#
#
# directions = [0, 90, 180, 270]
#
# for i in range(100):
#     colors=random_color()
#     tim.pen(pensize=10, pencolor=colors)
#     tim.fd(30)
#     tim.setheading(random.choice(directions))


## Square
# tim.left(120)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)


## Drawing nested shapes

# for i in range(3,10):
#     angle = 360/i
#     tim.pen(pensize=1, pencolor=random.choice(colors))
#     for j in range(0,i):
#         tim.forward(100)
#         tim.left(angle)


#Draw spirograph, tilt a circle
# tim.circle(100)
# tim.tilt(30)
# tim.heading(50)
# tim.forward(100)

for i in range(0,72):
    colors = random_color()
    turtle.pen(pensize=1, pencolor=colors)

    turtle.setpos(0, 0)
    turtle.pos()
    turtle.circle(100)
    multiplier = i*5
    turtle.setheading(10+multiplier)

my_screen = t.Screen()
my_screen.exitonclick()
