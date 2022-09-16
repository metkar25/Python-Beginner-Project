from turtle import Turtle
import random
import turtle

tom = Turtle()
colour = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
angle = [0,90,180,270]
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for _ in range(200):
    tom.pensize(10)
    tom.speed("normal")
    tom.color(random_color())
    tom.forward(25)
    tom.setheading(random.choice(angle))