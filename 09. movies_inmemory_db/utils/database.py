# In memory database, concerned with storing and retrieving books from list

books = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def get_all_books():
    return books


def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
            return True
    return False


def delete_book(name):
    global books
    
    original_length = len(books)
    books = [book for book in books if book['name'] != name]
    
    # Return True if a book was deleted (length changed)
    return len(books) < original_length

   