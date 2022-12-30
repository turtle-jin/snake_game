from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """A simple attempt to model a snake."""

    def __init__(self):
        """initialize the snake body and create snake attributes"""
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        """create a new snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")  # when creating a new turtle instance, you can set the shape of the turtle
        new_segment.color("green")
        new_segment.shapesize(stretch_wid=0.8, stretch_len=0.8)
        new_segment.penup()
        new_segment.goto(position)
        self.all_snakes.append(new_segment)

    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.all_snakes[-1].position())

    def move(self):
        """make snake segments all move at the same time"""
        for seg_num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[seg_num - 1].xcor()
            new_y = self.all_snakes[seg_num - 1].ycor()
            self.all_snakes[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """make snake head go up"""
        if self.head.heading() != DOWN:  # be careful not to forget the ()after heading because it's a method.
            self.head.setheading(UP)

    def down(self):
        """make snake head go down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """make snake head go left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """make snake head go right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

