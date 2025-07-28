from library import Library
from book import Book

# main menu
def display_menu():
    print("-------------\nLMS MAIN MENU \n-------------")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search Books by Title")
    print("4. Search Books by Author")
    print("5. Display All Books")
    print("6. Count All Books")
    print("7. Modify Book Data")
    print("8. Read File")
    print("9. Save and Exit")
    print("0. Exit\n-------------")

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
    print("\nBooks in library:")
    library.book_titles()
    title = input("Enter book title to remove: ")
    library.remove_book(title)

def search_by_title(library):
    title = input("Search Title: ")
    results = library.search_title(title)
    if results:
        print("\nSEARCH RESULTS:")
        for book in results:
            print(book)
    else:
        print("No books found with that title.")

def search_by_author(library):
    author = input("Search Author: ")
    results = library.search_author(author)
    if results:
        print("\nRESULTS:")
        for book in results:
            print(book)
    else:
        print("No books found by that author.")

def modifiy(library):
    print("\nModify Book Data")
    library.modify()

def count_books(library):
    library.book_count()

def read_file_main(library):
    library.read_file("LMS.csv")

def display_all_books(library):
    print("\nInventory: \n-------------")
    library.display_books()

def main():
    library = Library()
    display_menu()

    while True:
        select = input("MAIN SELECT: ")
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
            modifiy(library)
        elif select == "8":
            read_file_main(library)
        elif select == "9":
            library.save_to_file()
            print("TERMINATED.\n")
            break
        elif select == "0":
            break
        else:
            print("Invalid Select")

if __name__ == "__main__":
    main()

