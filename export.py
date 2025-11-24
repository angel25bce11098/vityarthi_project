import csv

def export_to_csv(cursor):
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll No","Name","Marks","Grade"])
        writer.writerows(data)

    print("\nCSV Exported Successfully!")