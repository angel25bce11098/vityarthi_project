import sqlite3

def connect_db():
    conn = sqlite3.connect("grades.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            roll_no INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            marks INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
    """)

    conn.commit()
    return conn, cursor