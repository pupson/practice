from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.pu()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        self.setheading(90)
        self.move()


    def left(self):
        self.setheading(180)
        self.move()

    def right(self):
        self.setheading(0)
        self.move()

    def reset_position(self):
        self.goto(STARTING_POSITION)