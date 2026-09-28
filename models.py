BOOK_STATUS = ("AVAILABLE", "BORROWED", "LOST", "DAMAGED")
MEMBERSHIP_TYPES = ("STUDENT", "TEACHER", "STAFF")

class Book:
    def __init__(self, book_id, title, author, isbn, category="Programming"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
    
    def display(self):  # PDF Section 8 example
        return f"{self.title} - {self.author}"

class Member:
    def __init__(self, member_id, name, email, member_type="STUDENT"):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.member_type = member_type
        self.max_books = 3  # For business rule
    
    def borrow_book(self):
        pass

class Student(Member):
    def __init__(self, member_id, name, email):
        super().__init__(member_id, name, email, "STUDENT")
        self.max_books = 3  # Student -> 3 books

class Teacher(Member):
    def __init__(self, member_id, name, email):
        super().__init__(member_id, name, email, "TEACHER")
        self.max_books = 5  # Teacher -> 5 books (PDF Section 10)

# encapsulation
class BorrowTransaction:
    def __init__(self):
        self.__fine = 0
    def get_fine(self):
        return self.__fine
    def calculate_fine(self, days):
        self.__fine = days * 10
        return self.__fine

# For FastAPI (Pydantic) 
from pydantic import BaseModel

class BookCreate(BaseModel):
    isbn: str
    title: str
    author: str
    category: str

class MemberCreate(BaseModel):
    name: str
    email: str

class BorrowCreate(BaseModel):
    member_id: int
    book_id: int