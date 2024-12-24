#Turtle Crossing game

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key = "Up", fun = player.move_turtle)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.display_level()
    car_manager.create_car()    
    car_manager.move_car()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish_line():
        score.level_up()
        player.go_to_start()
        car_manager.increase_car_speed()

screen.exitonclick()    
