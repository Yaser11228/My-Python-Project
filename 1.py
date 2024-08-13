# Create a class called Person with attributes name and age. Create an object of the class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Yaser", 20)
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")