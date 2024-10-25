import sqlite3
from pathlib import Path

from tutorialpkg.queries.tutorial8_select_queries import get_db_con


def run_chinook_delete_queries(connection, cursor):
    """Runs the DELETE queries on the chinook database."""

    # These all assume you ran the insert queries from the previous tutorial activity! If not please run
    # tutorialpkg/sample_code/tutorial8_insert_queries.py first.
    
    # 1. Delete all Artists where the Name is any of: New Artist 1, New Artist 2, New Artist 3, New Artist 4, New Artist 100
    try:
        # Print the artists before delete
        cursor.execute(
            "SELECT * FROM artists WHERE Name IN ('New Artist 1', 'New Artist 2', 'New Artist 3', 'New Artist 4', 'New Artist 100')")
        print(cursor.fetchall())
        # Delete the artists
        sql = "DELETE FROM artists WHERE Name IN ('New Artist 1', 'New Artist 2', 'New Artist 3', 'New Artist 4', 'New Artist 100')"
        cursor.execute(sql)
        # Print the artists after delete. This should return an empty list.
        cursor.execute(
            "SELECT * FROM artists WHERE Name IN ('New Artist 1', 'New Artist 2', 'New Artist 3', 'New Artist 4', 'New Artist 100')")
        print(cursor.fetchall())
        connection.commit()
    except sqlite3.Error as e:
        print(f"An sqlite3 error occurred: {e}")

    # 2. Delete all Albums where the title is New Album 100 or New Album 1
    try:
        # Print the albums before delete
        sql_select = "SELECT * FROM albums WHERE Title = 'New Album 1' OR 'New Album 100'"
        cursor.execute(sql_select)
        print(cursor.fetchall())
        # Delete the albums
        sql_delete = "DELETE FROM albums WHERE Title = 'New Album 1' OR 'New Album 100'"
        cursor.execute(sql_delete)
        # Print the albums after delete. This should return an empty list.
        cursor.execute(sql_select)
        print(cursor.fetchall())
        connection.commit()
    except sqlite3.Error as e:
        print(f"An sqlite3 error occurred: {e}")


if __name__ == '__main__':
    db_path_chinook = Path(__file__).parent.parent.joinpath('data_db_activity', 'chinook.db')
    ch_con, ch_cur = get_db_con(db_path_chinook)

    # Run the Chinook database DELETE queries
    run_chinook_delete_queries(ch_con, ch_cur)
    ch_con.close()

    # Use the para_queries database
    db_path_para_queries = Path(__file__).parent.parent.joinpath('data_db_activity', 'para_queries.db')
    pq_con, pq_cur = get_db_con(db_path_para_queries)

    # Write your own code for the following:
    # 1. Delete all rows in Quiz

    # 2. Delete all rows in Questions

    # 3. Delete all the answer choices for the questions

    # Close the connection to the para_queries database
    pq_con.close()
