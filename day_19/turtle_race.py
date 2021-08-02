from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="enter the color of turtle")
colors=["red","yellow","green","blue","orange","purple"]
# print(user_bet)
race=False
y_axis=-100
all_turtles=[]
for index in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230,y=y_axis)
    y_axis+=42
    all_turtles.append(tim)
print(all_turtles)
if user_bet:
    race=True
while race:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            win_color=turtle.pencolor()
            if win_color==user_bet:
                print(f"you turtle {win_color} won!!")
                race=False
            else:
                print(f"you lost {win_color} turtle won!!")
                race=False
            
        distance=random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()