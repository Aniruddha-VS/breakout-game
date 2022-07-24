from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Brick
import time


game_ball = Ball()
scoreboard = Scoreboard()

my_screen = Screen()
my_screen.title("Breakout")
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)

paddle = Paddle((0, -280))

my_screen.update()

my_screen.listen()
my_screen.onkey(paddle.go_right, "Right")
my_screen.onkey(paddle.go_left, "Left")

game_is_on = True
bricks = []


def build_bricks():
    x_delta = 50
    y_delta = 30
    x_new = -380
    y_new = 200
    for color in ["red", "green", "yellow"]:
        for index in range(16):
            new_brick = Brick((x_new ,y_new))
            x_new += x_delta
            new_brick.color(color)
            bricks.append(new_brick)
        x_new = -380
        y_new -= y_delta
build_bricks()


while game_is_on:

    game_ball.move()
    time.sleep(game_ball.move_speed)
    my_screen.update()
    scoreboard.update_score()

    if game_ball.ycor() < -280:
        game_ball.reset_position()
        scoreboard.reset()
        build_bricks()

    for brick in bricks:
        if game_ball.distance(brick) < 50:
            game_ball.bounce_y()
            brick.goto(800, 800)
            scoreboard.increase_score()
            time.sleep(0.2)

    if game_ball.ycor() < 280 and game_ball.distance(paddle) < 50:
        game_ball.bounce_y()

    if game_ball.ycor() > 280:
        game_ball.bounce_y()

    if game_ball.xcor() > 380 or game_ball.xcor() < -380:
        game_ball.bounce_x()


my_screen.exitonclick()





