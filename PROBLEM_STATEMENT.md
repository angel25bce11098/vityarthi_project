# Problem Statement: Student Exam Management System

## Objective

Develop a console-based Student Exam Management System using Python and SQLite that allows users to perform CRUD operations on student records with authentication.

## Requirements

### 1. User Authentication
- Users must be able to register new accounts
- Users must be able to login with their username
- System should validate user credentials before granting access

### 2. Student Management (CRUD Operations)
- **Create**: Add new student records (name, age, grade)
- **Read**: View all existing student records
- **Update**: Modify existing student information
- **Delete**: Remove student records from the database

### 3. Data Export
- Export all student data to CSV format for external use

### 4. Database
- Use SQLite for data persistence
- Maintain two tables: users and students
- Auto-generate database if it doesn't exist

### 5. User Interface
- Console-based menu system
- Clear prompts and error messages
- Loop until user chooses to exit

## Technical Specifications

- **Language**: Python 3.x
- **Database**: SQLite3
- **Architecture**: Modular design with separate files for different functionalities
- **Data Validation**: Handle invalid inputs gracefully

## Expected Deliverables

1. Working Python application
2. Database schema implementation
3. User authentication system
4. Complete CRUD functionality
5. CSV export feature
6. Documentation (README)
