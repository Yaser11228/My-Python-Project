# Add a method called greet to the Person class that prints a greeting message including the person's name.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")



person1 = Person("Yaser", 20)
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
person1.greet()