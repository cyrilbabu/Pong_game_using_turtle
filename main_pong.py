from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard

game = True

s = Screen()
s.bgcolor("black")
s.title("Pong")
s.setup(width=800, height=600)
s.tracer(0)


r_paddle = Paddle(direction="left")
l_paddle = Paddle(direction="right")
ball = Ball()
score = Scoreboard()

s.listen()
s.onkey(fun=r_paddle.up, key="Up")
s.onkey(fun=r_paddle.down, key="Down")
s.onkey(fun=l_paddle.up, key="w")
s.onkey(fun=l_paddle.down, key="s")

while game:
    ball.ball_move()
    s.update()
    time.sleep(ball.speed_time)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 80 and ball.xcor() > 340 or ball.distance(l_paddle) < 80 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.bounce_x()
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -400:
        ball.bounce_x()
        ball.reset_position()
        score.r_point()


s.exitonclick()
