# 4. SQL INSERT queries

## Databases used

[Chinook database](../../src/tutorialpkg/data_db_activity/chinook.db):

<img alt="ERD Chinook database" src="../img/erd-chinook.png" width=50%>

[Paralympics query database](../../src/tutorialpkg/data_db_activity/para_queries.db):

![ERD Paralmpics database for queries](../img/erd-para-queries.png)

## SQL INSERT

Reference links:

- [SQLite INSERT reference](https://www.sqlite.org/lang_insert.html)
- [SQLite INSERT tutorial](https://www.sqlitetutorial.net/sqlite-insert/)

The core syntax of a query to insert a row into a table:

```sqlite
INSERT INTO table_name (column_name_1, column_name_1)
VALUES (value1, value2);
```

If you are submitting values for all the columns, then you can omit the column names:

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

## Executing the queries with sqlite3

Reference link:

- [Python reference: How to use placeholders to bind values in SQL queries](https://docs.python.org/3/library/sqlite3.html#sqlite3-howtos)
- [Python sqlite3 tutorial](https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial)

The examples use a query syntax style called **parameterised query** where a '?' represents the values for each
column. Note that you can use named placeholders instead of question marks, this is not covered here.

Parameterised queries "disconnect" the query from the values. This helps to prevent against malicious injection of SQL.
If the values were to be input by a user, say from a form on a web page, then if the user were to type in malicious SQL
code you do not want that SQL to be run as SQL. If a value is malicious, using a parameterised query ensure it will be
executed separately from the query itself and won't cause any harm to the database. The values passed this way are
handled as text and not as SQL that can be executed.

To use parameterised queries, pass a tuple of values to the second argument of the cursor's `execute()` method.

This example shows 1 row being inserted using `cursor.execute()`:

```python
value_str = "string1"
value_int = 12
value_float = 12.01
cursor.execute("INSERT INTO table_name VALUES(?, ?, ?)", (value_str, value_int, value_float))

# The same as above, written without the variable names
cursor.execute("INSERT INTO table_name VALUES(?, ?, ?)", ("string1", 12, 12.01))
```

To insert a multiple rows, use a list of tuples and `cursor.executemany()`

```python
data = [
    ("string1", 12, 12.01),
    ("string2", 76, 33.07),
    ("string3", 45, 76.56),
]
cursor.executemany("INSERT INTO table_name VALUES(?, ?, ?)", data)
```

If you only want to insert a value or values for a subset of columns then specify the column names:

```python
data = [
    ("string1", 12),
    ("string2", 76),
    ("string3", 45),
]
cursor.executemany("INSERT INTO table_name (column_name, another_column_name) VALUES(?, ?, ?)", data)
```

## Chinook insert queries

View the full code and run the example queries
in: [tutorial8_insert_queries.py](../../src/tutorialpkg/sample_code/tutorial8_insert_queries.py).

### Insert into a table with no relations

```python
# Insert one row
artist_name = "New Artist 1"  # This is a string
cursor.execute('INSERT INTO artists (Name) VALUES (?);', (artist_name,))
connection.commit()

# 2. Insert 3 rows 
values = [("New Artist 2",), ("New Artist 3",), ("New Artist 4",)]  # This is a list of tuples
cursor.executemany('INSERT INTO artists (Name) VALUES (?);', values)
connection.commit()
```

### Insert into related tables

The 'albums' table has columns: Title, ArtistId, AlbumId

To insert a new album, you need to know the ArtistId. What if you know the artists name but not the id?

Assume you want to insert a new album for 'Aerosmith'. If you know their ArtistId is 3 then you can use:

```python
album = (3, "New Album 1")
cursor.execute('INSERT INTO albums (ArtistId, Title) VALUES (?, ?);', album)
```

Otherwise, you need to find the ArtistId first e.g. "SELECT ArtistId from artists WHERE name='Aerosmith'"

```python
cursor.execute('SELECT ArtistId FROM artists WHERE Name = "Aerosmith";')
artist_id = cursor.fetchone()[0]
album_values = (artist_id, "New Album 1")
cursor.execute('INSERT INTO albums (ArtistId, Title) VALUES (?, ?);', album_values)
```

You can also nest SQL queries, e.g., the following both selects the id and then directly inserts it into the database:

```sqlite
INSERT INTO albums (ArtistId, Title)
    SELECT ArtistId, ?
    FROM artists
    WHERE name = 'Aerosmith';
```

### Handling errors

It is considered good practice to catch specific exceptions rather than general ones.

`sqlite3.Error` is the base sqlite3 error. More specific sqlite3 errors include:

- `DatabaseError`: errors that are related to the database e.g. trying to open a file that is not a database file.
- `IntegrityError`: when the relational integrity of the database is affected, e.g., a foreign key check fails.
- `ProgrammingError`: raised due to programming errors, e.g., syntax error in the SQL query.
- `OperationalError`: errors that are related to the database's operation, e.g. a timeout occurs, data source issue

The following query would fail the integrity constraints as the ArtistId cannot be null:

```sqlite
cursor.execute('INSERT INTO albums (Title) VALUES ("New Album 1");')
```

You could catch this using either of these errors:

```python
import sqlite3
# General sqlite3 error
try:
    cursor.execute('INSERT INTO albums (Title) VALUES ("New Album 1");')
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# More specific
try:
    cursor.execute('INSERT INTO albums (Title) VALUES ("New Album 1");')
except sqlite3.IntegrityError as e:
    print(f"An integrity error occurred: {e}")
```

If you use the wrong error then it will not be handled and the code will stop executing, e.g.:

```python
import sqlite3

# Not appropriate for this case, so the error will not be handled and the code will stop
try:
    cursor.execute('INSERT INTO albums (Title) VALUES ("New Album 1");')
except sqlite3.DataError as e:
    print(f"A data error occurred: {e}")
```
An alternative if different errors could be raised it to add more than one error type, e.g.
```python
import sqlite3

# Provide fallback for all errors
try:
    cursor.execute('INSERT INTO albums (Title) VALUES ("New Album 1");')
except sqlite3.DataError as e:
    print(f"A data error occurred: {e}")
except sqlite3.OperationalError as e:
    print(f"An operational error occurred: {e}")
except sqlite3.ProgrammingError as e:
    print(f"A programming error occurred: {e}")
except sqlite3.IntegrityError as e:
    print(f"An integrity error occurred: {e}")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
```

## Paralympics INSERT queries

Write your own code for the following:

1. Insert a new Quiz with quiz_name value "My first quiz"
2. Insert two new Questions for the Quiz you just entered.

    - text="text for question 1"
    - text="text for question 2"
3. Insert three answer choices for one of the new questions.

    - choice_text=""option a" choice_value="1" is_correct="1"
    - choice_text=""option b" choice_value="0" is_correct="0"
    - choice_text=""option c" choice_value="0" is_correct="0"

4. An insert query that would raise an sqlite3.IntegrityError

[Next activity](8-5-update.md)