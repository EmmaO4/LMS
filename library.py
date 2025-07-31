# this file stores book info into a csv file using lists
# book logic
from book import Book
from csv_to_db import migrate_csv_to_db
import csv

class Library:
    
    def __init__(self):
        self.shelf = []
        self.load_data()    # auto run when called by constructor in main.py

    def add_book(self, book):
        self.shelf.append(book)
        self.save_to_file()
        migrate_csv_to_db()

    def remove_book(self, title):
        for book in self.shelf:
            if book.get_title().lower() == title.lower():
                self.shelf.remove(book)
                print(f"'{book.get_title()}' by {book.get_author()} has been removed from library.")
#                return
        print(f"Book with title: {title} was not found.")
        self.save_to_file()

    # returns comprehension of title after being set to lowercase
    def search_title(self, title):
        return [book for book in self.shelf if title.lower() in book.get_title().lower()]
    
    # return comprhension of author after being set to lowercase (same as above)
    def search_author(self, author):
        return [book for book in self.shelf if author.lower() in book.get_author().lower()]

    # reads books from library for debugging
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
                format_display = "Physical" if book.get_format() in ("p", "physical") else "Digital"
            
                storage_display = {
                    "s1": "Shelf 1",
                    "s2": "Shelf 2"
                }.get(book.get_storage_loc().lower(), book.get_storage_loc())
                
                writer.writerow([
                    book.get_title(),
                    book.get_author(),
                    book.get_isbn(),
                    book.get_publication_year(),
                    book.get_genre(),
                    format_display,
                    storage_display
                ])
        print(f"Library data saved to {filename}.")

    def modify(self, filename="LMS.csv"):
        book_to_modify = input("Title of book: ")
        for book in self.shelf:
            if book.get_title().lower() == book_to_modify.lower():
                print(f"{book.get_title()} by {book.get_author()}")
                
                attributes = {
                    "title" : book.set_title,
                    "author" : book.set_author,
                    "isbn" : book.set_isbn,
                    "publication_year" : book.set_publication_year,
                    "genre" : book.set_genre,
                    "format" : book.set_format,
                    "storage_loc" : book.set_storage_loc
                }

                print("Attributes you can modify:", ", ".join(attributes.keys()))
                attr = input("Attr to modify: ")

                # not necessary if user inputs exact key syntax
                if attr == "year":
                    attr = "publication_year"
                elif attr == "storage":
                    attr = "storage_loc"

                if attr in attributes:
                    mod_attr_val = input("New attr value: ")
        
                    if attr == "publication_year":
                        try:
                            mod_attr_val = int(mod_attr_val)
                        except ValueError:
                            print("invalid. year must be type int")
                        
                    attributes[attr](mod_attr_val)
                    print(f"{attr} updated to: {mod_attr_val}")
                    self.save_to_file(filename)
                    return
                else:
                    print("Invalid attribute name.")
                    return

        print(f"No book found with title: {book_to_modify}")

    # reads count of library for debugging
    def book_count(self):
        count = len(self.shelf)
        print(f"Number of books in library: {count}")

    # reads the file as is for debugging
    def read_file(self, filename="LMS.csv"):
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(', '.join(row))
        except FileNotFoundError:
            print(f"File {filename} not found.")

    # print all stored books by titles
    def book_titles(self):
        for book in self.shelf:
            print(book.get_title())

    def load_data(self, filename="LMS.csv"):
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    book = Book(
                        title = row["Title"],
                        author = row["Author"],
                        isbn = row["ISBN"],
                        publication_year = int(row["Publication Year"]),
                        genre = row["Genre"],
                        format = row["Format"],
                        storage_loc = row["Storage Location"]
                    )
                    self.shelf.append(book)
            print(f"Successfully loaded {len(self.shelf)} books from {filename}.")
        except FileNotFoundError:
            print(f"WARNING: {filename} not found. Starting with an empty library.")
        except Exception as e:
            print(f"ERROR loading books: {str(e)}")
