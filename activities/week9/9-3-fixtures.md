# Using Pytest fixtures

If you find yourself writing tests where you use the same set-up, 'arrange', steps you can create reusable 'fixtures'.

[Pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.htmle) are used to provide common functions that you
may need for your tests. They are created (set up, yield) and removed (tear down, finalise) using the `@fixture`
decorator.

Fixtures are established for a particular scope using the syntax `@pytest.fixture(scope='module')`. Options for scope
are:

- `function` fixture is executed/run once per test function (if no scope is specified then this is the default)
- `class` one fixture is created per class of tests (if creating test classes)
- `module` fixture is created once per module (e.g., a test file)
- `session` one fixture is created for the entire test session

You may not need to make use of fixtures for COMP0035 coursework, however you will need to use these when we move on to
testing Flask and Dash apps in COMP0034.

Fixtures can be added either within the test file itself or in a separate python file called `conftest.py`. Placing them
in `conftest.py` to make them available to other test modules. `conftest.py` is typically placed in the root of
the `tests` directory, though you can have multiple `conftest.py` files (not covered here).

## Create a fixture

So far you have written code to prepare the data (coursework 1); and execute queries for a sqlite3 database.

To test the data preparation function, you are likely to need to repeatedly create the same DataFrame.

To test the queries, you will need to create a sqlite3 database and create a cursor and connection object.

It would be useful to create fixtures for these.

Create the following fixture in `conftest.py` which is in the `tests` directory.

```python
import os
from pathlib import Path

import pytest

from tutorialpkg.week8_queries.create_query_db import create_db


@pytest.fixture
def db(scope="session"):
    """ Create a database with data for the paralympic tables."""
    db_loc = Path(__file__).parent.parent.joinpath('tests', 'test_para_queries.db')
    data_loc = Path(__file__).parent.parent.joinpath('src', 'tutorialpkg', 'data_db_activity', 'paralympics_all.xlsx')
    con, cur = create_db(data_loc, db_loc)

    # Provide the connection and cursor to the tests
    yield con, cur

    # When the session is finished, close the connection and delete the database file
    con.close()
    if os.path.exists(db_loc):
        os.remove(db_loc)
    else:
        print(f"The file {db_loc} does not exist.")

```

The following Python code creates a sample dataframe. Write a fixture called `sample_df` that 'yields' this dataframe:

```python
import pandas as pd

df = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
})
```

## Modify the tests to use the fixtures

Update the code in the test module so that the test functions use the fixtures.

You can pass a fixture to the function like this: `def test_query_select_succeeds(db):` where a fixture called `db` is
being passed to the function.

## Add more fixtures

Try to add at least one further fixture of your own. For example, add sample data for a Quiz, Question, QuizQuestion and
AnswerChoice to the paralympics database.

[Next activity](9-4-ci-github.md)