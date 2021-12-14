from turtle import Turtle
import random

COLORS = ["red", "orange", "blue", "gold", "green", "purple"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.setposition(x=self.ran_x_start(), y=self.ran_y())

    def ran_y(self):
        rand_y = random.randint(-250, 250)
        return rand_y

    def ran_x_start(self):
        rand_x_st = random.randint(50, 600)
        return rand_x_st

    def ran_x(self):
        rand_x = random.randint(280, 600)
        return rand_x

    def move(self):
        if self.xcor() < -330:
            self.setposition(x=self.ran_x(), y=self.ran_y())
        self.backward(5)
