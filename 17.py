# Create a class School with attributes name and students (a list of Student objects). Provide methods to add and remove students.
class Student:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

