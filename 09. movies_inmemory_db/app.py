from utils import database


USER_CHOICE = """
ENTER:
- 'a' to add new book. 
- 'l' list all the books.
- 'r' to mark the book has been read.
- 'd' to delete the book.
- 'q' to quit 

Your choice: """


def menu():
    user_input = input(USER_CHOICE).lower()
    
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()

        elif user_input == 'l':
            list_books()

        elif user_input == 'r':
            prompt_read_book()

        elif user_input == 'd':
            prompt_delete_book()

        else:
            print("❌ Enter the valid input, Please try again!")

        user_input = input(USER_CHOICE).lower()


def prompt_add_book():
    name = input("Enter the name of new book you want to add: ").strip().title()
    author = input("Enter the name of the author: ").strip().title()

    database.add_book(name=name, author=author)
    print("-" * 50)
    print("✅ Successfully added!")


def list_books():
    books = database.get_all_books()

    print("-" * 50)
    
    if not books:
        print("📚 No books in your library yet!")
    else:
        for book in books:
            read = 'YES' if book['read'] else 'NO'
            print(f"📕 {book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name = input("Enter the name of the book you read: ").strip().title()
  
    print("-" * 50)
    if database.mark_book_as_read(name):
        print(f"✅ '{name}' marked as read")
    else:
        print(f"❌ Book '{name}' not found")


def prompt_delete_book():
    name = input("Enter the name of the book you want to delete: ").strip().title()

    print("-" * 50)
    if database.delete_book(name):
        print(f"✅ '{name}' successfully deleted!")
    else:
        print(f"❌ Book '{name}' not found")


menu()