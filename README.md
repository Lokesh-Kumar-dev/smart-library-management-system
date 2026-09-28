# Smart Library Management System 📚

A real-world Python application combining FastAPI, SQL Database, and External API integration.

>  Project - Demonstrates List, Tuple, Dictionary, Set, OOP, Inheritance, Encapsulation, SQL & REST APIs in one project.

### 🚀 Features (All 16 Requirements Done)
- *Books:* Add, View All, View One, Update, Delete, Search by title, Check Availability
- *Members:* Add, View All, View One, Update, Delete
- *Borrowing:* Issue Book, Return Book, View Borrowed Books, History, Fine Calculation
- *External API:* Fetch book details by ISBN from OpenLibrary API

### 🧠 Python Concepts Used (As per assignment)
| Concept | Where Used |
| :--- | :--- |
| *LIST* | List of books, members, borrowed books - books = [] |
| *TUPLE* | Fixed statuses BOOK_STATUS = ("AVAILABLE","BORROWED","LOST") |
| *DICTIONARY* | Book details {id, title}, External API JSON response |
| *SET* | Unique categories, unique authors |
| *CLASS/OBJECT* | Book, Member, Student, Teacher, BorrowTransaction |
| *Inheritance* | Student(Member) - 3 books max, Teacher(Member) - 5 books max |
| *Encapsulation* | Private fine self.__fine with getter/setter |
| *Exception Handling* | try/except for DB, invalid ID, book not available |

### 🏗️ Project Structure