from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1
UP = 90
DOWN = 270
MOVE_DIST = 20


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.shape('square')
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.color('white')
        self.pu()
        self.goto(self.x_pos, self.y_pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



