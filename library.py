# this file stores book info into a txt file using lists
from book import Book

class Library:

    def __init__(self):
        self.shelf = []
        self.load_data()

    def add_book(self, book):
        self.shelf.append(book)

    def remove_book(self, isbn):
        for book in self.shelf:
            if book.get_isbn() == isbn:
                self.shelf.remove(book)
                print(f"'{book.get_title()}' by {book.get_author()} has been removed from library.")
                return
        print(f"Book with ISBN: {isbn} was not found.")

    # learn return line
    def search_title(self, title):
        return [book for book in self.shelf if title.lower() in book.get_title().lower()]
    
    def search_author(self, author):
        pass

    #R1
    def display_books(self, filename = "LMS.txt"):
        for i, book in enumerate(self.shelf, 1):
            print(f"\nBook #{i}")
            print(book)
            print("-" * 30)

    def save_to_file(self, filename = "LMS.txt"):
        with open(filename, "w") as file:
            for book in self.shelf:
                file.write(str(book) + "\n\n")  # Write each book's details to the file
        print(f"Library data saved to {filename}.")

    def book_count(self, book):
        count = len(self.shelf)
        print(f"Number of books in library: {count}")

    def read_file(self, filename):
        with open(filename, "r") as file:
            print("\n" + file.read())

    #R1: WTF is this 
    def load_data(self, filename="LMS.txt"):
        try:
            with open(filename, "r") as file:
                content = file.read().strip()
                if not content:
                    return
                
                book_entries = content.split("\n\n")
                
                for entry in book_entries:
                    if not entry.strip():
                        continue
                    
                    # Initialize book attributes with None
                    book_attrs = {
                        'title': None,
                        'author': None,
                        'isbn': None,
                        'publication_year': None,
                        'genre': None,
                        'format': None,
                        'storage_loc': None
                    }
                    
                    # Parse each line of the book entry
                    for line in entry.split("\n"):
                        if ": " in line:
                            key, value = line.split(": ", 1)
                            key = key.lower().replace(" ", "_")
                            if key in book_attrs:
                                # Special handling for publication year (convert to int)
                                if key == "publication_year":
                                    try:
                                        value = int(value)
                                    except ValueError:
                                        value = None
                                book_attrs[key] = value
                    
                    # Check if all required attributes were found
                    if all(book_attrs.values()):
                        book = Book(
                            title=book_attrs['title'],
                            author=book_attrs['author'],
                            isbn=book_attrs['isbn'],
                            publication_year=book_attrs['publication_year'],
                            genre=book_attrs['genre'],
                            format=book_attrs['format'],
                            storage_loc=book_attrs['storage_loc']
                        )
                        self.shelf.append(book)
                    else:
                        continue
                        #print(f"Skipping incomplete book entry: {entry[:50]}...")
            
            print(f"Successfully loaded {len(self.shelf)} books from {filename}")
        except FileNotFoundError:
            print(f"Warning: {filename} not found. Starting with empty library.")
        except Exception as e:
            print(f"Error loading books from {filename}: {str(e)}")