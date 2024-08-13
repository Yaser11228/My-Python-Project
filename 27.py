# Create a class ShoppingCart with methods to add, remove, and display items. Each item should be an object of a class Item with attributes name and price.
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display_item(self):
        return [f"{item.name}: ${item.price:.2f}" for item in self.items]
