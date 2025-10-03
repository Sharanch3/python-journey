# Book Tracker Application

A simple command-line application for managing your personal book collection. Track books you want to read, mark them as read, and maintain your reading list.

## Problem Statement

Many readers struggle to keep track of their book collections and reading progress. This application solves that problem by providing a lightweight, terminal-based solution to:

- Maintain a persistent list of books with author information
- Track reading status for each book
- Add and remove books from your collection
- View your entire collection at a glance

The application uses a simple text file storage system, making it easy to backup, share, or manually edit your book list if needed.

## Features

- **Add Books**: Store book name and author information
- **List Books**: View all books with their reading status
- **Mark as Read**: Update books when you finish reading them
- **Delete Books**: Remove books from your collection
- **Persistent Storage**: All data saved to a local text file


## Installation

1. Clone or download the project files
2. Ensure both main script and `utils/database.py` are in the correct directory structure:
```
project/
├── app.py
├── utils/
│   └── database.py
└── books.txt (created automatically)
```

## Usage

Run the application:
```bash
python app.py
```

## Limitations

### Data Storage
- **Single file storage**: All books stored in one text file (`books.txt`) with no database backup
- **No data validation**: Duplicate books can be added without warning
- **CSV format vulnerability**: Book names or authors containing commas will break the file format
- **No backup system**: Accidental deletion or file corruption means permanent data loss

### Search and Matching
- **Exact name matching only**: Must type book names exactly as stored (case-sensitive)
- **No partial search**: Cannot find books by partial title or author name
- **No fuzzy matching**: Typos will result in "book not found" errors

### User Experience
- **Command-line only**: No graphical interface
- **No undo functionality**: Deleted books cannot be recovered
- **Limited feedback**: Minimal error messages for failed operations
- **No confirmation prompts**: Destructive actions (delete) happen immediately

### Functionality
- **Single user**: No multi-user support or concurrent access handling
- **Basic read status**: Only binary read/unread (no reading progress, ratings, or dates)
- **No sorting or filtering**: Books displayed in file order only
- **No export options**: Cannot export to other formats (JSON, Excel, etc.)
- **No book metadata**: Cannot store genre, publication year, ISBN, or other details

### Technical Limitations
- **Error handling gaps**: Some edge cases may cause crashes
- **File lock issues**: Concurrent access by multiple instances may corrupt data
- **Encoding issues**: May not handle special characters in all languages correctly
- **No input sanitization**: Newlines or special characters in input can break the storage format
- **Memory inefficient**: Loads entire file for every operation (problematic for large collections)

## Future Improvements

Potential enhancements to address limitations:
- Switch to SQLite database for robust data storage
- Implement fuzzy search and partial matching
- Add data validation and duplicate detection
- Include confirmation prompts for destructive actions
- Add export/import functionality
- Support additional metadata (genre, rating, reading dates)
- Implement backup and restore features
- Add sorting and filtering options

## File Format

Books are stored in `books.txt` with the following CSV format:
```
book_name,author_name,read_status
```
Where `read_status` is `0` (unread) or `1` (read).

