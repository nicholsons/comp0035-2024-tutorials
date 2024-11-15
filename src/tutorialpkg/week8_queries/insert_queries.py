import sqlite3
from pathlib import Path

from tutorialpkg.queries.tutorial8_select_queries import get_db_con


def run_chinook_insert_queries(connection, cursor):
    """Runs the insert queries on the chinook database."""

    # 1. Insert 1 row into the artists table then print it
    # Insert the new artist using a parametrised query
    artist_name = "New Artist 1"  # This is a string
    cursor.execute('INSERT INTO artists (Name) VALUES (?);', (artist_name,))
    connection.commit()
    # Get the last inserted row id
    last_row_id = cursor.lastrowid
    # Select and then print the last inserted row
    cursor.execute('SELECT * FROM artists WHERE ArtistId = ?', (last_row_id,))
    print(cursor.fetchone())

    # 2. Insert 3 rows into the artist table and then print them
    values = [("New Artist 2",), ("New Artist 3",), ("New Artist 4",)]  # This is a list of tuples
    cursor.executemany('INSERT INTO artists (Name) VALUES (?);', values)
    connection.commit()
    # lastrowid can't be used for many inserts, instead select the last 3 rows
    cursor.execute('SELECT * FROM artists ORDER BY ArtistId DESC LIMIT 3')
    print(cursor.fetchall())

    # 3. Insert 1 row into the albums table where you know the ArtistId for Aerosmith then print it
    album = (3, "New Album 1")  # This is a tuple
    cursor.execute('INSERT INTO albums (ArtistId, Title) VALUES (?, ?);', album)
    connection.commit()
    last_row_id = cursor.lastrowid
    cursor.execute('SELECT * FROM artists WHERE ArtistId = ?', (last_row_id,))
    print(cursor.fetchone())

    # 4. Insert 1 row into the albums table where you do not know the ArtistId for Aerosmith then print it
    cursor.execute("SELECT ArtistId FROM artists WHERE Name = 'Aerosmith';")
    artist_id = cursor.fetchone()[0]
    album_values = (artist_id, "New Album 1")
    cursor.execute('INSERT INTO albums (ArtistId, Title) VALUES (?, ?);', album_values)
    connection.commit()
    last_row_id = cursor.lastrowid
    cursor.execute('SELECT * FROM albums WHERE AlbumId = ?', (last_row_id,))
    print(cursor.fetchone())

    # 5. Variant of 4 using a single SQL statement
    album_title = ("New Album 1",)
    sql = "INSERT INTO albums (ArtistId, Title) " \
          "SELECT ArtistId, ? " \
          "FROM artists " \
          "WHERE name = 'Aerosmith';"
    cursor.execute(sql, album_title)
    connection.commit()
    last_row_id = cursor.lastrowid
    cursor.execute('SELECT * FROM albums WHERE AlbumId = ?', (last_row_id,))
    print(cursor.fetchone())

    # 6. An insert that fails the validation constraint
    # General sqlite3 error
    try:
        cursor.execute("INSERT INTO albums (Title) VALUES ('New Album 1');")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    # More specific
    try:
        cursor.execute("INSERT INTO albums (Title) VALUES ('New Album 1');")
    except sqlite3.IntegrityError as e:
        print(f"An integrity error occurred: {e}")

    # Provide fallback for all errors
    try:
        cursor.execute("INSERT INTO albums (Title) VALUES ('New Album 1');")
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

    # Not appropriate for this case, so the error will not be handled and the code will stop
    try:
        cursor.execute("INSERT INTO albums (Title) VALUES ('New Album 1');")
    except sqlite3.DataError as e:
        print(f"A data error occurred: {e}")

    print("This will not print as the previous error is not handled")


if __name__ == '__main__':
    # Database file location
    db_path_chinook = Path(__file__).parent.parent.joinpath('data_db_activity', 'chinook.db')
    # Console and cursor for chinook database
    ch_con, ch_cur = get_db_con(db_path_chinook)

    # Run the Chinook database INSERT queries
    run_chinook_insert_queries(ch_con, ch_cur)

    # Close the connection
    ch_con.close()

    # Write your own queries for the following using the para_queries database
    db_path_para_queries = Path(__file__).parent.parent.joinpath('data_db_activity', 'para_queries.db')
    pq_con, pq_cur = get_db_con(db_path_para_queries)

    # Write your own code for the following:

    # 1. Insert a new Quiz with quiz_name value "My first quiz"

    # 2. Insert two new Questions for the Quiz you just entered.
    # text="text for question 1"
    # text="text for question 2"

    # 3. Insert three answer choices for one of the new questions.
    #  choice_text=""option a" choice_value="1" is_correct="1"
    #  choice_text=""option b" choice_value="0" is_correct="0"
    #  choice_text=""option c" choice_value="0" is_correct="0"

    # 4. An insert query that fails the validation constraint and raises an integrity error

    # Close the connection to the para_queries database
    pq_con.close()
