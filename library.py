# this file stores book info into a csv file using lists
from book import Book
import csv

class Library:

    def __init__(self):
        self.shelf = []
        self.load_data()

    def add_book(self, book):
        self.shelf.append(book)

    def remove_book(self, title):
        for book in self.shelf:
            if book.get_title() == title:
                self.shelf.remove(book)
                print(f"'{book.get_title()}' by {book.get_author()} has been removed from library.")
                return
        print(f"Book with title: {title} was not found.")

    def search_title(self, title):
        return [book for book in self.shelf if title.lower() in book.get_title().lower()]
    
    def search_author(self, author):
        return [book for book in self.shelf if author.lower() in book.get_author().lower()]

    def display_books(self, filename="LMS.csv"):
        for i, book in enumerate(self.shelf, 1):
            print(f"\nBook #{i}")
            print(book)
            print("-" * 30)

    def save_to_file(self, filename="LMS.csv"):
        with open(filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Author", "ISBN", "Publication Year", "Genre", "Format", "Storage Location"])
            for book in self.shelf:
                writer.writerow([
                    book.get_title(),
                    book.get_author(),
                    book.get_isbn(),
                    book.get_publication_year(),
                    book.get_genre(),
                    book.get_format(),
                    book.get_storage_loc()
                ])
        print(f"Library data saved to {filename}.")

    def book_count(self):
        count = len(self.shelf)
        print(f"Number of books in library: {count}")

    def read_file(self, filename="LMS.csv"):
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(', '.join(row))
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def book_titles(self):
        for book in self.shelf:
            print(book.get_title())

    def load_data(self, filename="LMS.csv"):
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    book = Book(
                        title=row["Title"],
                        author=row["Author"],
                        isbn=row["ISBN"],
                        publication_year=int(row["Publication Year"]),
                        genre=row["Genre"],
                        format=row["Format"],
                        storage_loc=row["Storage Location"]
                    )
                    self.shelf.append(book)
            print(f"Successfully loaded {len(self.shelf)} books from {filename}.")
        except FileNotFoundError:
            print(f"WARNING: {filename} not found. Starting with an empty library.")
        except Exception as e:
            print(f"ERROR loading books: {str(e)}")
