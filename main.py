import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Street
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
street = Street()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkeypress(key='w', fun=player.move)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # TODO 1: Create a Car
    car_manager.create_car()
    # TODO 2: Move the cars generated
    car_manager.start_highway()

    # TODO 3: Detect when the Turtle collides with a Car
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # TODO 6: Check if Turtle reach top, then next level.
    if player.ycor() > 270:
        scoreboard.level_up()
        player.go_to_start_position()
        car_manager.speed_increase()


screen.exitonclick()

