# Create a class Flight with attributes flight_number, destination, and passengers (a list of Person objects). Provide methods to add and remove passengers.
class Person:
    def __init__(self, name):
        self.name = name


class Flight:
    def __init__(self, flight_number, destination):
        self.flight_number = flight_number
        self.destination = destination
        self.passengers = []

    def add_passengers(self, person):
        self.passengers.append(person)

    def remove_passengers(self, person):
        self.passengers.remove(person)