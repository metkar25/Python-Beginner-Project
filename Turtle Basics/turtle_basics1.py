from turtle import Turtle, Screen
import random

# timmy = Turtle()
# timmy.shape("arrow")
# timmy.color("red")
# for _ in range(4):  
#     timmy.forward(100)
#     timmy.right(90)

tom = Turtle()
"Method - 1"
# colours = ["List of colours of your choice"]

# def draw_shape(num_sides):
#     angle = 360/ num_sides
#     for _ in range(num_sides):
#         tom.forward(100)
#         tom.right(angle)

# for shape_side_n in range(3, 11):
#     tom.color(random.choice(colours))
#     draw_shape(shape_side_n)
"Method -2"
for _ in range(3):  
    tom.forward(100)
    tom.right(120)   
for _ in range(4):
    tom.color("red")
    tom.forward(100)
    tom.right(90)
for _ in range(5):
    tom.color("yellow")
    tom.forward(100)
    tom.right(72)
for _ in range(6):
    tom.color("blue")
    tom.forward(100)
    tom.right(60)
for _ in range(7):
    tom.color("green")
    tom.forward(100)
    tom.right(51.42)
for _ in range(8):
    tom.color("pink")
    tom.forward(100)
    tom.right(45)
for _ in range(9):
    tom.color("gold")
    tom.forward(100)
    tom.right(40)
for _ in range(10):
    tom.color("maroon")
    tom.forward(100)
    tom.right(36)

screen = Screen()
screen.exitonclick()