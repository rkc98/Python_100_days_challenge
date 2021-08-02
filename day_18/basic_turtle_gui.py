from turtle import Screen, Turtle
import heroes
timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')
timmy.speed('slowest')
print(heroes.gen())
# for _ in range(4):
#     timmy.right(90)
#     timmy.forward(100)

for _ in range(8):
    timmy.pensize(4)
    timmy.pendown()
    timmy.forward(15)
    timmy.penup()
    timmy.forward(15)


screen = Screen()
screen.exitonclick()
