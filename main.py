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
    print("0. Exit\n-------------")

def add_book(library):
    # helper function to determine curr user input to cancel add book operation early
    def sub_select(select):
        value = input(f"{select}: ")
        if value == "0":
            print("Book entry cancelled.")
            return None
        else:
            return value
        
    print("\nAdd a Book\n(0. Cancel)")
    title = sub_select("Title")

    if title is None: 
        return
    author = sub_select("Author")
    if author is None: 
        return
    isbn = sub_select("ISBN")
    if isbn is None: 
        return
    pub_year = sub_select("Publication Year")
    if pub_year is None: 
        return
    try:
        publication_year = int(pub_year)
    except ValueError:
        print("Invalid year. Entry cancelled.")
        return
    genre = sub_select("Genre")
    if genre is None: 
        return
    format = sub_select("Format (p/d)")
    if format is None: 
        return
    storage_loc = sub_select("Storage Location")
    if storage_loc is None: 
        return
    
    book = Book(title, author, isbn, publication_year, genre, format, storage_loc)
    library.add_book(book)
    print(f"'{title}' has been added.")

def remove_book(library):
    # helper method to quit function mid-action
    def sub_select(select): 
        value = input(f"{select}")
        if value == "0":
            print("Remove book cancelled.")
            return None
        else:
            return value
    print("Remove Book\n(0. Cancel)")
    print("\nBooks in library:")
    library.book_titles()
    title = sub_select("Enter book title to remove: ")
    if title == None:
        return
    library.remove_book(title)

def search_by_title(library):
    title = input("Search Title: ")
    results = library.search_title(title)
    if results:
        print("\nSEARCH RESULTS:\n")
        for book in results:
            print(book, "\n")
    else:
        print("No books found with that title.")

def search_by_author(library):
    author = input("Search Author: ")
    results = library.search_author(author)
    if results:
        print("\nSEARCH RESULTS:\n")
        for book in results:
            print(book, "\n")
    else:
        print("No books found by that author.")

def modify(library):
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
            modify(library)
        elif select == "8":
            read_file_main(library)
        elif select == "0":
            print("TERMINATED.\n")
            break
        else:
            print("Invalid Select")

if __name__ == "__main__":
    main()

