# Create a class Circle with a method to compute the area. Initialize the class with the radius.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius ** 2

circle = Circle(5)
print("Area the circle: ", circle.compute_area())