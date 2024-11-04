""" Activity 5.7: Creating the paralympics database from a pandas dataframe with sqlite3 and pandas"""
import sqlite3
from pathlib import Path

import pandas as pd


# This is the same function as for the student database.
def create_not_normalised_db(df, db_path, table_name):
    """Create a database from a pandas dataframe without normalising the data.

    Creates a database using all columns in a single table.

    Args:
        df (pd.DataFrame): The pandas dataframe to be saved to the database.
        db_path (Path): The name and location of the database file.
        table_name (str): The name of the table to be created in the database.

    Returns:
        None
    """
    # Create a connection to the database using sqlite3.
    conn = sqlite3.connect(db_path)

    # Save the dataframe to the database, this will create a table called 'enrollments' and replace it if
    # it exists. The index column is not saved to the table.
    # If the file does not exist then it will be created.
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection.
    conn.close()


def create_paralympics_db_structure(db_path):
    """
    Create the normalised paralympics database structure only.

    Args:
        db_path (Path): The name and location of the database file.

    Returns:
       None

    """
    # Define the tables and relationships between the tables using SQL statements
    country_sql = '''CREATE TABLE country (code TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    region TEXT,
                    sub_region TEXT,
                    member_type TEXT,
                    notes TEXT)'''

    host_sql = '''CREATE TABLE host (host_id INTEGER PRIMARY KEY,
                country_code TEXT NOT NULL,
                host TEXT NOT NULL,
                FOREIGN KEY (country_code) REFERENCES country(code) ON DELETE CASCADE ON UPDATE CASCADE)'''

    event_sql = '''CREATE TABLE event (
                    event_id INTEGER PRIMARY KEY,
                    type INTEGER NOT NULL,
                    year INTEGER NOT NULL,
                    start TEXT,
                    end TEXT,
                    disabilities TEXT,
                    countries INTEGER,
                    events INTEGER,
                    sports INTEGER,
                    participants_m INTEGER,
                    participants_f INTEGER,
                    participants INTEGER,
                    highlights TEXT,
                    url TEXT
                )'''

    host_event_sql = '''CREATE TABLE host_event (
                            host_event_id INTEGER PRIMARY KEY,
                            host_id TEXT NOT NULL,
                            event_id INTEGER NOT NULL,
                            FOREIGN KEY (host_id) REFERENCES host(host_id) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE ON UPDATE CASCADE
                    )'''

    try:
        # Create a connection to the database using sqlite3
        connection = sqlite3.connect(db_path)

        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()

        # Enable foreign key constraints for sqlite
        # By default, foreign key constraints are disabled in SQLite, enable them for each database connection.
        cursor.execute('PRAGMA foreign_keys = ON;')

        # Commit the changes
        connection.commit()

        # Drop each table individually if they already exist
        cursor.execute('DROP TABLE IF EXISTS host_event;')
        cursor.execute('DROP TABLE IF EXISTS event;')
        cursor.execute('DROP TABLE IF EXISTS host;')
        cursor.execute('DROP TABLE IF EXISTS country;')

        # Create the tables in the database by executing the SQL statements and then commit the changes to the database
        # The order is important, you cannot create a child table before the parent table where there are relationships.

        cursor.execute(country_sql)
        cursor.execute(host_sql)
        cursor.execute(event_sql)
        cursor.execute(host_event_sql)

        # Commit the changes
        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred creating the database. Error: {e}')
        if connection:
            connection.rollback()  # Rollback the changes on error
    finally:
        if connection:
            # Close the connection.
            connection.close()


def add_country_data(df, db_path):
    """
    Add the country data to the normalised paralympics database.

    Args:
        df (pd.DataFrame): The pandas dataframe with NPC country codes.
        db_path (Path): The name and location of the database file.

    Returns:
       None

    """

    try:
        # Create a connection to the database using sqlite3
        connection = sqlite3.connect(db_path)

        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()

        # Enable foreign key constraints for sqlite
        # By default, foreign key constraints are disabled in SQLite, enable them for each database connection.
        cursor.execute('PRAGMA foreign_keys = ON;')

        # Commit the changes
        connection.commit()

        # Insert values into the country table, this only works if the table columns match the dataframe column names!
        # df.to_sql('country', connection, if_exists='append', index=False)

        # Alternative way to insert the values into the country table.
        for index, row in df.iterrows():
            # The row is pandas series, we want the series as a list of values
            row_values = row.tolist()
            cursor.execute('INSERT INTO country VALUES (?,?,?,?,?,?)', row_values)

        # Commit the changes
        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred adding country data to the paralympics database. Error: {e}')
        if connection:
            connection.rollback()  # Rollback the changes on error
    finally:
        if connection:
            connection.close()  # Close the connection.


def add_event_data(df, db_path):
    """
    Add event data to the normalised paralympics database.

    Args:
        df (pd.DataFrame): The pandas dataframe with event data.
        db_path (Path): The name and location of the database file.

    Returns:
       None

    """
    # Create a connection to the database using sqlite3
    connection = sqlite3.connect(db_path)
    try:
        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()

        # Enable foreign key constraints for sqlite
        # By default, foreign key constraints are disabled in SQLite, enable them for each database connection.
        cursor.execute('PRAGMA foreign_keys = ON;')

        # Commit the changes
        connection.commit()

        # Convert the dates to strings
        df['start'] = df['start'].dt.strftime('%d/%m/%Y')
        df['end'] = df['end'].dt.strftime('%d/%m/%Y')

        # Insert the values into the event table
        for index, row in df.iterrows():
            columns = "type, year, start, end, disabilities, countries, events, sports, participants_m, participants_f, participants, highlights, url"
            values = (
                row['type'],
                row['year'],
                str(row['start']),
                str(row['end']),
                row['disabilities'],
                row['countries'],
                row['events'],
                row['sports'],
                row['participants_m'],
                row['participants_f'],
                row['participants'],
                row['highlights'],
                row['url'])
            cursor.execute(f'INSERT INTO event ({columns}) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', values)

        # Commit the changes
        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred adding event data to the paralympics database. Error: {e}')
        if connection:
            connection.rollback()  # Rollback the changes on error
    finally:
        if connection:
            connection.close()  # Close the connection.


def add_host_data(df_events, db_path):
    """
    Add data to the normalised paralympics database.

    Activity 5.5 part 2.

    Args:
        df_events (pd.DataFrame): The pandas dataframe with event data.
        db_path (Path): The name and location of the database file.

    Returns:
       host_country_df (pd.DataFrame): The DataFrame with the host and country pairs and the host_id

    """
    # Create a connection to the database using sqlite3
    connection = sqlite3.connect(db_path)
    try:

        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()

        # Enable foreign key constraints for sqlite
        # By default, foreign key constraints are disabled in SQLite, enable them for each database connection.
        cursor.execute('PRAGMA foreign_keys = ON;')

        # Commit the changes
        connection.commit()

        # Extract unique host and country pairs
        # Initialize an empty DataFrame with the columns needed
        host_country_df = pd.DataFrame(columns=['host', 'country'])
        # Iterate over each row in the events DataFrame and split each column into multiple values where there is ','
        for index, row in df_events.iterrows():
            hosts = row['host'].split(',')
            countries = row['country'].split(',')
            # Create pairs of each host with each country and append to the DataFrame
            for host, country in zip(hosts, countries):
                new_row = pd.DataFrame({'host': [host.strip()], 'country': [country.strip()]})
                host_country_df = pd.concat([host_country_df, new_row], ignore_index=True)
        # Remove duplicate hosts from the dataframe
        host_country_df = host_country_df.drop_duplicates(subset=['host', 'country'])

        # Iterate over the dataframe, add the host and country to the host table
        for index, row in host_country_df.iterrows():
            # Get the country code from the country table
            country_name = row['country']
            select_sql = f'SELECT code from country where name="{country_name}"'
            result = cursor.execute(select_sql).fetchone()
            country_code = result[0]
            # Insert into the host table
            host = row['host']
            cursor.execute('INSERT INTO host (country_code, host) VALUES (?, ?)', (country_code, host))

        # Commit the changes
        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred adding host data to the paralympics database. Error: {e}')
        if connection:
            connection.rollback()  # Rollback the changes on error
    finally:
        if connection:
            connection.close()  # Close the connection.


def add_host_event_data(df, db_path):
    """
    Add host_event data to the normalised paralympics database.

    Activity 5.5 part 2.

    Args:
        df (pd.DataFrame): The pandas dataframe with the event data.
        db_path (Path): The name and location of the database file.

    Returns:
       None

    """

    try:
        # Create a connection to the database using sqlite3
        connection = sqlite3.connect(db_path)

        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()

        # Enable foreign key constraints for sqlite
        # By default, foreign key constraints are disabled in SQLite, enable them for each database connection.
        cursor.execute('PRAGMA foreign_keys = ON;')

        # Commit the changes
        connection.commit()

        # Iterate each event, find the pairs of hosts, then get the event_id and host_id and insert into the host_event table
        for index, row in df.iterrows():
            hosts = row['host'].split(',')
            # Find the event id for the event. This matches based on the year and type of event.
            event_id = cursor.execute('SELECT event_id FROM event WHERE year = ? AND type = ?',
                                      (row['year'], row['type'])).fetchone()[0]
            # Find the host_id for each host
            for host in hosts:
                host_id = cursor.execute(f'SELECT host_id FROM host WHERE host = "{host.strip()}"').fetchall()[0][0]
                # Insert the host_event pair
                cursor.execute('INSERT INTO host_event (host_id, event_id) VALUES (?, ?)', (host_id, event_id))

        # Commit the changes
        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred adding host_event data to the paralympics database. Error: {e}')
        if connection:
            connection.rollback()  # Rollback the changes on error
    finally:
        if connection:
            connection.close()  # Close the connection.


if __name__ == '__main__':
    # Activity: Create a database from the pandas dataframe without normalising
    data_file_csv = Path(__file__).parent.parent.joinpath('data_db_activity', 'paralympics_events.csv')
    db_file_un = Path(__file__).parent.parent.joinpath('data_db_activity', 'paralympics_not_normalised.db')
    df_para = pd.read_csv(data_file_csv)
    name_table = 'event'
    create_not_normalised_db(df_para, db_file_un, name_table)

    # Activity: Create a normalised database and add the data to the tables
    data_file_xlsx = Path(__file__).parent.parent.joinpath('data_db_activity', 'paralympics_all.xlsx')
    db_file_norm = Path(__file__).parent.parent.joinpath('data_db_activity', 'paralympics_normalised.db')
    events_df = pd.read_excel(data_file_xlsx, sheet_name='events')
    npc_df = pd.read_excel(data_file_xlsx, sheet_name='npc_codes')
    # Create the normalised database structure
    create_paralympics_db_structure(db_file_norm)
    # Adding data is in a series of functions to isolate the different parts of the process
    add_country_data(npc_df, db_file_norm)
    add_host_data(events_df, db_file_norm)
    add_event_data(events_df, db_file_norm)
    add_host_event_data(events_df, db_file_norm)

    # TODO: the disabilities column in the event table has multiple values in it so is not in 1NF.