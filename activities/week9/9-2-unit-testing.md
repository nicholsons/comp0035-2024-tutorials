# Writing unit tests with Pytest

Before starting, make sure you:

1. Configured your IDE to support pytest
2. Installed pytest in your venv `pip install pytest`
3. [Pytest good practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html) recommends you install your
   project code in your virtual environment (venv) using `pip install -e .`. Check that you updated your
   pyproject.toml if you changed your code directory structure or name.

## Test case structure

Given the guidance the introduction, the following is a suggested way to approach writing a unit test.

1. Write an appropriate test case name

   The test functions inside the test python module (file) typically have the prefix `test_`. The test
   name should make it clear what is being tested e.g. `test_add_success_with_integers` is lengthy but more descriptive
   than `test_add` which only tells you the method being tested and not what behavior you are testing.

2. Add the test description as the docstring. The following examples uses the 'GIVEN > WHEN > THEN' pattern.

    ```python
   def test_valid_email():
    """
        GIVEN valid values an Admin object, email='test@test.com' and password='testpassword'
        WHEN the Admin object 'admin' is created
        THEN admin.email should equal 'test@test.com'
    """
    ```

3. Write the code to set up the test conditions

    - `Arrange`: Provide the values e.g. `email = 'test@test.com`, `password = 'testpassword'`

4. Call the function under test:

    - `Act`: Create an instance of Admin e.g. admin = Admin(email, password)

5. Write the assertion code

    - `Assert`: Add the assertion e.g. `assert admin.email == email`

6. Run the test and check it passes e.g. `pytest -v test_modulename.py::test_valid_email`

## Write unit tests

[tutorial2_refactored.py](../../src/tutorialpkg/tutor_solution/tutorial2_refactored.py) is a refactored version of
the week solution to prepare the data. Refactoring is an approach that improves the structure of code without changing
its behaviour. In this case the code has been refactored (restructured) into several smaller functions in place of one
long function.

In the directory called `tests` as a new Python file for the test cases, e.g., `test_data_prep.py`

Let's test that the function to save a dataframe to file works. This function takes a dataframe, an output file location
and a file_type of 'csv' or 'xlsx'. If the function is successful then one test would be to check for the presence of
the file in the file system.

```python
from pathlib import Path
import pandas as pd
from tutorialpkg.tutor_solution import tutorial2_refactored


def test_save_dataframe_file_present():
    """
    GIVEN a pandas dataframe
    WHEN tutorial2_refactored.save_dataframe_to_file() is called with the correct file path and file type
    THEN the file specified should be found as a valid file in the file system
    """
    df = pd.DataFrame({
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    })
    # Arrange
    file_path_save = Path(__file__).parent.joinpath('output_df.csv')
    # Act
    tutorial2_refactored.save_dataframe_to_file(df, file_path_save, file_type='csv')
    # Assert
    assert file_path_save.is_file()
```

There are several ways to run a test depending on your IDE. For example, right-click on the filename in the project pane
and 'Run tests'.

For now, open the Terminal in the IDE and enter:  `pytest -v`. This should run all tests. Depending on your computer you
may need to use `python3 -m pytest -v` or `py3 -v pytest`.

You can also specify the test to run e.g., `pytest -v tests/test_data_prep.py::test_save_dataframe_file_present`

Another check that the save function worked correctly might be to read the contents of the file and check that they
match the original dataframe. It is generally accepted that a unit test should have a single reason to fail. This may or
may not be interpreted as a single assertion. In this case you could consider that the second assertion is still
checking the same condition so you could add a second assertion to the same test. Try this:

```python
def test_save_dataframe_file_present():
    """
    GIVEN a pandas dataframe
    WHEN tutorial2_refactored.save_dataframe_to_file() is called with the correct file path and file type
    THEN the file specified should be found as a valid file in the file system
    AND reading the file into dataframe should give a dataframe contents equal to the original dataframe
    """
    df = pd.DataFrame({
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    })
    # Arrange
    file_path_save = Path(__file__).parent.joinpath('output_df.csv')
    # Act
    tutorial2_refactored.save_dataframe_to_file(df, file_path_save, file_type='csv')
    # Assert
    assert file_path_save.is_file()
    read_df = pd.read_csv(file_path_save)
    assert read_df.equals(df)
```

## Write a test that raises an exception

The syntax
to [test exceptions](https://docs.pytest.org/en/7.1.x/how-to/assert.html#assertions-about-expected-exceptions) is
different.

The function to save a dataframe to file
in [tutorial2_refactored.py](../../src/tutorialpkg/tutor_solution/tutorial2_refactored.py) raises a ValueError if
file_type is not either 'csv' or 'xlsx'. Add this test to your code and run it:

```python
from pathlib import Path
import pandas as pd
import pytest
from tutorialpkg.tutor_solution import tutorial2_refactored


def test_save_dataframe_incorrect_type_raises_error(db):
    """
    GIVEN a dataframe
    WHEN save_dataframe_to_file is called with .txt which is not supported
    THEN a ValueError should be raised with the message 
    'Invalid file type. Please specify 'csv' or 'xlsx'.
    """
    df = pd.DataFrame({
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    })
    path_to_save = str(Path(__file__).joinpath('incorrect_file.txt'))
    with pytest.raises(ValueError):
        tutorial2_refactored.save_dataframe_to_file(df, path_to_save, file_type='txt')

```

## Write a test for a query

Create a new test module called `test_queries.py` in the 'tests' directory.

Add a fixture to create a deck of cards database.

For example:

```python
import os
import sqlite3
import pytest
from pathlib import Path


@pytest.fixture
def cards_db():
    """Creates a database with suits and ranks and yields a sqlite3 connection to the database."""
    db_path = Path(__file__).parent.joinpath('test_deck_cards.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    conn.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS ranks (rank_id INTEGER PRIMARY KEY AUTOINCREMENT, rank TEXT NOT NULL);")
    cur.execute("CREATE TABLE IF NOT EXISTS suits (suit_id INTEGER PRIMARY KEY AUTOINCREMENT, suit TEXT NOT NULL);")
    suit_values = [('Clubs',), ('Diamonds',), ('Hearts',), ('Spades',)]
    rank_values = [(2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), ('Jack',), ('Queen',), ('King',), ('Ace',)]
    cur.executemany("INSERT INTO ranks (rank) VALUES (?)", rank_values)
    cur.executemany("INSERT INTO suits (suit) VALUES (?)", suit_values)
    conn.commit()
    yield conn
    conn.close()
    if os.path.exists(db_path):
        os.remove(db_path)
    else:
        print(f"The file {db_path} does not exist.")
```

We don't have a function to generate the queries so will add them in the test case itself.

```python
def test_deck_cards_contains_queen_hearts(cards_db):
    """
    GIVEN a database with table called suits and ranks with relevant rows and values
    WHEN a cross join query is made
    THEN the result should contain Queen of Hearts
    """
    expected_card = ('Hearts', 'Queen')
    cur = cards_db.cursor()
    rows = cur.execute("SELECT suit, rank FROM ranks CROSS JOIN suits ORDER BY suit;")
    cards = []
    [cards.append(row) for row in rows]
    assert expected_card in cards
```

Run the tests again.

Now try and add a query for the following:

```python

    """
    GIVEN a database with table called suits
    WHEN a select all query is made to to get all suit in the suits table
    THEN the result should contain 'Clubs', 'Diamonds', 'Hearts', 'Spades'
    """
```

## Write more unit tests

Try and write a few more tests to get practice. Some suggestions:

1. Test that the suits table contains 'Clubs', 'Diamonds', 'Hearts', 'Spades'
2. Test that you cannot add a new suit and leave the column 'suit' empty
3. Add a new suit. Assert that the row count in the table is +1 after the insert? Or get the rowid and check it exists?
4. Delete a suit and check it no longer exists.
5. Update the ranks with rank=2 to 'Two'. There should be 4 rows changed.

You could also try and write a fixture and test queries for the paralympics database or the chinook database.

## Use Copilot to generate a unit test

If you have copilot enabled in your IDE, try generating a test automatically.

For example, open [create_query_db.py](../../src/tutorialpkg/week8_queries/create_query_db.py), right-click on the
`create_paralympics_db_structure` function name and find the option to generate a test:

- PyCharm: Generate... | Test
- VS Code: Copilot | Generate tests...

Review the generated code. Do you agree with it?

Run the tests and see if they run.

[Next activity](9-3-fixtures.md)