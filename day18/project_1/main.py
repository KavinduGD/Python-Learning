import math
import turtle
from turtle import Turtle, Screen
import random

joe = Turtle()
joe.shape('turtle')
# joe.color('red')


# for lines in range(3, 11):
#     R = random.random()
#     B = random.random()
#     G = random.random()
#     joe.color(R, G, B)
#     for line in range(lines):
#         joe.forward(100)
#         joe.right(360/lines)

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]

# joe.pensize(8)
# joe.speed('fastest')

# for round in range(0, 200):
#     joe.color(random.choice(colors))
#     joe.forward(20)
#     joe.right(random.choice(directions))

joe.speed('fastest')

for _ in range(72):
    R = random.random()
    B = random.random()
    G = random.random()
    joe.color(R, G, B)
    joe.circle(100)
    joe.setheading(joe.heading()+5)
    print(joe.heading())


screen = Screen()
screen.exitonclick()
