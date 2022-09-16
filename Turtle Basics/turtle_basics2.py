from turtle import Turtle
import random

tom = Turtle()
colour = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
angle = [0,90,180,270]
for _ in range(200):
    tom.pensize(10)
    tom.speed("normal")
    tom.color(random.choice(colour))
    tom.forward(25)
    tom.setheading(random.choice(angle))