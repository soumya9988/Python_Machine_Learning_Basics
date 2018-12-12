class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r

    def __str__(self):
        return 'Circle of radius: ' + str(self.r)

c1 = Circle(8)
print(c1)
print('Area of c1 is ', c1.area())
print('Perimeter of c1 is ', c1.perimeter())
