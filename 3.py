# Create a class called Car with attributes make, model, and year. Include a method to print out the car's details.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_details(self):
        print(f"Car Details: {self.year} {self.model} {self.make}")


car1 = Car("Toyota", "Camry", 2021)
car1.print_details()