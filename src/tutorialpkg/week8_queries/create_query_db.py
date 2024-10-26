""" Version of the paralympics database for use in week 8 (queries) and 9 (unit testing)"""
import sqlite3
from pathlib import Path

import pandas as pd


def create_paralympics_db_structure(cursor, connection):
    """Create the paralympics database structure."""
    # Define the tables and relationships using SQL statements
    disability_sql = '''CREATE TABLE Disability (
                            disability_id INTEGER PRIMARY KEY,
                            category TEXT NOT NULL)'''

    country_sql = '''CREATE TABLE Country (
                    code TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    region TEXT,
                    sub_region TEXT,
                    member_type TEXT,
                    notes TEXT
                    )'''

    host_sql = '''CREATE TABLE Host (
                    host_id INTEGER PRIMARY KEY,
                    country_code TEXT NOT NULL,
                    host TEXT NOT NULL,
                    FOREIGN KEY (country_code) REFERENCES Country(code) ON DELETE CASCADE ON UPDATE CASCADE)'''

    event_sql = '''CREATE TABLE Event (
                    event_id INTEGER PRIMARY KEY,
                    type INTEGER NOT NULL,
                    year INTEGER NOT NULL,
                    start TEXT,
                    end TEXT,
                    countries INTEGER,
                    events INTEGER,
                    sports INTEGER,
                    highlights TEXT,
                    url TEXT
                )'''

    disability_event_sql = '''CREATE TABLE DisabilityEvent (
                            disability_id INTEGER,
                            event_id INTEGER,
                            PRIMARY KEY (disability_id, event_id),
                            FOREIGN KEY (disability_id) REFERENCES Disability(disability_id) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (event_id) REFERENCES Event(event_id) ON DELETE CASCADE ON UPDATE CASCADE)'''

    host_event_sql = '''CREATE TABLE HostEvent (
                            host_id TEXT NOT NULL,
                            event_id INTEGER NOT NULL,
                            PRIMARY KEY (host_id, event_id),
                            FOREIGN KEY (host_id) REFERENCES Host(host_id) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (event_id) REFERENCES Event(event_id) ON DELETE CASCADE ON UPDATE CASCADE
                    )'''

    participants_sql = '''CREATE TABLE Participants (
                    participant_id INTEGER PRIMARY KEY,
                    participants_m INTEGER,
                    participants_f INTEGER,
                    participants INTEGER,
                    event_id INTEGER,
                    FOREIGN KEY (event_id) REFERENCES Event(event_id) ON DELETE CASCADE ON UPDATE CASCADE

                )'''

    medal_result_sql = '''CREATE TABLE MedalResult (
                            result_id INTEGER PRIMARY KEY,
                            event_id INTEGER,
                            country_code TEXT,
                            rank INTEGER,
                            gold INTEGER,
                            silver INTEGER,
                            bronze INTEGER,
                            total INTEGER,
                            FOREIGN KEY (event_id) REFERENCES Event(event_id) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (country_code) REFERENCES Country(code) ON DELETE CASCADE ON UPDATE CASCADE)
                        '''

    question_sql = '''CREATE TABLE Question (
                        question_id INTEGER PRIMARY KEY,
                        question TEXT NOT NULL,
                        event_id INTEGER,
                        FOREIGN KEY (event_id) REFERENCES Event(event_id) ON DELETE CASCADE ON UPDATE CASCADE
                        )'''

    quiz_sql = '''CREATE TABLE Quiz (
                    quiz_id INTEGER PRIMARY KEY,
                    quiz_name TEXT NOT NULL,
                    close_date TEXT
                )'''

    answer_choice_sql = '''CREATE TABLE AnswerChoice (
                                ac_id INTEGER PRIMARY KEY,
                                question_id INTEGER NOT NULL,
                                choice_text TEXT NOT NULL,
                                choice_value INTEGER,
                                is_correct INTEGER,
                                FOREIGN KEY (question_id) REFERENCES Question(question_id) ON DELETE CASCADE ON UPDATE CASCADE
                        )'''

    quiz_question_sql = '''CREATE TABLE QuizQuestion (
                    question_id INTEGER,
                    quiz_id INTEGER,
                    PRIMARY KEY(question_id, quiz_id),
                    FOREIGN KEY (quiz_id) REFERENCES Quiz(quiz_id) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (question_id) REFERENCES Question(question_id) ON DELETE CASCADE ON UPDATE CASCADE
                    )'''

    student_response_sql = '''CREATE TABLE StudentResponse (
                            response_id INTEGER PRIMARY KEY,
                            student_email TEXT NOT NULL,
                            score INTEGER NOT NULL,
                            quiz_id INTEGER NOT NULL,
                            FOREIGN KEY (quiz_id) REFERENCES Quiz(quiz_id) ON DELETE CASCADE ON UPDATE CASCADE
                        )'''

    try:
        # Drop each table if they already exist
        cursor.execute('DROP TABLE IF EXISTS HostEvent;')
        cursor.execute('DROP TABLE IF EXISTS DisabilityEvent;')
        cursor.execute('DROP TABLE IF EXISTS Participants;')
        cursor.execute('DROP TABLE IF EXISTS MedalResult;')
        cursor.execute('DROP TABLE IF EXISTS Event;')
        cursor.execute('DROP TABLE IF EXISTS Host;')
        cursor.execute('DROP TABLE IF EXISTS Country;')
        cursor.execute('DROP TABLE IF EXISTS Disability;')
        cursor.execute('DROP TABLE IF EXISTS AnswerChoice;')
        cursor.execute('DROP TABLE IF EXISTS QuizQuestion;')
        cursor.execute('DROP TABLE IF EXISTS StudentResponse;')
        cursor.execute('DROP TABLE IF EXISTS Question;')
        cursor.execute('DROP TABLE IF EXISTS Quiz;')

        # Create the tables
        cursor.execute(country_sql)
        cursor.execute(host_sql)
        cursor.execute(event_sql)
        cursor.execute(participants_sql)
        cursor.execute(disability_sql)
        cursor.execute(host_event_sql)
        cursor.execute(disability_event_sql)
        cursor.execute(question_sql)
        cursor.execute(quiz_sql)
        cursor.execute(answer_choice_sql)
        cursor.execute(quiz_question_sql)
        cursor.execute(student_response_sql)
        cursor.execute(medal_result_sql)

        # Commit the changes
        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred creating the database. Error: {e}')
        if connection:
            connection.rollback()


def add_country_data(df, cursor, connection):
    """Add the country data to the paralympics database."""
    # Insert all values into the country table
    try:
        for index, row in df.iterrows():
            # The row is pandas series, we want the series as a list of values
            row_values = row.tolist()
            cursor.execute('INSERT INTO Country VALUES (?,?,?,?,?,?)', row_values)

        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred adding country data to the paralympics database. Error: {e}')
        if connection:
            connection.rollback()  # Rollback the changes on error


def add_event_data(df, cursor, connection):
    """Add event and participant data to the paralympics database."""
    try:
        # Convert the dates to strings
        df['start'] = df['start'].dt.strftime('%d/%m/%Y')
        df['end'] = df['end'].dt.strftime('%d/%m/%Y')

        # Insert the values into the event table
        for index, row in df.iterrows():
            values = (
                row['type'],
                row['year'],
                str(row['start']),
                str(row['end']),
                row['countries'],
                row['events'],
                row['sports'],
                row['highlights'],
                row['url'])
            cursor.execute(
                f'INSERT INTO Event (type, year, start, end, countries, events, sports, highlights, url) VALUES (?, ? , ?, ?, ?, ?, ?, ?, ?)',
                values)
            # insert the participants data
            event_id = cursor.lastrowid
            participant_values = (
                event_id,
                row['participants_m'],
                row['participants_f'],
                row['participants'],
            )
            sql_ins_part = 'INSERT INTO Participants (event_id, participants_m, participants_f, participants) VALUES (?, ?, ?, ?)'
            cursor.execute(sql_ins_part, participant_values)

        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred adding event data to the paralympics database. Error: {e}')
        if connection:
            connection.rollback()


def add_host_data(df_events, cursor, connection):
    """Add data to the normalised paralympics database."""

    try:
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
            select_sql = f'SELECT code from Country where name="{country_name}"'
            result = cursor.execute(select_sql).fetchone()
            country_code = result[0]
            # Insert into the host table
            host = row['host']
            cursor.execute('INSERT INTO Host (country_code, host) VALUES (?, ?)', (country_code, host))

        # Commit the changes
        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred adding host data to the paralympics database. Error: {e}')
        if connection:
            connection.rollback()  # Rollback the changes on error


def add_host_event_data(df, cursor, connection):
    """Add HostEvent data to the paralympics database."""

    try:
        # Iterate each event, find the pairs of hosts, then get the event_id and host_id and insert into the host_event table
        for index, row in df.iterrows():
            hosts = row['host'].split(',')
            # Find the event id for the event. This matches based on the year and type of event.
            event_id = cursor.execute(
                'SELECT event_id FROM Event WHERE year = ? AND type = ?',
                (row['year'], row['type'])
            ).fetchone()[0]
            # Find the host_id for each host
            for host in hosts:
                host_id = cursor.execute(f'SELECT host_id FROM Host WHERE host = "{host.strip()}"').fetchall()[0][0]
                # Insert the host_event pair
                cursor.execute('INSERT INTO HostEvent (host_id, event_id) VALUES (?, ?)', (host_id, event_id))

        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred adding HostEvent data to the paralympics database. Error: {e}')
        if connection:
            connection.rollback()


def add_disabilities_data(df, cursor, connection):
    """Add Disability and DisabilityEvent data."""

    try:
        # Split the comma-separated values into lists
        split_disabilities = df['disabilities'].str.split(', ')
        # Flatten the list of lists into a single list
        all_disabilities = [item for sublist in split_disabilities for item in sublist]
        # Convert the list to a set to get unique values
        unique_disabilities = set(all_disabilities)
        # Insert the unique values into the table
        for d in unique_disabilities:
            cursor.execute('INSERT INTO Disability (category) VALUES (?)', (d,))
        connection.commit()

        # Iterate each result row in the event table
        for index, row in df.iterrows():
            # find the event_id
            event_id = cursor.execute('SELECT event_id FROM Event WHERE year = ? AND type = ?',
                                      (row['year'], row['type'])).fetchone()[0]
            # split the values for the disabilities
            disabilities = row['disabilities'].split(', ')
            # add each diability
            for d in disabilities:
                # find the disability_id.
                disability_id = cursor.execute(
                    'SELECT disability_id FROM Disability WHERE category LIKE ?', (d,)
                ).fetchone()[0]
                # Insert into the DisabilityEvent table
                cursor.execute('INSERT INTO DisabilityEvent (event_id, disability_id) VALUES (?, ?)',
                               (event_id, disability_id))

        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred adding Disability data to the paralympics database. Error: {e}')
        if connection:
            connection.rollback()


def add_medal_result_data(df, cursor, connection):
    """Add MedalResult data to the paralympics database."""

    try:
        # Iterate each result row, get the event_id and code and insert into the MedalResult table
        for index, row in df.iterrows():
            # Find the event id for the event. This matches based on the year and type of event.
            qry = f'SELECT event_id FROM Event WHERE year = {row['Year']}'
            event_id = cursor.execute(qry).fetchone()[0]
            # Insert the medal results
            values = (event_id, row['NPC'], row['Rank'], row['Gold'], row['Silver'], row['Bronze'], row['Total'])
            sql = 'INSERT INTO MedalResult (event_id, country_code, rank, gold, silver, bronze, total) VALUES (?, ?, ?, ?, ?, ?, ?)'
            cursor.execute(sql, values)

        connection.commit()

    except sqlite3.Error as e:
        print(f'An error occurred adding MedalResult data. Error: {e}')
        if connection:
            connection.rollback()


def create_db(data_path, db_path, empty=False):
    """Creates a database in the specified directory.

    Parameters
    ----------
    data_path : Path to the excel file with the data
    db_path : Path to the database file
    empty : Boolean  If True then create a database with no rows. Default is False.
    """

    # Create a connection to the database, create a cursor, and enable foreign key support
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    conn.commit()

    # Create the structure
    create_paralympics_db_structure(cur, conn)

    if not empty:
        # Read data and create pandas dataframes
        events_df = pd.read_excel(data_path, sheet_name='events')
        medals_df = pd.read_excel(data_path, sheet_name='medal_standings')
        npc_df = pd.read_excel(data_path, sheet_name='npc_codes')

        # add data to the tables
        add_country_data(npc_df, cur, conn)
        add_host_data(events_df, cur, conn)
        add_event_data(events_df, cur, conn)
        add_host_event_data(events_df, cur, conn)
        add_disabilities_data(events_df, cur, conn)
        add_medal_result_data(medals_df, cur, conn)

    return cur, conn


def create_paralympics_query_db():
    """Create the paralympics query database."""
    db_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'para_queries.db')
    data_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'paralympics_all.xlsx')
    create_db(data_path, db_path)
