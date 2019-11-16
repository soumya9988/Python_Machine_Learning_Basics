import turtle


def draw_square(ref, length_of_sides):
    """
    (turtle reference, int) --> None
    A function that accepts the length of each side and draw the square.

    """

    ref.color('blue')
    for i in range(4):
        ref.forward(length_of_sides)
        ref.left(90)
    ref.right(10)


if __name__ == "__main__":
    scr = turtle.Screen()
    scr.bgcolor('lightgreen')
    turtle_ref = turtle.Turtle()
    size = 100
    for i in range(36):
        draw_square(turtle_ref, size)
    scr.exitonclick()








