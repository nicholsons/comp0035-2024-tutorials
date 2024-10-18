import sqlite3
from pathlib import Path

if __name__ == '__main__':

    # Connect to the database
    music_db_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'music.db').resolve()
    connection = sqlite3.connect(music_db_path)

    # Create the cursor object
    cursor = connection.cursor()

    # Enable support for foreign keys
    cursor.execute('PRAGMA foreign_keys = ON;')
    connection.commit()

    # Delete tables from the music database if they exist
    sql_drop_artist = 'DROP TABLE IF EXISTS artist;'
    sql_drop_track = 'DROP TABLE IF EXISTS track;'
    cursor.execute(sql_drop_artist)
    cursor.execute(sql_drop_track)
    connection.commit()

    # SQL to create the database
    sql_table_artist = '''CREATE TABLE artist(artist_id INTEGER PRIMARY KEY, artist_name TEXT NOT NULL);'''
    sql_table_track = '''CREATE TABLE track(track_id INTEGER PRIMARY KEY, track_name TEXT, artist_id INTEGER, 
                            FOREIGN KEY(artist_id) REFERENCES artist(artist_id) ON UPDATE CASCADE);'''
    # The following has a syntax error in the SQL query
    sql_table_track_error = '''CREATE TABL track(track_id INTEGER PRIMARY KEY, track_name TEXT, artist_id INTEGER, 
                            FOREIGN KEY(artist_id) REFERENCES artist(artist_id) ON UPDATE CASCADE);'''

    # SQL to insert artist data
    sql_artist_1 = 'INSERT INTO artist (artist_name) VALUES ("The Band");'
    sql_artist_2 = 'INSERT INTO artist VALUES (2, "Robert Plant");'
    sql_track_1 = 'INSERT INTO track VALUES (1, "Killing the blues",2);'

    # Handle the SQLite error if the query fails
    # Run it an you should get an error
    # Run again but add # before the table_track_error line and remove # from the line below
    try:
        cursor.execute(sql_table_artist)
        cursor.execute(sql_table_track_error)
        # cursor.execute(sql_table_track)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    connection.commit()

    # This should fail as the relationship is violated
    # Run again but remove the # from the second artist insert statement
    try:
        cursor.execute(sql_artist_1)
        # cursor.execute(sql_artist_2)
        cursor.execute(sql_track_1)
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    # As above but using the context manager
    try:
        with connection:
            cursor.execute(sql_artist_1)
            # cursor.execute(sql_artist_2)
            cursor.execute(sql_track_1)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
