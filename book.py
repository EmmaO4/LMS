# this file holds physical (p) or digital (d) book information
# class attrs: title. author, ISBN, publication year, genre, format (p/d), storage location

class Book:
    # book information here
    def __init__(self, title, author, isbn, publication_year, genre, format, storage_loc):
        # Initialize all attributes here
        self._title               = title
        self._author              = author
        self._isbn                = isbn
        self._publication_year    = publication_year
        self._genre               = genre
        self._format              = format
        self._storage_loc         = storage_loc
    
    # title
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        self._title = title

    # author
    def get_author(self):
        return self._author
    
    def set_author(self, author):
        self._author = author

    # isbn
    def get_isbn(self):
        return self._isbn
    
    def set_isbn(self, isbn):
        self._isbn = isbn

    # publication year
    def get_publication_year(self):
        return self._publication_year
    
    def set_publication_year(self, publication_year):
        self._publication_year = publication_year

    # genre
    def get_genre(self):
        return self._genre
    
    def set_genre(self, genre):
        self._genre = genre

    # format
    def get_format(self):
        return self._format
    
    def set_format(self, format):
        self._format = format

    # storage location
    def get_storage_loc(self):
        return self._storage_loc
    
    def set_storage_loc(self, storage_loc):
        self._storage_loc = storage_loc

    # display book information
    # R
    def __str__(self):
        return (
            f"Title: {self.get_title()}\n"
            f"Author: {self.get_author()}\n"
            f"ISBN: {self.get_isbn()}\n"
            f"Publication Year: {self.get_publication_year()}\n"
            f"Genre: {self.get_genre()}\n"
            f"Format: {self.get_format()}\n"
            f"Storage Location: {self.get_storage_loc()}"
        )
