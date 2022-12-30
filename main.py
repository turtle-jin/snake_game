from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
user_score = Scoreboard()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        user_score.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        user_score.game_over()

    # Detect collision with tail
    for segment in snake.all_snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            user_score.game_over()

screen.exitonclick()
