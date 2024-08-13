# Create a class Company with attributes name and employees (a list of Employee objects). Provide methods to add and remove employees.
class Employee:
    def __init__(self, name):
        self.name = name


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employees(self, employee):
        self.employees.append(employee)

    def remove_employees(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)