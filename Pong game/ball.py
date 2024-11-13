# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
    
    def move_ball(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
    
    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
    
    def increase_speed(self):
        self.ball_speed *= 0.9



