"""Possible solutions to the activities in week 8.

There are more efficient ways to write some of these!

Each query is structured into a separate function.
You would not typically create such specific functions!
I have done this to provide functions to test in next week's tutorial.
"""

import sqlite3
from pathlib import Path


def get_db_con(db_path):
    """Returns a connection and cursor to the chinook database."""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('PRAGMA optimize = ON')
    con.commit()
    con.set_trace_callback(print)
    return con, cur


def execute_select_query(cursor, sql):
    """Executes a SQL SELECT query and returns the fetched rows as tuples or raises a sqlite3 exception."""
    try:
        cursor.execute(sql)
        return cursor.fetchall()
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


def select_sorted_disability(cursor, column, table_name, sort_order):
    """1. Query to find the disability categories sorted alphabetically."""
    sql = f"SELECT {column} FROM {table_name} ORDER BY {column} {sort_order};"
    return execute_select_query(cursor, sql)


def select_unique(cursor, column, table_name):
    """ 2. Query to find the unique values in a column of a table."""
    sql = f"SELECT DISTINCT {column} FROM {table_name};"
    return execute_select_query(cursor, sql)


def select_event_date_range(cursor, start, end):
    """3. Find the start and end dates of events that in years between 1960 and 1969."""
    sql = f"SELECT start, end FROM Event WHERE year BETWEEN {start} AND {end};"
    return execute_select_query(cursor, sql)


def select_limit(cursor, table, column, limit):
    """4. Find 5 country codes from the 'Host' table."""
    sql = f"SELECT {column} FROM {table} LIMIT {limit};"
    return execute_select_query(cursor, sql)


def select_groupby(cursor, table, group_column, count_column, id=None):
    """5. Find the event_id and number of teams in the MedalResult table for each Event.
    6. Find the event_id and number of teams in the MedalResult table for event with event_id 27.
    """
    if not id:
        sql = f'SELECT {group_column}, COUNT({count_column}) FROM {table} GROUP BY {group_column}'
    else:
        sql = (
            f'SELECT {group_column}, COUNT({count_column}) FROM {table} '
            f'WHERE {group_column} = {id} GROUP BY {group_column}'
        )
    return execute_select_query(cursor, sql)


def select_join_groupby(cursor):
    """7. the event name and number of teams in the MedalResult table for event with event_id 27."""
    sql = (
        'SELECT Host.host, COUNT(MedalResult.country_code) '
        'FROM MedalResult '
        'INNER JOIN Event on MedalResult.event_id = Event.event_id '
        'LEFT JOIN HostEvent on Event.event_id = HostEvent.event_id '
        'LEFT JOIN Host on Host.host_id = HostEvent.host_id '
        'WHERE Event.event_id = 27 '
        'GROUP BY Event.event_id;'
    )
    return execute_select_query(cursor, sql)


def select_event_participants_winter(cursor):
    """8. Find the year, host name, number of male participants and number of female participants in all winter games."""
    sql = (
        'SELECT e.year, h.host, p.participants_m, p.participants_f '
        'FROM Event AS e '
        'LEFT JOIN Participants AS p on e.event_id = p.event_id '
        'LEFT JOIN HostEvent AS he on e.event_id = he.event_id '
        'LEFT JOIN Host AS h on h.host_id = he.host_id '
        "WHERE e.type = 'winter';"
    )
    return execute_select_query(cursor, sql)


def select_faroe_results(cursor):
    """9. Find the year, event name, event type and rank where the Faroe Islands appear in the MedalResults."""
    sql = ('SELECT Country.name, Event.year, Event.type, Host.host, MedalResult.rank '
           'FROM Country '
           'LEFT JOIN MedalResult on Country.code = MedalResult.country_code '
           'LEFT JOIN Event on Event.event_id = MedalResult.event_id '
           'LEFT JOIN HostEvent on Event.event_id = HostEvent.event_id '
           'LEFT JOIN Host on Host.host_id = HostEvent.host_id '
           "WHERE Country.name == 'Faroe Islands';")
    return execute_select_query(cursor, sql)


def select_intellectual_ability_events(cursor):
    """
    10. Find the events that included the disability category 'Intellectual Disability' and sort alphabetically.
    """
    sql = (
        'SELECT h.host, e.year '
        'FROM Event AS e '
        'LEFT JOIN DisabilityEvent AS de on e.event_id = de.event_id '
        'LEFT JOIN Disability AS d on de.disability_id = d.disability_id '
        'LEFT JOIN HostEvent AS he on e.event_id = he.event_id '
        'LEFT JOIN Host AS h on he.host_id = h.host_id '
        "WHERE d.category == 'Intellectual Disability' "
        'ORDER BY h.host;'
    )
    return execute_select_query(cursor, sql)


if __name__ == '__main__':
    db_path_para_queries = Path(__file__).parent.parent.joinpath('data_db_activity', 'para_queries.db')
    con, cur = get_db_con(db_path_para_queries)

    # Print the SQL to the terminal
    con.set_trace_callback(print)

    # 1. Find all disability categories from the 'Disability' table and sort them in alphabetical order.
    print("\nQuestion 1: All categories from the 'Disability' table in alphabetical order:")
    result = select_sorted_disability(cur, column="category", table_name="Disability", sort_order="ASC")
    [print(row[0]) for row in result]

    # 2. Find the unique 'region' names from the 'Country' table.
    print("\nQuestion 2: Unique 'region' names from the 'Country' table:")
    result = select_unique(cursor=cur, column="region", table_name="Country")
    [print(row[0]) for row in result]

    # 3. Find the start and end dates of all events that occured in years between 1960 and 1969.
    print("\nQuestion 3: Start and end dates of all Events that occured in years between 1960 and 1969:")
    result = select_event_date_range(cur, start=1960, end=1969)
    [print(row) for row in result]

    # 4. Find 5 country codes from the 'Host' table.
    print("\nQuestion 4: 5 country codes from the 'Host' table:")
    result = select_limit(cur, table="Host", column="country_code", limit=5)
    [print(row[0]) for row in result]

    # 5. Find the event_id and number of teams in the MedalResult table for each Event.
    print("\nQuestion 5: The event_id and number of teams in the MedalResult table for each Event.")
    result = select_groupby(cursor=cur, table="MedalResult", group_column="event_id", count_column="country_code")
    [print(row) for row in result]

    # 6. Find the event_id and number of teams in the MedalResult table for event with event_id 27.
    print("\nQuestion 6: event_id and number of teams in the MedalResult table for event with event_id 27.")
    result = select_groupby(
        cursor=cur,
        table="MedalResult",
        group_column="event_id",
        count_column="country_code",
        id=27
    )
    [print(row) for row in result]

    # 7. Find the event name and number of teams in the MedalResult table for event with event_id 27.
    print("\nQuestion 7: Event name and number of teams in the MedalResult table for event with event_id 27.")
    result = select_join_groupby(cursor=cur)
    [print(row) for row in result]

    # 8. Find the year, host name, number of male participants and number of female participants in all winter games.
    print(
        "\n Question 8: The year, host name, number of male participants and number of female participants in all winter games.")
    result = select_event_participants_winter(cur)
    [print(row) for row in result]

    # 9. Find the year, event name, event type and rank for all events where the team from the Faroe Islands appear
    # in the MedalResults.
    print(
        "\nQuestion 9: Find the year, event name, event type and rank where the Faroe Islands appear in the MedalResults.")
    result = select_faroe_results(cur)
    [print(row) for row in result]

    # 10. Find the events that included the disability category 'Intellectual Disability' and sort them in alphabetical
    # order.
    print(
        "\nQuestion 10: Find the events that included the disability category 'Intellectual Disability' and sort alphabetically.")
    result = select_intellectual_ability_events(cur)
    [print(row) for row in result]

    con.close()
