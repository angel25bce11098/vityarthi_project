from utils import calculate_grade

def add_student(cursor, conn):
    roll = int(input("Roll No: "))
    name = input("Name: ")
    marks = int(input("Marks: "))
    grade = calculate_grade(marks)

    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (roll, name, marks, grade))
    conn.commit()

def view_students(cursor):
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def update_student(cursor, conn):
    roll = int(input("Enter Roll to Update: "))
    marks = int(input("New Marks: "))
    grade = calculate_grade(marks)

    cursor.execute("UPDATE students SET marks=?, grade=? WHERE roll_no=?", (marks, grade, roll))
    conn.commit()

def delete_student(cursor, conn):
    roll = int(input("Roll to Delete: "))
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll,))
    conn.commit()