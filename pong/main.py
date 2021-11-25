from scoreboard import Scoreboard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350, 0))
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')

l_paddle = Paddle((-350, 0))
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

ball = Ball()
r_scoreboard = Scoreboard((150, 270), 'Right')
l_scoreboard = Scoreboard((-150, 270), 'Left')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect collision with y wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # Detect collision with rx wall
    if ball.xcor() > 380:
        #
        ball.reset_position()
        l_scoreboard.increase_score('Left')
        if l_scoreboard.score > 5:
            l_scoreboard.game_over('Left')
            game_is_on = False

    # Detect collision with rx wall
    if ball.xcor() < -380:
        ball.reset_position()
        r_scoreboard.increase_score('Right')
        if r_scoreboard.score > 5:
            r_scoreboard.game_over('Right')
            game_is_on = False



screen.exitonclick()