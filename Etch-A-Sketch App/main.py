from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forwared():
    tom.forward(15)

def move_backward():
    tom.backward(15)

def move_right():
    tom.right(10)

def move_left():
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)

def screen_clear():
    tom.clear()
    tom.up()
    tom.home()
    tom.down()

screen.listen()
screen.onkeypress(move_forwared, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(move_right, "d")  
screen.onkeypress(move_left, "a")
screen.onkeypress(screen_clear, "c")
screen.exitonclick()
