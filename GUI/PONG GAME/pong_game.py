import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from ScoreBoard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(1600, 1000)
screen.tracer(0)

mid = Turtle()
mid.ht()
mid.color("white")
mid.goto(x=0, y=500)
mid.goto(0, -500)
r_paddle = Paddle((750, 0))
l_paddle = Paddle((-750, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 480 or ball.ycor() < -480:
        ball.bounce_y()


    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 725 or ball.distance(l_paddle) < 50 and ball.xcor() < -725:
        ball.bounce_x()

    #Detect ball miss r_paddle
    if ball.xcor() > 780:
        ball.reset_position()
        scoreboard.l_point()

    #l_paddle
    if ball.xcor() < -780:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
