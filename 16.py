# Create a class Library with attributes name and books (a list of Book objects). Provide methods to add and remove books.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}',author='{self.author}')"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Add {book} to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed {book} from the library.")
        else:
            print(f"{book} not found in the library.")

    def __repr__(self):
        return f"Library(name='{self.name}', books={self.books})"