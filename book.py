from datetime import datetime

# this file holds physical (p) or digital (d) book information
# class attrs: title. author, ISBN, publication year, genre, format (p/d), storage location

from datetime import datetime

class Book:
    def __init__(self, title, author, isbn, publication_year, genre, format, storage_loc):
        # Validate and assign attributes
        self.set_title(title)
        self.set_author(author)
        self.set_isbn(isbn)
        self.set_publication_year(publication_year)
        self.set_genre(genre)
        self.set_format(format)
        self.set_storage_loc(storage_loc)

    # title
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if not title or not isinstance(title, str):
            raise ValueError("Title can't be empty.")
        self._title = title

    # author
    def get_author(self):
        return self._author
    
    def set_author(self, author):
        if not author or not isinstance(author, str):
            raise ValueError("Author must be a non-empty string.")
        self._author = author

    # isbn
    def get_isbn(self):
        return self._isbn
    
    def set_isbn(self, isbn):
        if not isinstance(isbn, str) or not isbn.replace("-", "").isdigit() or not (10 <= len(isbn.replace("-", "")) <= 13):
            raise ValueError("ISBN must be a string of 10 to 13 digits.")
        self._isbn = isbn

    # publication year
    def get_publication_year(self):
        return self._publication_year
    
    def set_publication_year(self, publication_year):
        current_year = datetime.now().year
        if not isinstance(publication_year, int) or not (1000 <= publication_year <= current_year):
            raise ValueError(f"Publication year must be between 1000 and {current_year}.")
        self._publication_year = publication_year

    # genre
    def get_genre(self):
        return self._genre
    
    def set_genre(self, genre):
        if not genre or not isinstance(genre, str):
            raise ValueError("Genre must be a non-empty string.")
        self._genre = genre

    # format
    def get_format(self):
        return self._format
    
    def set_format(self, format):
        if format not in ('p', 'd'):
            raise ValueError("Format must be 'p' (physical) or 'd' (digital).")
        self._format = format

    # storage location
    def get_storage_loc(self):
        return self._storage_loc
    
    def set_storage_loc(self, storage_loc):
        if not storage_loc or not isinstance(storage_loc, str):
            raise ValueError("Storage location must be a non-empty string.")
        self._storage_loc = storage_loc

    # display book information
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
