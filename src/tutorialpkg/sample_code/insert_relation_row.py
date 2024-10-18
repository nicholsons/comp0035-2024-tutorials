"""
Example of adding a row to table in the database which has a foreign key relation.
"""
import sqlite3
from pathlib import Path

if __name__ == '__main__':
    # Connect to the database
    music_db_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'music.db').resolve()
    con = sqlite3.connect(music_db_path)

    # Create the cursor object
    cur = con.cursor()

    # Enable support for foreign keys
    cur.execute('PRAGMA foreign_keys = ON;')
    con.commit()

    # Delete tables from the music database if they exist
    sql_drop_artist = 'DROP TABLE IF EXISTS artist;'
    sql_drop_track = 'DROP TABLE IF EXISTS track;'
    cur.execute(sql_drop_artist)
    cur.execute(sql_drop_track)
    con.commit()

    # Create the tables
    sql_table_artist = '''CREATE TABLE artist(artist_id INTEGER PRIMARY KEY, artist_name TEXT NOT NULL);'''
    sql_table_track = '''CREATE TABLE track(track_id INTEGER PRIMARY KEY, track_name TEXT, artist_id INTEGER, 
                            FOREIGN KEY(artist_id) REFERENCES artist(artist_id) ON UPDATE CASCADE);'''

    cur.execute(sql_table_artist)
    cur.execute(sql_table_track)
    con.commit()

    # data
    artist_dict = [{"name": 'Led Zeppelin'}, {"name": 'Robert Plant'}, {"name": 'Alison Krauss'}]
    track_data = [{"artist": 'Led Zeppelin', "track_title": "Stairway to Heaven"},
                  {"artist": 'Alison Krauss', "track_title": "Let your loss be your lesson"},
                  {"artist": 'Alison Krauss', "track_title": "Your long journey"}]

    # Insert data into the artist table, there is no FK constraint in this table
    cur.executemany('INSERT INTO artist(artist_name) VALUES (:name)', artist_dict)
    con.commit()

    # Insert data into the track table, there is a FK constraint in this table
    # For each row of data
    for track in track_data:
        # Query the artist_id from the artist table, the result is a tuple
        result = cur.execute('SELECT artist_id FROM artist WHERE artist_name = :artist', track)
        # Fetch the artist_id which is the first value of the first row in the result
        artist_id = result.fetchone()[0]
        # Now insert the track data into the track table with the artist_id
        # cur.execute('INSERT INTO track(track_name, artist_id) VALUES (:track_title, :artist_id)', {"track_title": track["track"], "artist_id": artist_id})
        cur.execute('INSERT INTO track(track_name, artist_id) VALUES (?, ?)', (track['track_title'], artist_id))

    con.commit()
