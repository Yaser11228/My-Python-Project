# Create a base class Vehicle with a method drive. Create derived classes Bike and Truck that override the drive method.
class Vehicle:
    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Bike(Vehicle):
    def drive(self):
        return "Riding the bike"

class Truck(Vehicle):
    def __del__(self):
        return "Driving the truck!"


bike = Bike()
truck = Truck

print("Bike:", bike.drive())
print("Truck:", truck.drive())