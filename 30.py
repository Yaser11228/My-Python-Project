# Create a class Hotel with attributes name and rooms (a list of Room objects). Each Room should have attributes room_number and is_occupied. Provide methods to book and check-out rooms.
class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_occupied = False


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def book_room(self, room):
        if not room.is_occupied:
            room.is_occupied = True

    def checkout_room(self, room):
        if room.is_occupied:
            room.is_occupied = False