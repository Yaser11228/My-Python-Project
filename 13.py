# Create a class Laptop with private attributes brand, model, and price. Provide a method to apply a discount and a method to display laptop details.
class Laptop:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def apply_discount(self, dicount_percentage):
        if 0 <= dicount_percentage <= 100:
            dicount_percentage = (dicount_percentage / 100) * self.__price
            self.__price -= dicount_percentage
            return f"Discount of {dicount_percentage}% applied. New price is {self.__price:.2f}"
        else:
            return "Discount percentage must be between 0 and 100."

    def display_details(self):
        return f"Laptop Details:\nBrand: {self.__brand}\nModel: {self.__model}\nPrice: {self.__price:.2f}."
