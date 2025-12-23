from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()


screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed  )
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor()>320:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.refresh()
        score.inc_l_score()

    if ball.xcor()<-380:
        ball.refresh()
        score.inc_r_score()


screen.exitonclick()
