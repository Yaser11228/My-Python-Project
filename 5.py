# Create a class Rectangle with methods to compute the area and perimeter. Initialize the class with the length and width.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.width * self.length

    def compute_perimeter(self):
        return 2 * (self.length * self.width)


rectangle = Rectangle(10, 20)
print("Area of the rectangle: ", rectangle.compute_area())
print("Perimeter of the rectangle: ", rectangle.compute_perimeter())