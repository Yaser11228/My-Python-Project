# Create a class Zoo with attributes name and animals (a list of Animal objects). Provide methods to add and remove animals.
class Animals:
    def __init__(self, animal):
        self.animal = animal


class Zoo:
    def __init__(self, animal):
        self.animal = animal
        self.animals = []

    def add_animals(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)