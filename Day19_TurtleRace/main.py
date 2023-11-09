import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "orange", "yellow", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtle_fleet = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtle_fleet.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in turtle_fleet:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()
