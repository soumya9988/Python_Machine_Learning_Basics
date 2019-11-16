import math


def polysum(n, s):
    """
    (int, int) --> float

    A function that accepts the number of sides, n of a regular polygon and the length of side, s
    It calculates the area of regular polygon as: (0.25*n*s^2)/tan(pi/n) and perimeter as  length of the boundary of
    the polygon.

    This function should sum the area and square of the perimeter calculated above and return the sum rounded to
    4 decimal places.


    """
    area_polygon =(0.25 * n * s ** 2) / math.atan(math.pi / n)
    peri_polygon = n * s
    result = area_polygon + (peri_polygon ** 2)
    poly_res = round(result, 4)
    return poly_res


print(polysum(3, 12))
