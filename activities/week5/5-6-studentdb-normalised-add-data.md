# 6. Use pandas, sqlite3 and SQL to add data to a normalised database

The general approach used in this activity is:

1. Use pandas to load the data from .csv
2. Define the file path to the database
3. Create a connection to the database using sqlite3
4. Create a sqlite3 cursor that will be used to execute the SQL
5. Enable foreign key support
6. Use sqlite3 and SQL queries to write code to add the data from the dataframe to the database
7. Execute the SQL using sqlite3 to create the database structure
8. Close the connection

## Define file paths, load the data from csv into a pandas dataframe

Return to your Python module where you wrote the code to create the normalised enrollment database structure.

You should be able to do this by now!

Add code in 'main' to:

- load the student data to a dataframe.
- define the database file path

## Create the connection and cursor, and enable foreign key support

Create a new function for adding the data to the tables.

Connect to the database, create a cursor and enable the foreign key support.

You did this in the last activity.

```python
# Create a connection to the database using sqlite3
connection = sqlite3.connect(db_path)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Enable foreign key constraints for sqlite
# By default, foreign key constraints are disabled in SQLite, enable them explicitly for each database connection.
cursor.execute('PRAGMA foreign_keys = ON;')

# Commit the changes
connection.commit()
```

## Add data to the student, teacher and courses tables

Write code to add the data to the student, teacher and courses tables.

Here is suggested approach with code to add to your function to add data to the student table.

```python
# Define the SQL insert statement for the parameterised query
student_sql = 'INSERT INTO student (student_name, student_email) VALUES (?, ?)'

# Create a dataframe with the unique values for the columns needed for the student table (excluding the student_id PK)
student_df = pd.DataFrame(df[['student_name', 'student_email']].drop_duplicates())

# Get the values as a list rather than pandas Series. The parameterised query expects a list.
student_data = student_df.values.tolist()

# Use `executemany()` with a parameterised query to add the values to the table.
cursor.executemany(student_sql, student_data)

# Commit the changes to the database
connection.commit()
```

Add code to add data to the teacher and course tables. The above approach should work.

## Add data to the enrollment table

The above won't work for the enrollments table. For this table you need to know the values of the id fields for student,
teacher and course for each row of the dataframe.

One method is to iterate the rows in the dataframe, find the key fields values for each row in the student, teacher and
course tables, then add the new row to the enrollment table.

The code for student_id (`s_id`) is given to you, add the logic yourself for teacher and course.

```python
# Iterate all the rows in the dataframe
for index, row in df.iterrows():
    # Find student_id using student_email which unique in the student table
    # Student email value is in the row you are iterating
    student_email = row['student_email']
    # Define the sql select. The following is a Python f-string, it is not the only approach you could use.
    select_student_sql = f'SELECT student_id FROM student WHERE student_email = "{student_email}"'
    # 'row' variable name is already used so use a different variable name, e.g. 'result'
    # Get the first result from the query, there should only be 1!
    result = cursor.execute(select_student_sql).fetchone()
    # The result is a tuple, so get the first value from the tuple
    s_id = result[0]
    
    # Find teacher_id
    t_id =  # add your code here
    
    # Find course_id
    c_id =  # add your code here
    
    # Insert new row into the enrollment table
    enrollment_insert_sql = 'INSERT INTO enrollment (student_id, course_id, teacher_id) VALUES (?, ?, ?)'
    student_values = (s_id, t_id, c_id)
    cursor.execute(enrollment_insert_sql, student_values)
```

Add code as for the above to your function. You may need to change variable and attribute names depending on your own
code.

Add code to close the connection (you might already have this).

## Run the function to add the data to the tables
Now in `main`, call the function and pass in your database file location and dataframe and run it.

Use the database viewer in your IDE to check the created file has the expected contents.

[Next activity](5-7-create-paralympics-db.md)