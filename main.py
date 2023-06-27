from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Snake's movements
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    # Slowing down the speed of the snake
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Eating a food
    if snake.head.distance(food) < 15:
        food.refresh() 
        scoreboard.increaseScore()
        snake.extend()

    # Checking for collision with edges of the screen
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        game_is_on = False
        scoreboard.game_over()

    # Checking collision of head of the snake with other segments of the snake
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) <10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()