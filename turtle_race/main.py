from turtle import Turtle, Screen
import random


is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Enter bet", prompt="Pick a turtle to win, enter color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

y_loc = -175
turtle_lst = []

for col in range(len(colors)):
    y_loc += 50
    turtle_name = colors[col]
    turtle_name = Turtle(shape="turtle")
    turtle_name.color(colors[col])
    turtle_name.pu()
    turtle_name.goto(x=-230, y=y_loc)
    turtle_lst.append(turtle_name)

if user_bet:
    is_race_on = True

while is_race_on:
    for turt in turtle_lst:
        rand_dist = random.randint(0, 10)
        turt.forward(rand_dist)
        if turt.xcor() >= 210:
            is_race_on = False
            if user_bet == turt.pencolor():
                print(f'{turt.pencolor()} won! You picked the winner!')
            else:
                print(f'{turt.pencolor()} won, you lost')



screen.exitonclick()