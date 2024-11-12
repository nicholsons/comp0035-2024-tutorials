import sqlite3
from pathlib import Path


if __name__ == '__main__':
    # This is a long sequence of steps to create a database structure.
    # For the coursework you should structure your code into functions and consider error handling
    student_sql = '''CREATE TABLE student (
                           student_id INTEGER PRIMARY KEY,
                           student_name TEXT NOT NULL,
                           student_email TEXT NOT NULL UNIQUE);'''
    teacher_sql = '''CREATE TABLE teacher (
                           teacher_id INTEGER PRIMARY KEY,
                           teacher_name TEXT NOT NULL,
                           teacher_email TEXT NOT NULL UNIQUE);'''
    course_sql = '''CREATE TABLE course (
                           course_id INTEGER PRIMARY KEY,
                           course_name TEXT NOT NULL,
                           course_code INTEGER NOT NULL,
                           course_schedule TEXT,
                           course_location TEXT);'''
    enrollment_sql = '''CREATE TABLE enrollment (
                               student_id INTEGER NOT NULL, 
                               course_id INTEGER NOT NULL,
                               teacher_id INTEGER,
                               PRIMARY KEY (student_id, course_id, teacher_id),
                               FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE cascade ON UPDATE cascade,
                               FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE cascade ON UPDATE cascade,
                               FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON UPDATE cascade ON DELETE SET NULL);
                               '''

    db_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'sample.db')
    data_file = Path(__file__).parent.parent.joinpath('data_db_activity', 'student_data.csv')

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')
    connection.commit()

    # Create tables
    cursor.execute(student_sql)
    cursor.execute(teacher_sql)
    cursor.execute(course_sql)
    cursor.execute(enrollment_sql)

    # Commit then close connection
    connection.commit()
    connection.close()