# 1. Introduction: Using Python sqlite3 and pandas to create SQLite databases

## Overview

In this activity you will use the logical database design documented in the ERD, and use it to create a database.

There are many ways and tools that can be used to create a relational database. This activity uses a combination of:

- pandas DataFrame to load the data
- Python sqlite to create a database and access a database file
- SQLite database file to store the data

## SQL or SQLite

SQL, or Structured Query Language, is a programming language designed for managing and manipulating relational
databases. It allows users to perform various operations on the data stored in these databases, such as:

- Creating: Defining new databases, tables, and other database objects.
- Querying: Retrieving specific data by writing queries.
- Inserting: Adding new records to the database.
- Updating: Modifying existing records.
- Deleting: Removing records from the database.
- Managing: Controlling access to the data and ensuring data integrity.

SQL is widely used in data analysis, web development, and many other fields where data management is needed.

SQLite is a variant of SQL. As the name implies, it has less syntax and features than SQL. It is used in this course
as a [key benefit](https://www.sqlite.org/whentouse.html) of SQLite for this course is that it saves the database as a
single file which does not require a database server to work with. This simplifies the infrastructure you need for the
course.

Many, but not all, of the SQL commands exist for SQLite. You should refer to
the [SQLite documentation](https://www.sqlite.org/docs.html) for
syntax, though more [general SQL references](https://www.w3schools.com/sql/) will still be useful.

## sqlite3

[sqlite3](https://docs.python.org/3/library/sqlite3.html) is a library that is bundled with the Python standard library
so you do not need to 'pip install' it as we have with other packages.

The [sqlite3 tutorial](https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial) may be a useful reference.

sqlite3 can be used to create databases.

The typical steps involved in using sqlite3 are:

- Import `import sqlite3`
- Define the path to a database file
- Create a connection object to the database
- Create a cursor object
- Use the cursor object to execute SQL queries on the database. 'Queries' here refers to executing SQL statements which
  covers creating, querying, inserting, deleting and updating.
- Close the connection object

## sqlalchemy

[sqlalchemy](https://www.sqlalchemy.org) provides an alternative to sqlite3. It is written to work with SQL databases in
Python, and is not only for sqlite. "sqlalchemy" will be used in COMP0034. You will see it described as an ORM, Object
Relational Mapper, which "maps" Python classes to database tables. It abstracts database operations, with the aim of
making it easier for developers to work with queries.

You must install sqlalchemy to use it e.g., `pip install sqlalchemy`

The typical steps involved in using sqlalchemy with pandas to add data to the database:

- Import `from sqlalchemy import create_engine`
- Define the database file path
- Create an instance of a sqlite connection engine
- Connect to the database
- Use the DataFrame.to_sql method to execute the sql, using the connection engine as the value for the `con=` parameter

DataFrame.to_sql handles the commit.

This tutorial focuses on sqlite3 as it uses SQL directly, and you need to develop an understanding of this. However,
there is an example of using sqlalchemy
in [sqlalchemy_demo.py](../../src/tutorialpkg/sample_code/sqlalchemy_demo.py). You can use it in the coursework if
you prefer.

## pandas DataFrame

You have used pandas DataFrame to read the data from a .csv or .xslx file, and to save a DataFrame back to .csv. Pandas
DataFrame has methods that will interact with a SQL, or SQLite, database.

- [pd.read_sql](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)
- [pd.read_sql_table](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html)
- [pd.read_sql_query](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)
- [df.to_sql](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)

[Next activity](5-2-create-studentdb-unnormalised)