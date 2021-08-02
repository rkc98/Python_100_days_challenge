from turtle import Screen, Turtle


timmy=Turtle()
screen =Screen()

def forward():
    timmy.forward(50)
def backward():
    timmy.backward(50)
def clock():
    timmy.right(10)
def anticlock():
    timmy.left(10)
def clear():
    timmy.clear()
screen.listen()
screen.onkeypress(forward,key="w")
screen.onkeypress(backward,key="s")
screen.onkeypress(clock,key="d")
screen.onkeypress(anticlock,key="a")
screen.onkeypress(clear,key="c")





screen.exitonclick()