from math import sqrt


class Point:
    def __init__(self, p_x, p_y):
        self.p_x = p_x
        self.p_y = p_y

    def get_x(self):
        return self.p_x

    def get_y(self):
        return self.p_y

    def __str__(self):
        return 'Point(' + str(self.p_x) + ", " + str(self.p_y) + ')'


class Rectangle:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def __str__(self):
        return  'The rectangle can be represented as: ' + str(self.l) + ', ' + str(self.w) + ', ' + str(self.h)

    def get_width(self):
        return self.w

    def get_height(self):
        return self.h

    def get_area(self):
        return self.h * self.w

    def get_perimeter(self):
        return 0.5 * (self.h + self.w)

    def transpose(self):
        old_ht = self.h
        self.h = self.w
        self.w = old_ht
        return self  # Rectangle(self.l, self.w, self.h)

    def get_diagonal(self):
        return sqrt((self.h ** 2) + (self.w ** 2)) * 0.5

loc = Point(3,4)
rect = Rectangle(loc, 6, 10)
print(rect)
print('Area of the triangle is:', rect.get_area())
print('Perimeter of the triangle is', rect.get_perimeter())
print('Length of the diagonal is:', rect.get_diagonal())
print(rect.transpose())