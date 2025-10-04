from utils import database

USER_PROMPT = """
ENTER:
- 'a' to add new book.
- 'l' to list all the books.
- 'r' to mark book as read
- 'd' to delete a book
- 'q' to exit

your choice: """



def menu():

    database.create_book_table()
    

    while True:
     
     user_input = input(USER_PROMPT).lower()
     if user_input == "q":
        break
     
     elif user_input == 'a':
            prompt_add_book()

     elif user_input == 'l':
            list_books()
        
     elif user_input == 'r':
            prompt_mark_as_read()

     elif user_input == 'd':
            prompt_delete_book()
        
     else:
            print("Unknown command, please try again.")


def prompt_add_book():
    name = input("Enter the name of a new book: ")
    author = input("Enter the name of the author: ")


    database.add_book(name= name, author= author)

    

def list_books():
    
    books = database.fetch_all_books()

    for book in books:
            print(f"<📕 {book['name']} by {book['author']}, read: {book['read']}>")
    


def prompt_mark_as_read():
    name = input("Enter the name of the book you finished reading: ")

    database.mark_as_read(name= name)



def prompt_delete_book():
    name = input("Enter the name of the book you want to delete: ")

    database.delete_book(name = name)





if __name__ == "__main__":
    menu()





