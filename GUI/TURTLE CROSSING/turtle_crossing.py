from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.gameover()
            game_is_on = False

    if player.finish_line():
        car_manager.level_up()

screen.exitonclick()