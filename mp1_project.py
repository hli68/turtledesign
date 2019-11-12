import turtle
turtle.colormode(255)
bob=turtle.Turtle()
bob.speed(0)
def sungod(distance):
    bob.begin_fill()
    for times in range(73):
        bob.forward(distance)
        bob.left(170)
    bob.end_fill()
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
