from turtle import Screen, Turtle
import random


color = ['red', 'blue', 'green', 'Black', 'Cyan', 'Brown', 'Orange', 'maroon']
tim = Turtle()
screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim.pensize(10)
tim.speed('slow')
direction = ["right", "left", "forward", "backward"]
for _ in range(300):
    if random.choice(direction) == "right":
        tim.pencolor(random_color())
        tim.right(90)
        tim.forward(30)
    elif random.choice(direction) == "left":
        tim.pencolor(random_color())
        tim.left(90)
        tim.forward(30)
    elif random.choice(direction) == "backward":
        tim.pencolor(random_color())
        tim.backward(30)
    elif random.choice(direction) == "forward":
        tim.pencolor(random_color())
        tim.forward(30)

screen.exitonclick()
