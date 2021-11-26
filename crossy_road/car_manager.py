from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        # super().__init__()
        self.car_lst = []
        self.car_speed = MOVE_INCREMENT


    def create_car(self):
        x = random.randint(1, 6)
        if x == 1:

            car_instance = Turtle()
            car_instance.shape('square')
            car_instance.pu()
            car_instance.shapesize(stretch_wid=1, stretch_len=2)
            car_instance.color(random.choice(COLORS))
            y_pos = random.randint(-200, 200)
            car_instance.goto(300, y_pos)
            self.car_lst.append(car_instance)

    def move(self):
        for car in self.car_lst:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
