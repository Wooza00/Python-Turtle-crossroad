from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setposition(x=0, y=-280)
        self.setheading(90)

    def move(self):
        self.forward(20)
