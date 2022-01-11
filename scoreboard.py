from turtle import Turtle
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.start_level()

    def start_level(self):
        self.hideturtle()
        self.penup()
        self.goto(-240, 265)
        self.write(f"Level {self.level}", move=False,
                   align="center", font=FONT)

    def level_up(self):
        self.reset()
        self.level += 1
        self.start_level()

    def game_over(self):
        self.reset()
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align='center', font=FONT)
        pass




