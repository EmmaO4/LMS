# this file stores book info into a txt file using lists
from book import Book

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

    # learn 
    def search_title(self, title):
        return [book for book in self.shelf if title.lower() in book.get_title().lower()]
    
    def search_author(self, author):
        return [book for book in self.shelf if author.lower() in book.get_author().lower()]

    #R
    # reads up-to-date library data contents before having to save
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

    # read file as is, will be outdated when modifying library
    def read_file(self, filename):
        with open(filename, "r") as file:
            print("\n" + file.read())

    def book_titles(self):
        for book in self.shelf:
            print(book.get_title())

    #R
    # loads in all books and prints them to output for viewing
    def load_data(self, filename="LMS.txt"):
        try:
            with open(filename, "r") as file:
                content = file.read().strip()
                content = content.replace("\r\n", "\n").replace("\r", "\n")

                if not content:
                    print("DEBUG: LMS.txt is empty.")
                    return

                book_entries = content.split("\n\n")
                print(f"DEBUG: Found {len(book_entries)} entries in LMS.txt")

                for entry in book_entries:
                    if not entry.strip():
                        continue

                    book_attrs = {
                        'title': None,
                        'author': None,
                        'isbn': None,
                        'publication_year': None,
                        'genre': None,
                        'format': None,
                        'storage_loc': None
                    }

                    print(f"\nAuto Entry:\n{entry}")

                    for line in entry.split("\n"):
                        if ": " in line:
                            key, value = line.split(": ", 1)
                            key = key.lower().replace(" ", "_")
                            # Normalize alternate field names
                            key_aliases = {
                                "storage_location": "storage_loc"
                            }
                            key = key_aliases.get(key, key)  # remap if alias exists
                            if key in book_attrs:
                                if key == "publication_year":
                                    try:
                                        value = int(value)
                                    except ValueError:
                                        value = None
                                book_attrs[key] = value

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
                        print(f"DEBUG: Loaded book: {book.get_title()} by {book.get_author()}")
                    else:
                        print(f"WARNING: Skipped book due to missing data: {book_attrs}")

                print(f"\nSuccessfully loaded {len(self.shelf)} books from {filename}")

        except FileNotFoundError:
            print(f"WARNING: {filename} not found. Starting with an empty library.")
        except Exception as e:
            print(f"ERROR loading books: {str(e)}")
