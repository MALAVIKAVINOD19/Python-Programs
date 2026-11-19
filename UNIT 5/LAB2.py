class Library:
    def __init__(self):
        self.books = ["Python", "Java", "C++", "Data Structures"]

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"You have borrowed '{book}'")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print(f"You have returned '{book}'")


# Create Library Object
library = Library()

# Display available books
library.display_books()

# Borrow a book
book = input("\nEnter book name to borrow: ")
library.borrow_book(book)

# Display updated list
library.display_books()

# Return a book
book = input("\nEnter book name to return: ")
library.return_book(book)

# Display final list
library.display_books()