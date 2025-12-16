from random import random
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = - MOVE_INCREMENT
        self.y_move = 0
        self.far_apart = 5000
        self.car_reset()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def car_reset(self):
        self.penup()
        self.speed("slowest")
        self.color(random.choice(COLORS))
        self.shape("square")
        self.far_apart += 1000
        self.goto((random.randint(-300, self.far_apart), (random.randint(-250, 300))))
        self.shapesize(stretch_wid=1, stretch_len=2)
