# Create a class Restaurant with attributes name and menu (a list of Item objects). Provide methods to add and remove items from the menu.
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_item(self, item):
        self.menu.append(item)

    def remove_item(self, item):
        self.menu.remove(item)