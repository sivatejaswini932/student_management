import sqlite3

# Connect database
conn = sqlite3.connect("students.db")

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

conn.commit()


# Add Student
def add_student():

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()

    print("Student Added Successfully")


# View Students
def view_students():

    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    print("\n--- Student Records ---")

    for row in records:
        print(row)


# Main Menu
while True:

    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        view_students()

    elif choice == '3':
        print("Thank You")
        break

    else:
        print("Invalid Choice")3