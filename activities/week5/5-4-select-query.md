# 4. Introduction to SQL queries to find data

For activities 5.6 onwards, you will need to be able to find the primary key values for rows you have added to
tables.

You need to know a little about SQL SELECT queries to complete this.

This activity covers the minimum knowledge to find one or more values from a single table. It is not sufficient to find
values from tables joined by relationships; this is covered after reading week.

The following references have more details:

- [SQLite SELECT reference](https://www.sqlite.org/lang_select.html)
- [SQLite SELECT tutorial](https://www.sqlitetutorial.net/sqlite-select/) gives examples.

There are plenty of other reference sites available if you search.

## SQLite syntax

The core syntax of a query to find one or more rows or values from a table is:

```sqlite
SELECT column_names
FROM table_name
WHERE some_condition;
```

To select all columns and rows from the `student` table in
the [sample.db](../../src/tutorialpkg/data_db_activity/sample.db) database you can use the '*' instead of writing all
the column names. The SQL looks like this:

```sql
SELECT *
FROM student;
```

To select one or more rows meeting a given condition, add
a [WHERE clause](https://www.sqlitetutorial.net/sqlite-where/).

This example selects one result. It finds the student_id column from the student table where the value in the
student_name column is 'Bob Green':

```sqlite
SELECT student_id
FROM student
WHERE student_name = "Bob Green";
```    

This example selects several results. It finds the teacher_email and teacher_name of the teachers with teacher_id of 1
or 2:

To put these in context with the sqlite3 python code:

```python
import sqlite3
from pathlib import Path

# Create a SQL connection to our SQLite database and a cursor
db_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'student_normalised.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

# Select all rows and columns from the student table
cur.execute('SELECT * FROM student')
rows = cur.fetchall()  # Fetches more than 1 row

# Select the student_id column 
cur.execute('SELECT student_id FROM student WHERE student_name="Blue Bird"')
row = cur.fetchone()  # Fetches the first result

# Close the connection
con.close()
```

- `fetchall()` returns a list of tuples, each tuple contains field values of a row.
- `fetchone()` returns a row as a tuple.
- `fetchmany(size)` returns a specified number of rows as tuples.

## Accessing values from the result row

The rows are returned as tuples. To access specific values from a tuple you need to use list style notation to access
the element (NB: lists values start at 0 and not 1).

For example, with a single result:

```python
# From the student table, find the student_id column, where the value in the name column is "Bob Green"
cur.execute('SELECT student_id FROM student WHERE student_name="Bob Green"')
row = cur.fetchone()  # Fetches the first result only
print(row)  # Prints the tuple containing the student_id
print(row[0])  # Access the value of the first column in the result, i.e. prints the student_id
```

For example, with a multiple row result:

```python
cur.execute('SELECT teacher_name, teacher_email FROM teacher WHERE teacher_id in (1, 2)')
rows = cur.fetchall()  # Fetches all rows from the result
# Iterate the rows and print each row
for row in rows:
    print(row)
    # Iterate the items in the row and print each item
    for item in row:
        print(item)
# Print only the value of the first item in the first row
print(rows[0][0])
```

## Run the sample insert query code

Open the [example_sql_query.py](../../src/tutorialpkg/sample_code/example_sql_queries.py).

Run `sample_insert_queries()` to see the results of the examples above.

## Challenge

Add your own query code to the sample queries code:

- Find all rows and columns for the courses table
- Find the course code for 'Chemistry'
- Find all course where the schedule includes Monday

[Next activity](5-5-insert-query.md)