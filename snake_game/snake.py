import turtle
from turtle import Screen, Turtle

MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        """Initializes Snake object with it's starting positions, creates the body of the snake, identifies the head of the snake and sets the snakes direction to default of Right"""
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "Right"

    def create_snake(self):
        """Creates the snake body"""
        for position in self.position:
            self.add_segment(position)
            

    def add_segment(self, position):
        """Creates the snake body"""
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.segments.append(snake_part)

    def move(self):
        """Moves the snake, by using the head of the snake to lead and then getting the second square to go in the place where the head was, and the third square to go where the second square used to be"""
        for part in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[part - 1].xcor()
            new_y = self.segments[part - 1].ycor()
            self.segments[part].goto(new_x, new_y)
        self.head.forward(MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.direction = "Up"

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.direction = "Down"

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.direction = "Left"

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.direction = "Right"