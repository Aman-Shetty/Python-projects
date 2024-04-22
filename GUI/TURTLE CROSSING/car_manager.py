from turtle import Turtle
import random
from scoreboard import Scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
score = Scoreboard()


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.level = 1
        score.update_scoreboard(self.level)

    def car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(random.randint(300, 310), random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.level += 1
        self.car_speed += MOVE_INCREMENT
        score.update_scoreboard(self.level)

