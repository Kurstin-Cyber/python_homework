import sqlite3



def add_student(cursor, name, age, major):
    try:
            cursor.execute("INSERT INTO Students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
    except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")


def add_course(cursor, name, instructor):
    try:
            cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?,?)", (name, instructor))
    except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")


      

def enroll_student(cursor, student, course):
    cursor.execute("SELECT * FROM Students WHERE name = ?", (student,))
    results = cursor.fetchall()
    if len(results) > 0:
        student_id = results[0][0]
    else:
        print(f"There was no student named {student}.")
        return
    
    cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
    results = cursor.fetchall()

    if len(results) > 0:
        course_id = results[0][0]
    else:
        print(f"There was no course named {course}.")
        return

    cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
    results = cursor.fetchall()
    if len(results) > 0:
         print(f"Student {student} is already enrolled in course {course}.")
         return
    
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))

with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    enroll_student(cursor, "Jasmine", "Math 101")
    enroll_student(cursor, "Jasmine", "Chemistry 101")
    enroll_student(cursor, "Pratik", "Math 101")
    enroll_student(cursor, "Pratik", "English 101")
    enroll_student(cursor, "Carlos", "English 101")
    conn.commit()
        