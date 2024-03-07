# Information about the library
library_name = "Pythonic Library"
library_location = "Cityville"

# List of books available in the library
books = [
    {"title": "Introduction to Python", "author": "John Python", "genre": "Programming"},
    {"title": "Python for Beginners", "author": "Alice Coder", "genre": "Programming"},
    {"title": "Mystery of Pythonic Code", "author": "Sherlock Hacker", "genre": "Mystery"}
]

# Dictionary representing the library staff
library_staff = {
    "librarian": {"name": "Eva Librarian", "age": 35, "role": "Librarian"},
    "assistant": {"name": "Alex Assistant", "age": 28, "role": "Assistant Librarian"},
}

def print_staff_info(staff):
    print("Name:", staff["name"])
    print("Age:", staff["age"])
    print("Role:", staff["role"])

genre_list = []
for book in books:
    genre_list.append(book["genre"])

print("Welcome to", library_name)
genre = input("Enter the genre of the book you are looking for: ")
if genre in genre_list:
    if genre =="Programming":
        print("Hello Programming enthusiast!")
    print("Here are the books available in the", genre, "genre:")
    for book in books:
        if book["genre"] == genre:
            print(book["title"], "by", book["author"])
else:
    print("Sorry, no books available in the", genre, "genre.")

print("Here is the information about the library staff:")
print_staff_info(library_staff["librarian"])
print_staff_info(library_staff["assistant"])