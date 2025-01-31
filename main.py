import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(3)

screen.update()
screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")

game_running = True
last_pos = None
food = Food()
scoreboard = Scoreboard()

while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Food Collision
    if snake.head.distance(food) < 15:
        food.reset()
        scoreboard.add()
        snake.grow()
    # Wall Collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("Snake hit the wall")
        scoreboard.gameover()
        screen.update()
        snake.reset()
    # Tail Collision
    for body_part in snake.body[1:]:
        if snake.head.distance(body_part) < 10:
            scoreboard.gameover()
            screen.update()
            snake.reset()

screen.exitonclick()
