import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
score = Scoreboard()
player = Player()
screen.onkey(player.up, "Up")

speed = 0.1

car_list = []

for i in range(random.randint(1,1000)):
    car_list.append(CarManager())

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()

    for car in car_list:
        car.move()
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if player.check_finish():
        score.update_score()
        for car in car_list:
            car.car_reset()
        player.reset_turtle()
        speed *= 0.9

screen.exitonclick()


