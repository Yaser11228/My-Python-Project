# Create a class Student with private attributes name, grade, and age. Provide methods to get and set these attributes and a method to display the student's details.
class Student:
    def __init__(self, name, grade, age):
        self.__name = name
        self.__grade = grade
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive.")

    def display_details(self):
        return f"Student Details:\nName: {self.__name}\nGrade: {self.__grade}\nAge: {self.__age}."