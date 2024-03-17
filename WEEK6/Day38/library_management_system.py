#Simple library Management System
class Book:
    def __init__(self,title,author,status):
        self.title = title
        self.author = author
        self.status = status
    def lend(self):
        if self.status == "available":
            self.status = "unavailable"
            print("The book has been lended")
        else:
            print("The book is currently unavailable")
    def return_book(self):
        if self.status == "unavailable":
            self.status = "available"
            print("The book has been returned")
        else:
            print("The book is currently available")

class Library:
    books = []
    def add_book(self,book):
        self.books.append(book)
        print("Book has been added to the library")
    def display_books(self):
        for book in self.books:
            print(book.title)
    def lend_book(self,title):
        for book in self.books:
            if book.title == title:
                book.lend()
    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                book.return_book()
    def available_books(self):
        for book in self.books:
            if book.status == "available":
                print(book.title)

def main():
    print("---Welcome to the library---")
    library = Library()
    while True:
        print("1. Add book")
        print("2. Display books")
        print("3. Lend book")
        print("4. Return book")
        print("5. Available books")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            status = input("Enter the status of the book: ")
            book = Book(title,author,status)
            library.add_book(book)
        elif choice == 2:
            library.display_books()
        elif choice == 3:
            title = input("Enter the title of the book: ")
            library.lend_book(title)
        elif choice == 4:
            title = input("Enter the title of the book: ")
            library.return_book(title)
        elif choice == 5:
            library.available_books()
        elif choice == 6:
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()