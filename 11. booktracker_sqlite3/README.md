# 📚 Book Manager - Personal Reading Library

A simple command-line application to manage your personal book collection. Track books you want to read, mark them as read, and keep your reading list organized!

## 🎯 Problem Statement

Many avid readers struggle to keep track of their reading lists. They often forget:
- Which books they've already read
- Books they wanted to read but never got around to
- Who wrote which book in their collection

**Physical solutions** (notebooks, sticky notes) are easy to lose and hard to search through.

**This application solves these problems** by providing a simple, persistent digital library where you can:
- ✅ Add books with author information
- ✅ View your entire collection at a glance
- ✅ Mark books as read when you finish them
- ✅ Remove books you're no longer interested in
- ✅ Keep all data saved locally in a database

## 🚀 Features

- **Add Books**: Store book titles and authors
- **List Books**: View your entire collection with read/unread status
- **Mark as Read**: Track your reading progress
- **Delete Books**: Remove books from your library
- **Persistent Storage**: All data saved in SQLite database
- **Duplicate Prevention**: Won't add the same book twice

## 🛠️ Technologies Used

- **Python 3.x**
- **SQLite3** - Lightweight database for data persistence
- **Context Managers** - Automatic database connection handling

## 📁 Project Structure

```
book-manager/
│
├── app.py                      # Main application file with menu logic
├── utils/
│   ├── __init__.py             # Makes utils a package
│   ├── database.py             # Database operations (CRUD)
│   └── database_connection.py # Context manager for DB connections
├── data.db                     # SQLite database (auto-generated)
└── README.md                   # Project documentation
```

## 🔧 Installation & Setup

1. **Clone or download this repository**

2. **Ensure Python 3.x is installed**
   ```bash
   python --version
   ```

3. **No external dependencies required!** (Uses Python standard library)

## ▶️ How to Run

```bash
python app.py
```

## 💻 Usage

When you run the application, you'll see a menu:

```
ENTER:
- 'a' to add new book
- 'l' to list all books
- 'r' to mark book as read
- 'd' to delete a book
- 'q' to exit

Your choice:
```

### Example Workflow:

1. **Add a book:**
   ```
   Your choice: a
   Enter the book name: The Hobbit
   Enter the author name: J.R.R. Tolkien
   ✅ Successfully added!
   ```

2. **List all books:**
   ```
   Your choice: l
   
   📚 YOUR BOOKS:
   1. 📕 The Hobbit by J.R.R. Tolkien [✗ Unread]
   ```

3. **Mark as read:**
   ```
   Your choice: r
   Enter the book name you finished: The Hobbit
   ✅ Marked as read!
   ```

4. **Delete a book:**
   ```
   Your choice: d
   Enter the book name to delete: The Hobbit
   ✅ Deleted successfully!
   ```

## 🏗️ Technical Highlights

### Context Manager Pattern
The project uses a custom context manager for database connections:

```python
class DatabaseConnection:
    def __enter__(self):
        # Opens connection
        self.connection = sqlite3.connect(self.host)
        return self.connection
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Automatically commits and closes
        if not (exc_type or exc_val or exc_tb):
            self.connection.commit()
        self.connection.close()
```

**Benefits:**
- ✅ Automatic connection cleanup
- ✅ Guaranteed commit on success
- ✅ Proper error handling
- ✅ No resource leaks

### Database Schema

```sql
CREATE TABLE books (
    name TEXT PRIMARY KEY,
    author TEXT,
    read INTEGER DEFAULT 0
);
```

## 🔮 Future Enhancements

- [ ] Add book genres/categories
- [ ] Search functionality
- [ ] Sort books by author or read status
- [ ] Export reading list to CSV/PDF
- [ ] Add reading dates and notes
- [ ] Book ratings (1-5 stars)
- [ ] Web interface using Flask
- [ ] Import books from Goodreads

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Built as a learning project to practice:
- Python fundamentals
- SQLite database operations
- Context managers
- CRUD operations
- Clean code principles

---

**Happy Reading! 📖✨**