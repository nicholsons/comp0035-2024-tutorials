import os
from pathlib import Path

import pytest

from tutorialpkg.week8_queries.create_query_db import create_db


@pytest.fixture
def db(scope='session'):
    """ Create a database with data for the paralympic tables.

    Note: this creates the database once for the session and deletes it after the session is finished.
    Change the scope to 'fixture' if you want to create a new database for each test function.
    """
    db_loc = Path(__file__).parent.parent.joinpath('tests', 'test_para_queries.db')
    data_loc = Path(__file__).parent.parent.joinpath('src', 'tutorialpkg', 'data_db_activity', 'paralympics_all.xlsx')
    con, cur = create_db(data_loc, db_loc)

    # Provide the connection and cursor to the tests
    yield con, cur

    # When the session is finished, close the cursor and connection and delete the database file
    con.close()
    if os.path.exists(db_loc):
        os.remove(db_loc)
    else:
        print(f"The database file {db_loc} does not exist.")
