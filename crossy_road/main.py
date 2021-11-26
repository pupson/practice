import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Crossy Turtle')
screen.listen()
screen.tracer(0)

player = Player()
screen.onkey(player.up, 'Up')
screen.onkey(player.left, 'Left')
screen.onkey(player.right, 'Right')

scoreboard = Scoreboard()

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    if player.ycor() > 280:
        scoreboard.increase_score()
        car_manager.level_up()
        player.reset_position()

    for car in car_manager.car_lst:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()