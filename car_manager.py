import random
from turtle import Turtle

COLORS = ["#121212", "#2D4263", "#6998AB", "#FF8E00", "#8B9A46", "#F39189", "#CE1212"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-245, 250))
            self.car_list.append(new_car)

    def start_highway(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT


class Street(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.x = -300
        self.y = -260
        self.street_lines(2)

    def street_lines(self, x):
        self.hideturtle()
        self.penup()
        self.goto(self.x, self.y)
        self.pendown()
        self.forward(280)
        self.pencolor("yellow")
        self.forward(40)
        self.pencolor("black")
        self.forward(280)
        # Recursion
        if x == 1:
            return 1
        else:
            self.x = -300
            self.y = 260
            return self.street_lines(x - 1)
