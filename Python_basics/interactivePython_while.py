import turtle
import random

win = turtle.Screen()
tur = turtle.Turtle()
tur.shape('turtle')


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


while isInScreen(win, tur):
    coin = random.randint(0,2)
    if coin == 1:
        tur.left(90)
        tur.stamp()
        tur.forward(100)
    else:
        tur.right(90)
        tur.stamp()
        tur.forward(100)

win.exitonclick()

