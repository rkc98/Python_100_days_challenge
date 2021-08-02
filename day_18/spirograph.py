from turtle import Screen, Turtle
import random


tim=Turtle()
tim.speed(0)
screen=Screen()
screen.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
for _ in range(0,360,5):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.left(5)
screen.exitonclick()




