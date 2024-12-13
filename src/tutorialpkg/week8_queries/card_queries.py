import sqlite3
from pathlib import Path

card_db_location = Path(__file__).parent.parent.joinpath('data_db_activity', 'cards.db')


def card_db():
    """
    Create a database with suits and ranks and yields a sqlite3 connection to the database.

    Returns:
        sqlite3.Connection: Connection to the database
    """
    con = sqlite3.connect('cards.db')
    cur = con.cursor()
    # Create the tables
    rank_table = '''CREATE TABLE IF NOT EXISTS ranks (
                    rank_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    rank TEXT NOT NULL);'''
    suits_table = '''CREATE TABLE IF NOT EXISTS suits (
                    suit_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    suit TEXT NOT NULL
                    );'''
    # check ( suit in ('Diamonds', 'Clubs', 'Hearts', 'Spades')
    cur.execute(rank_table)
    cur.execute(suits_table)
    # Add the data to the tables
    suit_values = [('Clubs',), ('Diamonds',), ('Hearts',), ('Spades',)]
    rank_values = [(2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), ('Jack',), ('Queen',), ('King',), ('Ace',)]
    cur.executemany("INSERT INTO ranks (rank) VALUES (?)", rank_values)
    cur.executemany("INSERT INTO suits (suit) VALUES (?)", suit_values)
    con.commit()
    return con


def create_deck(con):
    """
    Create a deck of cards using a cross join query.
    Args:
        con: Takes a sqlite3 connection object to the cards database

    Returns:
        deck: A sqlite3.Cursor result object with the deck of cards (suit, rank)
    """
    cur = con.cursor()
    deck = cur.execute("SELECT suit, rank FROM ranks CROSS JOIN suits ORDER BY suit;")
    return deck


def add_suit(suit_name, connection):
    """
    Add a suit to the suits table in the cards database.
    Args:
        suit_name: A string with the name of the suit to be added
        connection: A sqlite3 connection object to the cards database
    """
    cur = connection.cursor()
    try:
        cur.execute("INSERT INTO suits (suit) VALUES (?)", (suit_name,))
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(f"Suit already exists in the database or a Null value was given. {e}")


def delete_suit(suit_name, connection):
    """
    Delete a suit from the suits table in the cards database.
    Args:
        suit_name: A string with the name of the suit to be deleted
        connection: A sqlite3 connection object to the cards database
    """
    cur = connection.cursor()
    cur.execute("DELETE FROM suits WHERE suit = ?", (suit_name,))
    connection.commit()


def update_rank(current_rank, new_rank, connection):
    """
    Update the rank of a card in the ranks table in the cards database and returns the number of affected rows.
    Args:
        current_rank: A string with the name of the rank to be updated
        new_rank: A string with the new rank name
        connection: A sqlite3 connection object to the cards database
    Returns:
        int: The number of rows updated
    """
    cur = connection.cursor()
    rows_updated = cur.execute("UPDATE ranks SET rank = ? WHERE rank = ?", (new_rank, current_rank)).rowcount
    connection.commit()
    return rows_updated
