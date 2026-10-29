import json
import os

FILE_NAME = "library.txt"


# Load books from file
def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            
            except json.JSONDecodeError:
                return []
    return []


# Save books to file
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


# Generate book ID
def generate_id(books):
    number = 100

    for book in books:
        book_number = int(book["id"][1:])
        if book_number > number:
            number = book_number

    return "B" + str(number + 1)


# Add a book
def add_book(books):
    title = input("Title: ").strip()
    author = input("Author: ").strip()

    if title == "" or author == "":
        print("Title and author cannot be empty.")
        return

    book = {
        "id": generate_id(books),
        "title": title,
        "author": author,
        "status": "Available",
        "member": ""
    }

    books.append(book)
    save_books(books)

    print("Book added. ID:", book["id"], "|",
          book["title"], "|", book["author"], "| Available")


# Issue a book
def issue_book(books):
    book_id = input("Book ID: ").strip().upper()

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Issued":
                print("Book is already issued.")
                return

            member = input("Member name: ").strip()

            if member == "":
                print("Member name cannot be empty.")
                return

            book["status"] = "Issued"
            book["member"] = member
            save_books(books)

            print("Book", book_id, "issued to", member,
                  ". Status: Issued")
            print("Available books:", count_available(books))
            return

    print("Book ID", book_id, "not found.")


# Return a book
def return_book(books):
    book_id = input("Book ID: ").strip().upper()

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Available":
                print("Book is already available.")
                return

            book["status"] = "Available"
            book["member"] = ""
            save_books(books)

            print("Book", book_id,
                  "returned. Status: Available")
            return

    print("Book ID", book_id, "not found.")


# Search by title or author
def search_book(books):
    print("1. Search by title")
    print("2. Search by author")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        field = "title"
    elif choice == "2":
        field = "author"
    else:
        print("Invalid search option.")
        return

    text = input("Enter search text: ").strip().lower()

    if text == "":
        print("Search text cannot be empty.")
        return

    found = False

    for book in books:
        if text in book[field].lower():
            print(book["id"], "|", book["title"], "|",
                  book["author"], "|", book["status"])
            found = True

    if not found:
        print("No matching books found.")


# Count available books
def count_available(books):
    count = 0

    for book in books:
        if book["status"] == "Available":
            count += 1

    return count


# Display all books
def display_books(books):
    if len(books) == 0:
        print("No books in the library.")
        return

    for book in books:
        print(book["id"], "|", book["title"], "|",
              book["author"], "|", book["status"])

    print("Available books:", count_available(books))


# Main menu
def main():
    books = load_books()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add book")
        print("2. Issue book")
        print("3. Return book")
        print("4. Search book")
        print("5. Display all books")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            issue_book(books)
        elif choice == "3":
            return_book(books)
        elif choice == "4":
            search_book(books)
        elif choice == "5":
            display_books(books)
        elif choice == "6":
            save_books(books)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option. Enter 1 to 6.")


main()