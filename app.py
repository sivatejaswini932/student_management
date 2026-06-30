from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database Connection
conn = sqlite3.connect("students.db", check_same_thread=False)

cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

conn.commit()


# Home Page
@app.route('/')
def home():
    return render_template("index.html")


# Add Student
@app.route('/add', methods=['POST'])
def add_student():

    name = request.form['name']
    age = request.form['age']
    course = request.form['course']

    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()

    return redirect('/students')


# View Students
@app.route('/students')
def students():

    search = request.args.get('search')

    if search:
        cursor.execute(
            "SELECT * FROM students WHERE name LIKE ?",
            ('%' + search + '%',)
        )
    else:
        cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    return render_template(
        "students.html",
        students=data
    )


# Delete Student
@app.route('/delete/<int:id>')
def delete_student(id):

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()

    return redirect('/students')


# Update Page
@app.route('/update/<int:id>')
def update_page(id):

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    )

    student = cursor.fetchone()

    return render_template(
        "update.html",
        student=student
    )


# Update Student
@app.route('/update_student/<int:id>', methods=['POST'])
def update_student(id):

    name = request.form['name']
    age = request.form['age']
    course = request.form['course']

    cursor.execute("""
    UPDATE students
    SET name=?, age=?, course=?
    WHERE id=?
    """, (name, age, course, id))

    conn.commit()

    return redirect('/students')


if __name__ == '__main__':
    app.run(debug=True)