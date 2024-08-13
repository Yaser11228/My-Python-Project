# Create a class Team with attributes name and members (a list of Person objects). Provide methods to add and remove members.
class Person:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_members(self, member):
        self.members.append(member)

    def remove_members(self, member):
        if member in self.members:
            self.members.remove(member)
