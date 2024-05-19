import random
from turtle import Turtle, Screen

turtle_list = []
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

screen = Screen()
screen.setup(width=500, height=400)

for index in range(6):
    turtle = Turtle()
    turtle.color(colors[index])
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-200, 175-(70*index))
    turtle_list.append(turtle)


selected_color = screen.textinput(title="Make your bet",
                                  prompt="Which turtle will win the race: ")
race_is_on = True
winner = ''

while race_is_on:
    for index in range(6):
        turtle = turtle_list[index]
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            race_is_on = False
            winner = turtle.pencolor()
            print(winner)
            break

if winner == selected_color:
    print('Your bet has won')
else:
    print('Your bet has lost, winner is ' + winner)


screen.exitonclick()
