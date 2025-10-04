from .database_connection import DatabaseConnection


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name TEXT PRIMARY KEY, author TEXT, read INTEGER)")



def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM books WHERE name =?",(name,))
        existing_book = cursor.fetchone()
        
        if existing_book:
            print(f"❌  Book '{name}' already exists!")
        
        else:
            cursor.execute("INSERT INTO books VALUES(?, ?, 0)",(name, author))

            print("✅ Successfully added!")



def fetch_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books")
        books =  [{'name': row[0], 'author': row[1], 'read': row[2] } for row in cursor.fetchall()]

    return books



def mark_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books WHERE name =?",(name,))
        existing_book = cursor.fetchone()

        if existing_book:
            cursor.execute("UPDATE books SET read=1 WHERE name=?",(name,))
            print("✅ Marked as read!")
        
        else:
            print(f"❌ Book '{name}' does not exist!")
    
    


def delete_book(name):
   with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books WHERE name=?",(name,))
    existing_book = cursor.fetchone()

    if existing_book:
        cursor.execute("DELETE FROM books WHERE name=?",(name,))
        print("✅ Deleted successfully!")
        
    else:
        print("❌ Book name does not exist")
   

    

