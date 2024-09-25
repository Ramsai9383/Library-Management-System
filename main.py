class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
   
    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Available Books")
        for book in self.books:
            print(book)

class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed_books = []

    def __str__(self):
        return ("BookId:",self.book_id,"Title:",self.title,"Author:",self.author, "Available Copies:", self.copies)

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            self.borrowed_books.append(self)
            return True
        else:
            print("The book is not available in the library.")
            return False

    def return_book(self):
        if self in self.borrowed_books:
            self.copies += 1
            self.borrowed_books.remove(self)
            print("Book return was successful.")
        else:
            print("The book is not borrowed")

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []
        self.members = []
        self.is_subscribed = False

    def add_subscription(self):
        if self.is_subscribed:
            print("Member has already subscribed")
        else:
            self.members.append(self.name)
            print(self.name,"has subscribed")
            self.is_subscribed = True

    def remove_subscription(self):
        if not self.is_subscribed:
            print("Member has not subscribed before.")
        else:
            self.members.remove(self.name)
            print(self.name ,"has removed subscription,.")
            self.is_subscribed = False

book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald", 5)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 9)
library = Library("My Library")
library.add_book(book1)
library.add_book(book2)

member1 = Member(1, "Alice")
member2 = Member(2, "Bob")
member1.add_subscription()
member2.add_subscription()
