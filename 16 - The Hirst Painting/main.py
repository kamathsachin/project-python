import turtle as turtle_module
import random

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24),
              (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

# import colorgram
#
# colors_in_image = colorgram.extract("image.jpg", 10)
# colors = []
#
# for color in colors_in_image:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     colors.append((r, g, b))
#
# print(colors)
