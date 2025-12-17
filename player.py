from turtle import Turtle

STARTING_POSITION = (0, -300)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 300


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.speed("slowest")
        self.color("red")
        self.reset_turtle()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def mov_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE,self.ycor())

    def mov_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE,self.ycor())

    def check_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True

    def reset_turtle(self):
        self.goto(STARTING_POSITION)
