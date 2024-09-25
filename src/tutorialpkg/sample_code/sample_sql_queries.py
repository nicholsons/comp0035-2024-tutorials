import sqlite3
from pathlib import Path


def sample_select_queries():
    # Create a SQL connection to the enrollment SQLite database and a cursor
    db_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'sample.db')
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Select all rows and columns from the student table
    cur.execute('SELECT * FROM student')
    rows = cur.fetchall()  # Fetches all results (i.e. use where there could be more than 1)
    print("Multiple rows, print each row as a tuple:")
    for row in rows:
        print(row)  # Prints each row as a tuple

    # From the student table, find the student_id column, where the value in the name column is "Bob Green"
    cur.execute('SELECT student_id FROM student WHERE student_name="Bob Green"')
    row = cur.fetchone()  # Fetches the first result only
    print("\nPrint single row, print the tuple which has only one column in:")
    print(row)  # Prints the tuple containing the student_id
    print("\nPrint single row, print the value of the first (only) column:")
    print(row[0])  # Access the value of the first column in the result, i.e. prints the student_id

    # From the teacher table, find the teacher_name and teacher_email columns, where the value for teacher_id is 1 or 2
    cur.execute('SELECT teacher_name, teacher_email FROM teacher WHERE teacher_id in (1, 2)')
    rows = cur.fetchall()  # Fetches all rows from the result
    # Iterate the rows and print each row
    print("\nPrint multiple rows with multiple columns in each row:")
    for row in rows:
        print("\nThe row as a tuple:")
        print(row)
        # Iterate the items in the row and print each item
        print("\nThe values of all columns in the row:")
        for item in row:
            print(item)
    # Print the value of the first item in the first row
    print("\nPrint the value of the first column in the first row:")
    print(rows[0][0])

    # Close the connection
    con.close()


def sample_insert_queries():
    # Create a SQL connection to the enrollment SQLite database. Create a cursor. Enable foreign key constraints.
    db_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'enrollment_normalised.db')
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')

    # 1. Insert a new row into the student table. Define the values to insert within the SQL query.
    insert_sql = 'INSERT INTO student (student_name, student_email) VALUES ("Harpreet Rai", "harpreet.rai@school.com")'
    cur.execute(insert_sql)
    con.commit()
    # View all the rows in the student table
    rows = cur.execute('SELECT * FROM student')
    print("\nAll rows in the student table:")
    for row in rows:
        print(row)

    # 2. Insert a new row into the student table, using a parameterised query
    # Let sqlite handle the primary key (student_id) by not including it in the insert query
    insert_student_sql = 'INSERT INTO student (student_name, student_email) VALUES (?, ?), ("Jing Li", "jing.li@school.com")'
    cur.execute(insert_student_sql)
    con.commit()

    # View the last inserted row in the student table
    last_student_id = cur.lastrowid  # Get the last inserted row id
    # Use SELECT query with parameterised query to get the last inserted row
    row = cur.execute('SELECT * FROM student WHERE student_id=?', (last_student_id,))
    print('Last inserted row in the student table, using parameterised query:')
    print(row)

    # Insert multiple rows into the teacher table, using a parameterised query
    teachers = [
        ("Aiko Tanaka", "aiko.tanaka@school.com"),
        ("Carlos Mendez", "carlos.mendez@school.com"),
        ("Fatima Al-Mansouri", "fatima.al-mansouri@school.com"),
        ("Liam O'Connor", "liam.oconnor@school.com"),
        ("Sofia Rossi", "sofia.rossi@school.com")
    ]
    # In case you want to add more teachers
    teachers_more = [
        ("Chen Wei", "chen.wei@school.com"),
        ("Elena Petrova", "elena.petrova@school.com"),
        ("Rajesh Kumar", "rajesh.kumar@school.com"),
        ("Maria Garcia", "maria.garcia@school.com"),
        ("Hans Müller", "hans.muller@school.com")
    ]

    # Let sqlite handle the primary key (teacher_id) by not including it in the insert query
    insert_teacher_sql = 'INSERT INTO teacher (teacher_name, teacher_email) VALUES (?, ?)'
    cur.executemany(insert_teacher_sql, teachers)
    # Finally, close the connection
    con.close()

    if __name__ == '__main__':
        sample_select_queries()

    # Uncomment the lines below to run the insert queries and see the results by running the select queries
    sample_insert_queries()
