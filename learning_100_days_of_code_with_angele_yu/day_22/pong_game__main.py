# The Pong Game 👇

from turtle import Screen

from pong_game__paddle import Paddle
from pong_game__ball import Ball
from pong_game__scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -283:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
            ball.bounce_x()

    # Detect when the ball goes out of bounds
    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        # Score Keeping
        scoreboard.l_point()

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        # Score Keeping
        scoreboard.r_point()


screen.exitonclick()
