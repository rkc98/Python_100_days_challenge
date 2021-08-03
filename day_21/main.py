from scoreboard import Scoreboard
from food import Food
from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("MY Snake Game")
screen.tracer(0)
screen.listen()
game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    for segment in snake.segemnts[1:]:
        
        if snake.head.distance(segment)<10:
            game_on=False
            scoreboard.game_over()


screen.exitonclick()
