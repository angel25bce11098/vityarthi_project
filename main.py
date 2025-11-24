from database import connect_db
from autho import login
from curd import add_student, view_students, update_student, delete_student
from export import export_to_csv

def main():
    conn, cursor = connect_db()
    cursor.execute("INSERT OR IGNORE INTO users VALUES('admin','1234')")
    conn.commit()

    while not login(cursor, conn):
        print("Invalid Login, Try Again")

    while True:
        print("""
-------- MENU --------
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Export CSV
6. Exit
""")

        ch = input("Enter choice: ")

        if ch == "1": add_student(cursor, conn)
        elif ch == "2": view_students(cursor)
        elif ch == "3": update_student(cursor, conn)
        elif ch == "4": delete_student(cursor, conn)
        elif ch == "5": export_to_csv(cursor)
        elif ch == "6": break
        else: print("Invalid Choice!")

if __name__ == "__main__":
    main()