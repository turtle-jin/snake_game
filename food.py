from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-260, 280, 20)  # to make the food appear in the middle of the snake's path.
        random_y = random.randrange(-260, 280, 20)  # random.choice(range(-280, 280, 20)) or just use randrange()
        self.goto(random_x, random_y)
