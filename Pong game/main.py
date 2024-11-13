#The Pong game

# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height = 600, width = 800)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(key = "w", fun = l_paddle.paddle_up)
screen.onkey(key = "s", fun = l_paddle.paddle_down)
screen.onkey(key = "Up", fun = r_paddle.paddle_up)
screen.onkey(key = "Down", fun = r_paddle.paddle_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()
    
    #Ball bounces off upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Ball bounces off the paddle
    if ball.distance(r_paddle) < 45 and ball.xcor() > 323 or ball.distance(l_paddle) < 45 and ball.xcor() < -323:
        ball.bounce_x()
        ball.increase_speed()
    
    #When right paddle misses
    if ball.xcor() > 380: 
        score.l_point()
        ball.reset_position()

    #When left paddle misses
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()




screen.exitonclick()
