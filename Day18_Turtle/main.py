# import colorgram
import turtle as turtle_module
import random

# extract colors from image using colorgram library. Adding color rgb values to a list of tuples
# color_pallet = []
# colors = colorgram.extract('pokemon-wooper-1217903.jpg', 20)
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_pallet.append(new_color)

# print(color_pallet)

color_list = [(17, 43, 18), (58, 115, 59), (173, 220, 234), (105, 188, 113), (35, 84, 38), (81, 162, 86), (26, 29, 15),
              (195, 154, 172), (157, 219, 141), (104, 173, 179), (188, 234, 199), (47, 86, 109), (20, 39, 46),
              (158, 179, 123), (89, 97, 68), (144, 73, 89), (181, 216, 134), (63, 74, 40), (121, 154, 80),
              (157, 209, 217)]

painter = turtle_module.Turtle()
turtle_module.colormode(255)
painter.hideturtle()
painter.speed("fastest")

painter.penup()
painter.setheading(225)
painter.forward(300)
painter.setheading(0)
painter.pendown()
starting_position = painter.position()


def paint_dots(size):
    counter = 0
    spacing = 0

    while counter <= 9:
        for _ in range(10):
            painter.dot(size, random.choice(color_list))
            painter.penup()
            painter.forward(50)
            painter.pendown()
            spacing += 5
        reset_paint_position(spacing)
        counter += 1


def reset_paint_position(num_spaces):
    painter.penup()
    painter.backward(9)
    painter.setposition(starting_position)
    painter.setheading(90)
    painter.forward(num_spaces)
    painter.setheading(0)


paint_dots(20)

screen = turtle_module.Screen()
screen.exitonclick()
