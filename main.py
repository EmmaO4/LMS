from library import Library
from book import Book

def display_menu():
    print("-------------\nLMS MAIN MENU \n-------------")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search Books by Title")
    print("4. Search Books by Author")
    print("5. Display All Books")
    print("6. Count all Books")
    print("7. Read File")
    print("8. Save and Exit\n-------------")

def add_book(library):
    print("\nAdd a Book")
    title               = input("Title: ")
    author              = input("Author: ")
    isbn                = input("ISBN: ")
    publication_year    = int(input("Publication year: "))
    genre               = input("Genre: ")
    format              = input("Format (p/d): ")
    storage_loc         = input("Storage location: ")

    book = Book(title, author, isbn, publication_year, genre, format, storage_loc)
    library.add_book(book)
    print(f"'{title}' has been added.")

def remove_book(library):
    print("\nRemove a Book")
    isbn                = input("Enter the ISBN of the book to remove: ")
    library.remove_book(isbn)

def search_by_title(library):
    print("\nSearch Title")
    title               = input("Search title: ")
    results             = library.search_by_title(title)
    if results:
        print("\nSearch Results:")
        for book in results:
            print(book)
    else:
        print("No books found with that title.")

def search_by_author(library):
    print("\nSearch by author")
    author              = input("Enter the author to search: ")
    results             = library.search_by_author(author)
    if results:
        print("\nResults:")
        for book in results:
            print(book)
    else:
        print("No books found by that author.")

def count_books(library):
    num_of_books        = library.book_count(Book)
    
def read_file_main(library):
    library.read_file("LMS.txt")

def display_all_books(library):
    print("\nInventory: \n-------------")
    library.display_books()


def main():
    library = Library()  # Create a library instance

    #book1 = Book("1984", "George Orwell", "978-0451524935", 1949, "Dystopian", "p", "S1")
    #library.add_book(book1)

    display_menu()

    while True:
        
        select = input("Select: ")

        if select == "1":
            add_book(library)
        elif select == "2":
            remove_book(library)
        elif select == "3":
            search_by_title(library)
        elif select == "4":
            search_by_author(library)
        elif select == "5":
            display_all_books(library)
        elif select == "6":
            count_books(library)
        elif select == "7":
            read_file_main(library)
        elif select == "8":
            library.save_to_file()
            print("TERMINATED.\n")
            break
        else:
            print("Invalid select")

if __name__ == "__main__":
    main()
