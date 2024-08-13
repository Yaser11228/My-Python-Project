# Create a class Book with private attributes title, author, and pages. Provide public methods to get and set these attributes.
class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_pages(self):
        self.__pages

    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            raise ValueError("Number of pages must be positive.")
