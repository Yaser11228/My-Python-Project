# Create a base class Animal with a method speak. Create two derived classes Dog and Cat that override the speak method.
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method.")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print("Dog Says:", dog.speak())
print("Cat Says:", cat.speak())