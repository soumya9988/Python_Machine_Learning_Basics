import turtle
import random

win = turtle.Screen()
tur = turtle.Turtle()
tur.shape('turtle')
tur.color('red')
ttl = turtle.Turtle()
ttl.shape('turtle')
ttl.color('blue')
ttl.setposition(10, 10)


def isInScreen(wind, turt):
    left_width = - (wind.window_width()/2)
    right_width = wind.window_width()/2
    top_height = wind.window_height()/2
    bottom_height = - (wind.window_width()/2)
    tur_xcor = turt.xcor()
    tur_ycor = turt.ycor()
    still_in = True
    if tur_xcor < left_width or tur_xcor > right_width or tur_ycor > top_height or tur_ycor < bottom_height:
        still_in = False
    return still_in


def safe_dist(t1, t2):
    t1x = t1.xcor()
    t2x = t2.xcor()
    t1y = t1.ycor()
    t2y = t2.ycor()
    if t1x - t2x == abs(20) and t1y - t2y == abs(20):
        return False
    else:
        return True


while isInScreen(win, tur) and isInScreen(win, ttl) and safe_dist(tur, ttl):
    coin = random.randint(0,2)
    if coin == 1:
        tur.left(90)
        tur.forward(50)
    else:
        tur.right(90)
        tur.forward(100)

    coin1 = random.randint(0, 2)
    if coin1 == 1:
        ttl.left(90)
        ttl.forward(75)
    else:
        ttl.right(90)
        ttl.forward(175)

win.exitonclick()
