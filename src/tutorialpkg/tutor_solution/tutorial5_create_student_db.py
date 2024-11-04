""" Activities 5.2 to 5.4: Create the student database from a pandas dataframe with sqlite3 """
import sqlite3
from pathlib import Path

import pandas as pd


def create_student_db_not_normalised(df, db_path, table_name):
    """Create a database from a pandas dataframe without normalising the data.

    Creates a database using all columns in a single table.

    Args:
        table_name: The name of the table to be created in the database.
        df (pd.DataFrame): The pandas dataframe to be saved to the database.
        db_path (str): The name and location of the database file.

    Returns:
        None

    """
    # Create a connection to the database using sqlite3.
    conn = sqlite3.connect(db_path)

    # Save the dataframe to the database, this will create a table called 'enrollments' and replace it if
    # it exists. The index column is not saved to the table.
    # If the file does not exist then it will be created.
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection.
    conn.close()


def create_student_db_normalised_structure(db_path):
    """
    Create the student enrollment database structure

    Args:
        db_path (str): The name and location of the database file.

    Returns:
       None

    """
    # Define the tables and relationships between the tables using SQL statements
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
                            enrollment_id INTEGER PRIMARY KEY,
                            student_id INTEGER NOT NULL, 
                            course_id INTEGER NOT NULL,
                            teacher_id INTEGER,
                            FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE cascade ON UPDATE cascade,
                            FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE cascade ON UPDATE cascade,
                            FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON UPDATE cascade ON DELETE SET NULL);
                            '''
    connection = sqlite3.connect(db_path)
    try:
        with connection:
            # Create a cursor object to execute SQL commands
            cursor = connection.cursor()

            # Enable foreign key constraints for sqlite
            # By default, foreign key constraints are disabled in SQLite, enable them explicitly for each database connection.
            cursor.execute('PRAGMA foreign_keys = ON;')

            # Commit the changes (not needed here as we are using the 'with' statement)
            # connection.commit()

            # Create the tables in the database by executing the SQL statements and then commit the changes to the database
            cursor.execute('DROP TABLE IF EXISTS enrollment;')
            cursor.execute('DROP TABLE IF EXISTS course;')
            cursor.execute('DROP TABLE IF EXISTS teacher;')
            cursor.execute('DROP TABLE IF EXISTS student;')
            cursor.execute(student_sql)
            cursor.execute(teacher_sql)
            cursor.execute(course_sql)
            cursor.execute(enrollment_sql)

            # Commit the changes (not needed here as we are using the 'with' statement)
            # connection.commit()
    except sqlite3.Error as err:
        print(f'An error occurred creating the database structure. Error: {err}')
    finally:
        if connection:
            # Close the connection.
            connection.close()


def add_student_data(df, db_path):
    """
    Add data to the student enrollment database from a pandas dataframe

    This version uses SQL SELECT and INSERT.

    Args:
        df (pd.DataFrame): The pandas dataframe to be saved to the database.
        db_path (str): The name and location of the database file.

    Returns:
       None

    """
    # Create a connection to the database using sqlite3
    connection = sqlite3.connect(db_path)

    try:
        with connection:
            # Create a cursor object to execute SQL commands
            cursor = connection.cursor()

            # Enable foreign key constraints for sqlite
            # By default, foreign key constraints are disabled in SQLite, enable them explicitly for each database connection.
            cursor.execute('PRAGMA foreign_keys = ON;')

            # Commit the changes
            # connection.commit()  # Required if you are not using the 'with connection:' statement

            # Insert data into student table (unique values only)
            student_sql = 'INSERT INTO student (student_name, student_email) VALUES (?, ?)'
            student_df = pd.DataFrame(df[['student_name', 'student_email']].drop_duplicates())
            # Get the values as a list rather than pandas Series
            student_data = student_df.values.tolist()
            cursor.executemany(student_sql, student_data)
            # connection.commit()  # Required if you are not using the 'with connection:' statement

            # Insert data into teacher table (unique values only)
            teacher_sql = 'INSERT INTO teacher (teacher_name, teacher_email) VALUES (?, ?)'
            teacher_df = pd.DataFrame(df[['teacher_name', 'teacher_email']].drop_duplicates())
            teacher_data = teacher_df.values.tolist()
            cursor.executemany(teacher_sql, teacher_data)
            # connection.commit()  # Required if you are not using the 'with connection:' statement

            # Insert data into course table (unique values only)
            course_sql = 'INSERT INTO course (course_name, course_code, course_schedule, course_location) VALUES (?, ?, ?, ?)'
            course_df = pd.DataFrame(df[['course_name', 'course_code', 'course_schedule', 'course_location']].drop_duplicates())
            course_data = course_df.values.tolist()
            cursor.executemany(course_sql, course_data)
            # connection.commit()  # Required if you are not using the 'with connection:' statement

            # Insert data into enrollment table
            # Iterate all the rows in the dataframe
            for index, row in df.iterrows():
                # Find student_id
                student_email = row['student_email']
                select_student_sql = f'SELECT student_id FROM student WHERE student_email = "{student_email}"'
                result = cursor.execute(select_student_sql).fetchone()
                # 'row' is already used so use a different variable name, e.g. 'result'
                s_id = result[0]

                # Find teacher_id
                teacher_email = row['teacher_email']
                select_teacher_sql = f'SELECT teacher_id FROM teacher WHERE teacher_email = "{teacher_email}"'
                result = cursor.execute(select_teacher_sql).fetchone()
                t_id = result[0]

                # Find course_id
                course_code = row['course_code']
                select_course_sql = f'SELECT course_id FROM course WHERE course_code = "{course_code}"'
                result = cursor.execute(select_course_sql).fetchone()
                c_id = result[0]

                # Insert new row into the enrollment table
                enrollment_insert_sql = 'INSERT INTO enrollment (student_id, course_id, teacher_id) VALUES (?, ?, ?)'
                student_values = (s_id, t_id, c_id)
                cursor.execute(enrollment_insert_sql, student_values)

            # connection.commit() # Required if you are not using the 'with connection:' statement

    except sqlite3.Error as err:
        print(f'An error occurred creating the database. Error: {err}')
    finally:
        if connection:
            # Close the connection.
            connection.close()


if __name__ == '__main__':
    try:
        # CSV file path and file name
        data_file = Path(__file__).parent.parent.joinpath('data_db_activity', 'student_data.csv')

        # Activity 5-2: Create a database from a pandas dataframe
        # Database file path and file name
        db_file_un = str(Path(__file__).parent.parent.joinpath('data_db_activity', 'enrollment_not_normalised.db'))

        # Create a pandas dataframe from the CSV file
        df_enrollments = pd.read_csv(data_file)

        # Table name to be created in the database
        table = 'enrollments'

        # Create a database from the pandas dataframe
        create_student_db_not_normalised(df_enrollments, db_file_un, table)

        # Activity 5-3: Create a normalised database from the pandas dataframe
        db_file_norm = str(Path(__file__).parent.parent.joinpath('data_db_activity', 'enrollment_normalised.db'))
        create_student_db_normalised_structure(db_file_norm)
        add_student_data(df_enrollments, db_file_norm)

    except FileNotFoundError as e:
        print(f' File not found. {e}')
