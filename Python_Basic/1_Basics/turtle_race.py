import turtle


def draw_shapes(ref, no_of_sides, length_of_sides):
    """
    (int, int) --> None
    A function that accepts the no of sides of a  regular polygon and the length of each side and draw the polygon.

    """
    angle = 360 / no_of_sides   # Angle of the polygon.
    ref.color('green')
    ref.fillcolor('red')
    ref.begin_fill()
    for i in range(no_of_sides):
        ref.forward(length_of_sides)
        ref.left(angle)
    ref.end_fill()


if __name__ == "__main__":
    scr = turtle.Screen()
    turtle_ref = turtle.Turtle()
    draw_shapes(turtle_ref, 3, 120)
    turtle_ref.penup()
    turtle_ref.goto(100,100)
    turtle_ref.pendown()
    draw_shapes(turtle_ref, 4, 120)
    turtle_ref.penup()
    turtle_ref.goto(-100,-100)
    turtle_ref.pendown()
    draw_shapes(turtle_ref, 6, 70)
    turtle_ref.penup()
    turtle_ref.goto(-100,100)
    turtle_ref.pendown()
    draw_shapes(turtle_ref, 8, 70)
    turtle_ref.penup()
    turtle_ref.goto(50,-250)
    turtle_ref.pendown()
    draw_shapes(turtle_ref, 20, 20)
    scr.exitonclick()






