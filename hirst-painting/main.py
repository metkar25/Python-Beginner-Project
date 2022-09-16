from turtle import Turtle, Screen
import random
import turtle
"Process to extract color(rgb) from an image "
# import colorgram
# rgb = []
# colors = colorgram.extract("D:\Python-Beginner-Project\hirst-painting\image.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb.append(new_color)
# print(rgb)
turtle.colormode(255)
tom = Turtle()
color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]
tom.pu()
tom.speed("fastest")
tom.hideturtle()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+ 1):
    tom.dot(20, random.choice(color_list))
    tom.forward(50)
    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)
screen = Screen()
screen.exitonclick()