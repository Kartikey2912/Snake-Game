from turtle import Screen
from time import sleep
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# we have turned the tracer off then we can update the screen when we want.
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun= snake.up)
screen.onkey(key="Down", fun= snake.down)
screen.onkey(key="Right", fun= snake.right)
screen.onkey(key="Left", fun= snake.left)


game_on = True
while game_on:
    
    screen.update()  
    sleep(0.1) # this will produce a 0.1 seconds delay and then update the screen. Only then we will be able to 
    # watch our snake.
    
    
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail
    for segments in snake.list[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
