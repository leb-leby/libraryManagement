import os

class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.books = []

        if os.path.exists(self.file_path):
            self.load_books()
        else:
            with open(self.file_path, "a+") as file:
                file.write("")

    def load_books(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                for line in file:
                    book_info = line.strip().split(',')
                    self.books.append(book_info)

    def save_books(self):
        with open(self.file_path, "w") as file:
            for book_info in self.books:
                file.write(','.join(book_info) + '\n')

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return

        for book_info in self.books:
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = [title, author, release_year, num_pages]
        self.books.append(book_info)
        self.save_books()
        print("Book added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        found = False
        for book_info in self.books:
            if book_info[0] == title_to_remove:
                confirmation = input(f"Are you sure you want to remove the book '{book_info[0]}' by {book_info[1]}? (yes/no): ")
                if confirmation.lower() == 'yes':
                    self.books.remove(book_info)
                    self.save_books()
                    print("Book removed successfully.")
                else:
                    print("Operation canceled.")
                found = True
                break

        if not found:
            print("Book not found.")

    def remove_all_books(self):
        confirmation = input("Are you sure you want to remove all books and the file? (yes/no): ")
        if confirmation.lower() == 'yes':
            self.books = []
            self.save_books()
            os.remove(self.file_path)
            print("All books and the file removed successfully.")
        else:
            print("Operation canceled.")

def main():
    lib = Library()

    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Remove All Books")
        print("5) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "4":
            lib.remove_all_books()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
