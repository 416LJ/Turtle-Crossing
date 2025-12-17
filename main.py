import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=700)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
score = Scoreboard()
player = Player()
screen.onkey(player.up, "Up")
speed = 0.1
car_list = []
num_of_cars = 5

def create_cars():
    for i in range(num_of_cars):
        car_list.append(CarManager())

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    if random.randint(1,6) == 1:
        create_cars()
    for car in car_list:
        car.move()
        if player.distance(car) < 25:
            game_is_on = False
            score.game_over()
    if player.check_finish():
        score.update_score()
        for car in car_list:
            car.car_reset()
        player.reset_turtle()
        speed *= 1.1

screen.exitonclick()
