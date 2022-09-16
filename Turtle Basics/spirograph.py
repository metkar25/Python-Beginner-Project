from multiprocessing.connection import answer_challenge
from turtle import Turtle, Screen
import random
import turtle

tom = Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

tom.speed("fastest")
def draw(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        tom.speed("normal")
        tom.color(random_color())
        tom.circle(100)
        current_heading = tom.heading()
        tom.setheading(current_heading + size_of_gap)
    
draw(50)
   
screen = Screen()
screen.exitonclick()