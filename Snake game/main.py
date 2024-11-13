#The Snake Game

# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 10:
        score.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 7:
            game_is_on = False
            score.game_over()


    


    












screen.exitonclick()
