from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_clockwise():
    current_heading = tim.heading()
    tim.setheading(current_heading + 15)


def rotate_counter_clockwise():
    current_heading = tim.heading()
    tim.setheading(current_heading - 15)


def reset_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="c", fun=reset_drawing)

screen.exitonclick()
