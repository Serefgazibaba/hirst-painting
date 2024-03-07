"""import colorgram

rgb_colors = []
colors = colorgram.extract('damien_hirst.jpg',20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)
"""
from turtle import Turtle,Screen,colormode
import random


t = Turtle()

color_list = [(212, 13, 9), (197, 12, 35), (231, 228, 5), (197, 69, 20), (32, 90, 188), (43, 212, 70), (234, 149, 40), (33, 31, 152), (16, 22, 55), (66, 9, 48), (240, 245, 251), (244, 39, 149), (65, 203, 229), (14, 205, 222), (63, 21, 10), (223, 20, 110)]
colormode(255)
def draw():
    color = random.choice(color_list)
    t.pendown()
    t.dot(20, color)
    t.penup()


def move():
    t.forward(50)


def locate(x_coordinate, y_cordinate):
    t.teleport(x_coordinate,y_cordinate)

t.penup()
t.setheading(225)
t.forward(250)
t.setheading(0)
x_cor = t.xcor()
t.pendown()
y_cor = t.ycor()
for i in range(10):
    locate(x_cor, y_cor)
    y_cor += 50
    for j in range(10):
        draw()
        move()
t.hideturtle()
s = Screen()
s.exitonclick()