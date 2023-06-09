from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_pieces = []
        self.create_snake()
        self.head = self.snake_pieces[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake_pieces.append(new_turtle)

    def reset(self):
        for segments in self.snake_pieces:
            segments.goto(1000,1000)
        self.snake_pieces.clear()
        self.create_snake()
        self.head = self.snake_pieces[0]

    def extend(self):
        self.add_segment(self.snake_pieces[-1].position())

    def move(self):
        for pieces in range(len(self.snake_pieces) - 1, 0, -1):
            new_x = self.snake_pieces[pieces - 1].xcor()
            new_y = self.snake_pieces[pieces - 1].ycor()
            self.snake_pieces[pieces].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self): #90 grade
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self): #270 grade
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self): #180 grade
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):#0 grade
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)