from turtle import Screen, Turtle, color
import random
tim=Turtle()
initial_length=3
degree=360
tim.speed(1)
color=['red','blue','green','Black','Cyan','Brown','Orange','maroon']
for _ in range(initial_length,11):
    change_in_degrees=degree/initial_length
    tim.color(random.choice(color))

    for _ in range(initial_length):
        
        tim.forward(100)
        tim.right(change_in_degrees)
    initial_length+=1
screen =Screen()
screen.exitonclick()





