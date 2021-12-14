from turtle import Screen
import time
from player import Player
from car import Car
import random
from score import Score


player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(player.move, key="Up")

amount_of_cars = random.randint(10, 30)
cars = [Car() for i in range(amount_of_cars)]
score = Score()

speed = 0.1
game_on = True

while game_on:
    screen.update()
    time.sleep(speed)
    for car in cars:
        car.move()
        car_y = car.ycor()
        pla_y = player.ycor()
        abs_y = abs(car_y - pla_y)
        abs_x = abs(car.xcor())

        if abs_y < 18 and abs_x <= 20:
            game_on = False
            score.game_over()

        if player.ycor() > 280:
            score.level_up()
            score.update_score()
            time.sleep(1)
            player.setposition(0, -280)
            speed -= 0.005


screen.exitonclick()
