
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle gonna win?")
colors = ["red", "orange", "yellow", "green", "purple", "black"]
y_index = [-100, -70, -40, -10, 20, 50]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_index[turtle_index])
    new_turtle.pendown()
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bet:
                print(f"You won the winner turtle is {winner_turtle}")
            else:
                print(f"You lost the winner turtle is {winner_turtle}")

        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
