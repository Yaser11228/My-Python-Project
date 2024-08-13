# Create a class Employee with attributes name and salary. Create a derived class Manager with an additional attribute department.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


employee = Employee("Yaser", 50000)
manager = Manager("Mujtaba", 80000)

print(f"Employee: Name: {employee.name}, salary: {employee.salary}")
print(f"Manager: Name: {manager.name}, Salary: {manager.salary}, Deparment: {manager.department} ")