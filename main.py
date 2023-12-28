import turtle as tur
import pong
from ball import Ball
import time
from score import Score

screen = tur.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = pong.Paddle((370, 0))
l_paddle = pong.Paddle((-370, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh()
    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 430:
        ball.reset_position()
        score.l_point()

    # Detect L paddle misses
    if ball.xcor() < -430:
        ball.reset_position()
        score.r_point()

    if score.l_score == 5 or score.r_score == 5:
        game_on = False
        score.game_over()








screen.exitonclick()