# Student Exam CRUD System

A simple Python-based student management system with login/registration functionality and CSV export capabilities.

## Features

- User authentication (Login/Register)
- Add new students
- View all students
- Update student information
- Delete students
- Export student data to CSV

## Requirements

- Python 3.x
- SQLite3 (built-in with Python)

## Installation

1. Clone or download this project
2. Navigate to the project directory
3. Run the application:
   ```
   python main.py
   ```

## Usage

1. **First Time Users**: Select option 2 to register a new account
2. **Existing Users**: Select option 1 to login with your username
3. After login, use the menu to manage student records

## Project Structure

- `main.py` - Main application entry point
- `autho.py` - Authentication system (login/register)
- `database.py` - Database connection and setup
- `curd.py` - CRUD operations for students
- `export.py` - CSV export functionality
- `school.db` - SQLite database file (auto-generated)

## Database Schema

**users table**: username
**students table**: id, name, age, grade
