from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        message = 'x coordinate and y coordinate of the point is (' + str(self.x) + ', ' + str(self.y) + ')'
        return message

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def get_dist_from_center(self):
        return sqrt((self.x ** 2) + (self.y ** 2))

    def get_midway_of_points(self, dest):
        mid_x = (self.x + dest.x)/2
        mid_y = (self.y + dest.y)/2
        return mid_x, mid_y

    def get_dist_btwn_pt(self,target):
        x_diff = target.x - self.x
        y_diff = target.y - self.y
        return sqrt((x_diff ** 2) + (y_diff ** 2))

    def slope_from_origin(self):
        if self.x == 0:
            return 0
        else:
            return self.y / self.x

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


def distance(p1, p2):
    xdiff = p2.getX() - p1.getX()
    ydiff = p2.getY() - p1.getY()
    return sqrt((xdiff ** 2) + (ydiff ** 2) )


if __name__ == '__main__':
    p = Point(10, 7)
    # Printing the object
    print(p)
    # methods in class
    print('Distance of p from center is:', p.get_dist_from_center())
    p1 = Point(3,4)
    p2 = Point(7,10)
    # Passing the object as argument to a function
    print('Distance btwn points using method is', distance(p1, p2))
    # Instance as return value
    mid = p1.get_midway_of_points(p2)
    print('Mid point between the two point is:', mid)

    dist = p1.get_dist_btwn_pt(p2)
    print('The distance between the point is:', dist)

    slope = p.slope_from_origin()
    print('Slope of p from origin is', slope)

    p.move(3,3)
    print(p)


