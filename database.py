import pyodbc

conn_str = "DRIVER={SQL Server};SERVER=HP\\SQLEXPRESS;DATABASE=LibrarySystemDB;Trusted_Connection=yes;"

def get_connection():
    return pyodbc.connect(conn_str)

def create_tables():
    c = get_connection()
    cur = c.cursor()
    # books table
    cur.execute("""
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='books')
        CREATE TABLE books(
            id INT IDENTITY(1,1) PRIMARY KEY,
            isbn VARCHAR(20),
            title VARCHAR(100),
            author VARCHAR(100),
            category VARCHAR(100),
            available BIT DEFAULT 1
        )
    """)
    # members table
    cur.execute("""
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='members')
        CREATE TABLE members(
            id INT IDENTITY(1,1) PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)
    # borrowings table - FIXED column names
    cur.execute("""
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='borrowings')
        CREATE TABLE borrowings(
            id INT IDENTITY(1,1) PRIMARY KEY,
            book_id INT,
            member_id INT,
            borrowed_date DATETIME,
            returned_date DATETIME,
            status VARCHAR(20)
        )
    """)
    c.commit()
    c.close()
    print("3 tables created successfully")

if __name__ == "__main__":
    create_tables()