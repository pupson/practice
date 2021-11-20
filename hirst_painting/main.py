"""

import colorgram

colors = colorgram.extract('spots.jpg', 30)
color_lst = []

for color in range(len(colors)):
    col = colors[color]
    red = (col.rgb.r)
    green = (col.rgb.g)
    blue = (col.rgb.b)
    col_tuple = (red, green, blue)

    color_lst.append(col_tuple)

print(color_lst)
"""

import turtle as t
import random

leo = t.Turtle()
t.colormode(255)
leo.pu()
leo.hideturtle()

leo.shape('circle')
leo.speed('fastest')

col_lst = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
           (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
           (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
           (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203),
           (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]


leo_x = -270
leo_y = -230

for _ in range(10):
    leo.pu()
    leo.goto(leo_x, leo_y)
    for _ in range(10):
        col = random.choice(col_lst)
        leo.fd(50)
        leo.dot(20, col)
    leo_y += 50

screen = t.Screen()
screen.exitonclick()