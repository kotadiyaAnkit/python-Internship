class Shape:
    def area(self):
        print("Total area of the shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * (self.radius ** 2)
        print("Area of a circle is", area)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print("Area of a rectangle is", area)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side ** 2
        print("Area of a square is", area)


# Create objects and call area methods
c = Circle(4)
c.area()

r = Rectangle(5, 6)
r.area()

s = Square(7)
s.area()
