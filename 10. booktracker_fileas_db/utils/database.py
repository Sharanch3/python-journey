""" 
Concerned with storing and retrieving books from a csv file.
format of the csv file:

name,author,read
"""


books_file = "books.txt"



def add_book(name, author):
    try:
        with open (books_file, 'a') as f:
            f.write(f"{name},{author},0\n")
    except FileNotFoundError:
        print('❌ File name does not exist, please check the file name!')

    except Exception as e:
        print(e)
    
    else:
        print("✅ Successfully added!")



def get_all_books():
    try:
        with open(books_file, 'r') as f:
            lines = [line.strip().split(',') for line in f.readlines()]

        return [
            {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
        
        ]
    except Exception as e:
        print(e)
    
    

def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = 1

    __save_all_books(books)


def __save_all_books(books):
    with open(books_file, 'w') as f:
        for book in books:
            f.write(f"{book['name']},{book['author']},{book['read']}\n")



def delete_book(name):
    books = get_all_books()
    books = [ book for book in books if book['name'] != name]

    __save_all_books(books)
