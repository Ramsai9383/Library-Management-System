class Book:
    def _init_(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

class Member:
    def _init_(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []
        self.is_subscribed = False

    def subscribe(self):
        self.is_subscribed = True
        return f"{self.name} has subscribed."

    def borrow_book(self, book):
        if self.is_subscribed:
            if book.available:
                self.books_borrowed.append(book)
                book.available = False
                return f"{self.name} borrowed '{book.title}'."
            else:
                return f"Sorry, '{book.title}' is not available for borrowing."
        else:
            return f"{self.name} is not subscribed. Please subscribe to borrow books."

    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.available = True
            return f"{self.name} returned '{book.title}'."
        else:
            return f"Error: '{book.title}' not found in the list of borrowed books for {self.name}."

class Library:
    def _init_(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

# Example Usage:
book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")

member1 = Member(101, "Alice")
member2 = Member(102, "Bob")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.add_member(member2)

print(member1.subscribe())  # Output: "Alice has subscribed."

print(member1.borrow_book(book1))  # Output: "Alice borrowed 'The Great Gatsby'."
print(member2.borrow_book(book2))  # Output: "Bob is not subscribed. Please subscribe to borrow books."
