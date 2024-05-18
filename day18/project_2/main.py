import colorgram
from turtle import Turtle, Screen
import random
# rgb_color = []
# colors = colorgram.extract('painting.jpg', 30)
# for color in colors:
#     rgb_color.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_color)
screen = Screen()
screen.setup(width=500, height=500)

rgb_colors = [(216, 148, 92), (221, 78, 57), (45, 94, 146), (151, 64, 91), (232, 219, 93), (217, 65, 85), (22, 27, 41), (40, 22, 29), (120, 167, 197), (40, 19, 14), (194, 139, 159),
              (159, 72, 56), (35, 132, 91), (123, 181, 142), (69, 167, 94), (236, 222, 6), (170, 176, 42), (231, 168, 182), (14, 30, 21), (51, 54, 105), (106, 42, 61), (25, 168, 202), (236, 171, 161), (107, 44, 37), (163, 210, 185), (150, 207, 222)]


left_start = -225
bottom_start = -225

turtle = Turtle()
screen.colormode(255)

turtle.penup()
turtle.hideturtle()
turtle.setx(left_start)
turtle.sety(bottom_start)
turtle.showturtle()


def print_row():
    for _ in range(10):
        turtle. pencolor(random.choice(rgb_colors))
        turtle.dot(20)
        if (_ == 9):
            break
        else:
            turtle.forward(50)


for _ in range(10):
    print_row()
    x, y = turtle.pos()
    if _ != 9:
        turtle.sety(y+50)
        turtle.setx(left_start)


print_row()
screen.exitonclick()
