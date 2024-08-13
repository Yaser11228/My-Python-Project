# Create a class Ticket for a movie theater with attributes movie_name, seat_number, and price. Provide methods to display ticket details and apply discounts.
class Ticket:
    def __init__(self, movie, seat, price):
        self.movie = movie
        self.seat = seat
        self.price = price

    def display(self):
        return f"Movie: {self.movie}, seat: {self.seat}, price: {self.price:.2f}"

    def dicount(self, percent):
        self.price *= (1 - percent / 100)