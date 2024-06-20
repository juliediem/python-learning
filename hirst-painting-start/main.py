import turtle
import colorgram
import random

t = turtle.Turtle()
turtle.colormode(255)
t.penup()
t.speed("fastest")

rgb_colors = []
rgb_tuples = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    rgb_colors.append(color.rgb)
    rgb_tuples.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgb_tuples)

# Starting position
t.setpos(-250, -250)

# Draw the dots
for i in range(10):
    for j in range(10):
        t.dot(20, random.choice(rgb_tuples))
        t.forward(50)
    t.setx(-250)
    t.sety(t.ycor() + 50)

turtle.done()
