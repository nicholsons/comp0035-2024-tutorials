import sqlite3
from pathlib import Path


def get_db_con(db_path):
    """Returns a connection and cursor to the chinook database.

    Returns:
        tuple: A tuple containing the connection and cursor objects.
    """
    # Create a SQL connection the SQLite database and a cursor

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Enable foreign key constraint enforcement for INSERT, UPDATE, and DELETE operations.
    cur.execute('PRAGMA foreign_keys = ON;')
    con.commit()
    return con, cur


def run_chinook_select_queries(con, cur):
    """Runs the select queries on the chinook database."""

    # 1. SELECT Name from artists ORDER BY Name DESC;
    rows = cur.execute('SELECT Name FROM artists ORDER BY Name DESC;').fetchall()
    print("Artists name in descending order:")
    [print(row) for row in rows]

    # 2. SELECT DISTINCT: Find all the uniques job titles from the employees table.
    rows = cur.execute('SELECT DISTINCT Title FROM employees;').fetchall()
    print("Unique job titles from the table `employees`:")
    [print(row) for row in rows]

    # 3. WHERE: Find all album names that include the words 'Dark' or 'Black'
    rows = cur.execute(
        "SELECT albums.Title from albums WHERE Title LIKE '%Dark%' OR Title LIKE '%Black%';").fetchall()
    print("Album names that include the words 'Dark' or 'Black':")
    [print(row) for row in rows]

    # 4. LIMIT: Find 3 of the customer first and last names from the customers table
    # SELECT FirstName, LastName from customers LIMIT 3;
    rows = cur.execute("SELECT FirstName, LastName from customers LIMIT 3;").fetchall()
    print("3 of the customer first and last names from the customers table:")
    [print(row) for row in rows]

    # 5. GROUP BY: Find the album id and the number of tracks per album.
    rows = cur.execute("SELECT albumid, COUNT(trackid) FROM tracks GROUP BY albumid;").fetchall()
    print("Album id and the number of tracks per album:")
    [print(row) for row in rows]

    # 6.HAVING: Find the numbers of tracks for the album with id 1
    rows = cur.execute("SELECT albumid, COUNT(trackid) FROM tracks GROUP BY albumid HAVING albumid = 1;").fetchall()
    print("Number of tracks for the album with id 1:")
    [print(row) for row in rows]


def run_chinook_select_join_queries(con, cur):
    """Runs the select queries that use joins on the chinook database."""

    # 7. LEFT JOIN: Find the artists who do not have any albums
    rows = cur.execute('SELECT artists.Name, AlbumId '
                       'FROM artists '
                       'LEFT JOIN albums ON albums.ArtistId = artists.ArtistId '
                       'WHERE AlbumId IS NULL;').fetchall()
    print("\nArtists who do not have any albums:")
    [print(row) for row in rows]

    # Add a second join to get the artist name

    # 8. INNER JOIN: Find all track names, album and artist name
    # One track belongs to one album and one album have many tracks.
    # The tracks table associated with the albums table via albumid column.
    # One album belongs to one artist and one artist has one or many albums.
    # The albums table links to the artists table via artistid column.
    rows = cur.execute("SELECT tracks.name AS track, albums.title AS album, artists.name AS artist "
                       "FROM tracks "
                       "INNER JOIN albums ON albums.albumid = tracks.albumid "
                       "INNER JOIN artists ON artists.artistid = albums.artistid "
                       "WHERE artists.name LIKE 'Z%'").fetchall()
    print("\nTrack names, album and artist name:")
    [print(row) for row in rows]

    # 9. CROSS JOIN returns the cartesian product. I could not think of a meaningful example from chinook so the
    # example is from the SQLIte tutorial
    # Use CROSS JOIN to create a deck of cards.
    # Create two tables ranks and suits and populate them with the values.

    cur.execute("CREATE TABLE IF NOT EXISTS ranks (rank_id INTEGER PRIMARY KEY AUTOINCREMENT, rank TEXT NOT NULL);")
    cur.execute("CREATE TABLE IF NOT EXISTS suits (suit_id INTEGER PRIMARY KEY AUTOINCREMENT, suit TEXT NOT NULL);")
    suit_values = [('Clubs',), ('Diamonds',), ('Hearts',), ('Spades',)]
    rank_values = [(2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), ('Jack',), ('Queen',), ('King',), ('Ace',)]
    cur.executemany("INSERT INTO ranks (rank) VALUES (?)", rank_values)
    cur.executemany("INSERT INTO suits (suit) VALUES (?)", suit_values)
    con.commit()

    # Query to create a deck of cards
    rows = cur.execute("SELECT suit, rank FROM ranks CROSS JOIN suits ORDER BY suit;")
    print("\nDeck of cards:")
    [print(row) for row in rows]

    # Remove the tables
    cur.execute("DROP TABLE IF EXISTS ranks;")
    cur.execute("DROP TABLE IF EXISTS suits;")


if __name__ == '__main__':
    # Database file locations
    db_path_chinook = Path(__file__).parent.parent.joinpath('data_db_activity', 'chinook.db')
    # Console and cursor for chinook database
    ch_con, ch_cur = get_db_con(db_path_chinook)

    # Chinook database select queries
    # run_chinook_select_queries(ch_con, ch_cur)

    # Chinook database select queries with join
    run_chinook_select_join_queries(ch_con, ch_cur)

    # Close the connection
    ch_con.close()

    # Write your own queries for the following using the para_queries database
    db_path_para_queries = Path(__file__).parent.parent.joinpath('data_db_activity', 'para_queries.db')
    pq_con, pq_cur = get_db_con(db_path_para_queries)

    # 1. Find all disability categories from the 'Disability' table and sort them in alphabetical order.

    # 2. Find the unique 'region' names from the 'Country' table.

    # 3. Find the start and end dates of all events that occured in years between 1960 and 1969.

    # 4. Find 5 country codes from the 'Host' table.

    # 5. Find the event_id and number of teams in the MedalResult table for each Event.

    # 6. Find the event_id and number of teams in the MedalResult table for event with event_id 27.

    # 7. Find the event name and number of teams in the MedalResult table for event with event_id 27.

    # 8. Find the year, host name, number of male participants and number of female participants in all winter games.

    # 9. Find the year, event name, event type and rank for all events where the team from the Faroe Islands appear
    # in the MedalResults.

    # 10. Find the events that included the disability category 'Intellectual Disability' and sort them in alphabetical
    # order.

    # Close the connection to the para_queries database
    pq_con.close()
