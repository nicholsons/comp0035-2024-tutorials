import os
import sqlite3
from pathlib import Path

import pytest

from tutorialpkg.week8_queries import card_queries


# Placed here to illustrate that fixtures do not have to be in conftest.py
# This fixture is only used in this file
@pytest.fixture
def cards_db_con():
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


# The first 3 examples show tests that contain the queries

def test_deck_cards_has_suits(cards_db_con):
    """
    GIVEN a database with table called suit
    WHEN a cross join query is made
    THEN the result should contain Queen of Hearts
    """
    expected_card = ('Hearts', 'Queen')
    cur = cards_db_con.cursor()
    rows = cur.execute("SELECT suit, rank FROM ranks CROSS JOIN suits ORDER BY suit;")
    cards = []
    [cards.append(row) for row in rows]
    assert expected_card in cards


def test_deck_of_cards_contains_suits(cards_db_con):
    """
    GIVEN a database with table called suits
    WHEN a select all query is made to to get all suit in the suits table
    THEN the result should contain 'Clubs', 'Diamonds', 'Hearts', 'Spades'
    """
    expected_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    cur = cards_db_con.cursor()
    rows = cur.execute("SELECT suit FROM suits;")
    suits = []
    [suits.append(row[0]) for row in rows]
    for es in expected_suits:
        assert es in suits


# Test that you cannot add a new suit and leave the column 'suit' empty
def test_cannot_add_suit_empty(cards_db_con):
    """
    GIVEN a database with table called suits
    WHEN an insert query is made to add a new suit with an empty string
    THEN an IntegrityError should be raised with the message 'NOT NULL constraint failed: suits.suit'
    """
    cur = cards_db_con.cursor()
    with pytest.raises(sqlite3.IntegrityError):
        suit_name = None
        cur.execute("INSERT INTO suits (suit) VALUES (?);", (suit_name,))
        cards_db_con.commit()


# The next examples show tests that test functions that contain the queries
# A module called 'card_queries.py' contains the query functions
# This use of functions is not necessary, but it is done to illustrate how to test functions

# Add a new suit.
def test_add_suit(cards_db_con):
    """
    GIVEN a database with table called suits
    WHEN a new suit is added to the suits table
    THEN the row count in the table should increase by 1
    """
    cur = cards_db_con.cursor()
    # fetchone() returns a tuple with one element, we want the element so use [0]
    rows_start = cur.execute("SELECT COUNT(*) FROM suits;").fetchone()[0]
    # Call the function to add a suit
    card_queries.add_suit('Jokers', cards_db_con)
    rows_after = cur.execute("SELECT COUNT(*) FROM suits;").fetchone()[0]
    assert rows_after - rows_start == 1


# Delete a suit and check it no longer exists.
# This test assumes that the test before has run, this is not good practice you should not rely on the order of tests
# The test will fail if run on its own.

def test_delete_suit(cards_db_con):
    """
    GIVEN a database with table called suits
    WHEN a suit is deleted from the suits table
    THEN the row count in the table should decrease by 1
    """
    cur = cards_db_con.cursor()
    # fetchone() returns a tuple with one element, we want the element so use [0]
    rows_start = cur.execute("SELECT COUNT(*) FROM suits;").fetchone()[0]
    # Call the function to add a suit
    card_queries.add_suit('Jokers', cards_db_con)
    card_queries.delete_suit('Jokers', cards_db_con)
    rows_after = cur.execute("SELECT COUNT(*) FROM suits;").fetchone()[0]
    assert rows_start - rows_after == 1

# Update the ranks with rank=2 to 'Two'. There should be 1 row changed.
def test_update_rank(cards_db_con):
    """
    GIVEN a database with table called ranks
    WHEN the rank with rank=2 is updated to 'Two'
    THEN the number of rows updated should be 1
    """
    # Call the function to update the rank
    rows_updated = card_queries.update_rank(2, 'Two', cards_db_con)
    assert rows_updated == 4
