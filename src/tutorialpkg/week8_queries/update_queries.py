import sqlite3
from pathlib import Path

from tutorialpkg.queries.tutorial8_select_queries import get_db_con


def run_chinook_update_queries(connection, cursor):
    """Runs the UPDATE queries on the chinook database."""

    # These all assume you ran the insert queries from the previous tutorial activity!

    # 1. Change the artist name from New Artist 1 to New Artist 100 for all instances
    try:
        cursor.execute("UPDATE artists SET Name = 'New Artist 100' WHERE Name = 'New Artist 1';")
        connection.commit()
        cursor.execute("SELECT * FROM artists WHERE Name = 'New Artist 100';")
        print(cursor.fetchall())
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    # 2. Change the album title from New Album 1 to New Album 100 for all instances
    try:
        cursor.execute("UPDATE albums SET Title = 'New Album 100' WHERE Title = 'New Album 1';")
        connection.commit()
        cursor.execute("SELECT * FROM albums WHERE Title = 'New Album 100';")
        print(cursor.fetchall())
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    # 3. Change the ArtistId for the last album to be added to 3500
    # Should raise an integrity error since the ArtistId 3500 does not exist in the artists table
    try:
        last_album_id = cursor.execute('SELECT MAX(AlbumId) FROM albums;').fetchone()[0]
        cursor.execute('UPDATE albums SET ArtistId = 3500 WHERE AlbumId = ?;', (last_album_id,))
        connection.commit()
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


if __name__ == '__main__':
    db_path_chinook = Path(__file__).parent.parent.joinpath('data_db_activity', 'chinook.db')
    ch_con, ch_cur = get_db_con(db_path_chinook)

    # Run the Chinook database UPDATE queries
    run_chinook_update_queries(ch_con, ch_cur)
    ch_con.close()

    # Use the para_queries database
    db_path_para_queries = Path(__file__).parent.parent.joinpath('data_db_activity', 'para_queries.db')
    pq_con, pq_cur = get_db_con(db_path_para_queries)

    # Write your own code for the following:
    # 1. Update the Quiz name from "My first quiz" to "My first quiz updated"

    # 2. Update the question text for all questions to the value: "the same question text for all questions"

    # 3. Print all the rows from the QuizQuestion table.

    # Change the id of Quiz with quiz_id=1 to quiz_id=50.

    # Now print all the rows from the QuizQuestion table again.

    # Why has the quiz_id in the Question table changed when you only changed the Quiz table?

    # Close the connection to the para_queries database
    pq_con.close()
