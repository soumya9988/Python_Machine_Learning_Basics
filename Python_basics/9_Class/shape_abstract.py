from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):
    @abstractmethod
    def area_cal(self):
        pass

    @abstractmethod
    def perimeter_cal(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.r = radius

    @property
    def radius(self):
        return self.r

    @property
    def area_cal(self):
        return pi * self.r * self.r

    @property
    def perimeter_cal(self):
        return 2 * pi * self.r


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    @property
    def area_cal(self):
        return self.l * self.b

    @property
    def perimeter_cal(self):
        return 2 * (self.l + self.b)


x = Circle(2)
cir_area = x.area_cal
print("Area of the circle is %.2f" % cir_area)
y = Rectangle(3, 5)
peri_rect = y.perimeter_cal
print('Perimeter of the rectangle is %.2f' % peri_rect)






