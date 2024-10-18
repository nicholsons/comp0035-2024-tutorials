# 5. Introduction to SQL queries to add (insert) data into a table

For the activities after this one, you will need to be able to add data to tables where pandas.to_sql is not sufficient.

This activity covers the minimum knowledge to add one or more values to a table in a sql statement. It is not sufficient
to add values in a single SQL statement to tables joined by relationships; this is covered after reading week.

The following references have more details:

- [SQLite INSERT reference](https://www.sqlite.org/lang_insert.html)
- [SQLite SELECT tutorial](https://www.sqlitetutorial.net/sqlite-insert/) gives examples.

There are plenty of other reference sites available if you search.

## SQLite syntax

The core syntax of a query to insert one row of values into a table is:

```sqlite
INSERT INTO table_name (column_name_1, column_name_1)
VALUES (value1, value2);
```

If the table only has those two columns, then you can omit the column names like this:

```sqlite
INSERT INTO table_name
VALUES (value1, value2);
```

To insert multiple rows with values:

```sqlite
INSERT INTO table_name (column_name_1, column_name_1)
VALUES (value1, value2),
       (value1, value2),
       (value1, value2);
```

The above allow you to specify the names of the columns to insert the values, as well as the values.

This would be cumbersome where you have many columns and/or many values.

It is possible to select values based on a query and then insert them; however this is more complex and not
covered at this stage of the module. You are welcome to do your own research and use this approach. The general
syntax is:

```sqlite
INSERT INTO first_table_name (column1, column2, columnN)
SELECT column1, column2, columnN
FROM second_table_name
WHERE condition;
```

## Using sqlite3 to insert

The following outlines a general approach to use Python sqlite3 to insert a row values and view them:

```python
from pathlib import Path
import sqlite3

# Connect to SQLite, create cursor
db_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'enrollment_normalised.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

# Define the SQL INSERT query
insert_sql = 'INSERT INTO student (student_name, student_email) VALUES ("Harpreet Rai", "harpreet.rai@school.com")'

# Execute the insert query 
cur.execute(insert_sql)

# Commit the changes
con.commit()

# Execute a select query to get and print all rows, including the new row
rows = cur.execute('SELECT * FROM student')
print("\nAll rows in the student table:")
for row in rows:
    print(row)

# Close the cursor object and database connection object
cur.close()
con.close()
```

In an application you are more likely to be adding values generated from variables.

Using the sqlite3 library there is a more convenient way to do this using the following generic syntax:

`cursor.execute("INSERT INTO table_name VALUES(?, ?, ?)", data)`

- There is one `?` for each of the columns in the table_name
- The `data` is the values for each of the columns e.g. `("some_string", 7, 12.87)` and must match the same order as the
  columns in the table

This is called a **parameterised query**.

Here is an example:

```python
value_str = "string1"
value_int = 12
value_float = 12.01
cursor.execute("INSERT INTO table_name VALUES(?, ?, ?)", (value_str, value_int, value_float))

# The same as above, written without the variable names
cursor.execute("INSERT INTO table_name VALUES(?, ?, ?)", ("string1", 12, 12.01))
```

To insert a multiple rows instead of one, use a list of values and `cursor.executemany()`

```python
data = [
    ("string1", 12, 12.01),
    ("string2", 76, 33.07),
    ("string3", 45, 76.56),
]
cursor.executemany("INSERT INTO table_name VALUES(?, ?, ?)", data)
```

If you only want to insert a value or values for a subset of columns then specify the column names. This is useful when
the PRIMARY KEY is an auto-incrementing integer as you don't want to specify the value, you want the database to just
add the next value based on the previous row.

e.g. `cursor.execute("INSERT INTO table_name (column_name2, column_name3) VALUES(?, ?)", data)`

```python
data = [
    ("string1", 12),
    ("string2", 76),
    ("string3", 45),
]
cursor.executemany("INSERT INTO table_name (column_name, another_column_name) VALUES(?, ?, ?)", data)
```

## Run the sample insert query code

Open the [sample_sql_query.py](../../src/tutorialpkg/sample_code/sample_sql_queries.py).

Run `sample_insert_queries()` to see the results of the examples above.

If you run `sample_insert_queries()` multiple times you will get a constraint violation error as the email
address fields must be unique. Edit the code and pass new values to add more rows and run the code again.

[Next activity](5-6-studentdb-normalised-add-data.md)