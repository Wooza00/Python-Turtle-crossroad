from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(x=-240, y=260)
        self.level = 0
        self.write(arg=f"Level: {self.level}", align="center", font=("courier", 12, "bold"))

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=("courier", 12, "bold"))

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=("courier", 20, "bold"))
