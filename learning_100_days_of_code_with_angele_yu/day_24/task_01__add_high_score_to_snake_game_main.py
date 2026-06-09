# Snake Game Improvement ==> We want to add the highest score 👇

from turtle import Screen
from task_01__add_high_score_to_snake_game_snake import Snake
from task_01__add_high_score_to_snake_game_food import Food
from task_01__add_high_score_to_snake_game_scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Control the Snake with a Keypress
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collisions with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collisions with wall.
    if snake.head.xcor() < -300 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 300:
        # game_is_on = False
        # scoreboard.game_over()
        snake.reset()
        scoreboard.reset()


    # Detect collisions with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            snake.reset()
            scoreboard.reset()


screen.exitonclick()
