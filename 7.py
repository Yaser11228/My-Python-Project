# Create a base class Shape with a method area. Create derived classes Square and Triangle that implement the area method.
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method.")


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5  * self.base * self.height


square = Square(4)
triangle = Triangle(10, 50)

print("Area of the square:", square.area())
print("Area of the triangle:", triangle.area())
