# Book Manager CLI

A simple command-line application for managing your personal book collection with proper error handling and user feedback.

## Problem Statement

Book lovers often struggle to keep track of their personal book collection - which books they own, who wrote them, and whether they've been read. This application provides a lightweight, terminal-based solution for managing your reading list without the complexity of database setup, web interfaces, or account creation.

The goal is to offer a straightforward tool that helps you:
- Maintain a catalog of books with author information
- Track reading progress for each book
- Manage your collection by adding and removing titles
- Get immediate feedback on all operations

## Features

✅ **Add Books** - Store book titles with their authors  
✅ **List Books** - View your entire collection with reading status  
✅ **Mark as Read** - Update books when you've finished reading them  
✅ **Delete Books** - Remove books from your collection  
✅ **Error Handling** - Clear feedback when books are not found  
✅ **Empty Library Messages** - Friendly notification when no books exist

## Installation

1. Ensure Python 3.x is installed on your system
2. Create the following project structure:

```
book-manager/
├── utils/
│   └── database.py
└── app.py
```

3. Copy the code into the respective files

## Usage

Run the application from your terminal:

```bash
python app.py
```

### Example Session

```
Your choice: a
Enter the name of new book you want to add: The Hobbit
Enter the name of the author: J.R.R. Tolkien
--------------------------------------------------
✅ Successfully added!

Your choice: l
--------------------------------------------------
📕 The Hobbit by J.R.R. Tolkien, read: NO

Your choice: r
Enter the name of the book you read: The Hobbit
--------------------------------------------------
✅ 'The Hobbit' marked as read

Your choice: q
```

## Current Limitations

### 1. **No Data Persistence**
- Books are stored in memory only (Python list)
- All data is lost when the application closes
- No file storage, database, or cloud backup

### 2. **No Input Validation**
- Empty strings can be entered for book names/authors
- Duplicate books can be added without warning
- No ISBN or unique identifier system

### 3. **Case Sensitivity Issues**
- All titles are converted to title case using `.title()`
- This causes problems with special capitalization (e.g., "iPhone" becomes "Iphone")
- Book searches require exact match after title case conversion
- Articles get capitalized incorrectly ("the lord of the rings" → "The Lord Of The Rings")




