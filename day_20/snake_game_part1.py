from turtle import Screen
import time
from snake import Snake

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("MY Snake Game")
screen.tracer(0)
screen.listen()
game_on=True

snake=Snake()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")


while game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    



screen.exitonclick()

