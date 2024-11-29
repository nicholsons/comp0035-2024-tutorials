"""Possible solutions to the activities in week 8 INSERT queries.

Each query is structured into a separate function.
You would not typically create such query specific functions!
I have done this to provide functions to test in next week's tutorial.
"""

from pathlib import Path
import sqlite3


def get_db_con(db_path):
    """Returns a connection and cursor to the chinook database."""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    con.commit()
    # con.set_trace_callback(print)
    return con, cur


def execute_insert_query(cursor, connection, sql, values, type=0):
    """Executes a SQL INSERT query.

      Returns the last inserted row if for a single row insert, a string message for many row insert, or raises a sqlite3 exception.
    """
    try:
        if type == 1:
            cursor.execute(sql, values)
            connection.commit()
            return cursor.lastrowid
        else:
            cursor.executemany(sql, values)
            connection.commit()
            return "Multiple rows inserted successfully"
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


def insert_quiz(cursor, connection):
    """1. Insert a new Quiz with quiz_name value 'My first quiz'."""
    vals = ("My first quiz",)
    sql_stmt = "INSERT INTO Quiz (quiz_name) VALUES (?);"
    # For execute() type=1
    return execute_insert_query(cursor, connection, sql=sql_stmt, values=vals, type=1)


def insert_questions(cursor, connection, quiz_id):
    """2. Insert two new Questions for the Quiz you just entered."""
    q_text = [("text for question 1",), ("text for question 2",)]
    for qt in q_text:
        sql_q = "INSERT INTO Question (question) VALUES (?);"
        quest_id = execute_insert_query(cursor, connection, sql=sql_q, values=qt, type=1)
        qq_vals = (quiz_id, quest_id)
        sql_qq = "INSERT INTO QuizQuestion (quiz_id, question_id) VALUES (?, ?);"
        ins_id = execute_insert_query(cursor, connection, sql=sql_qq, values=qq_vals, type=1)
    return ins_id


def insert_answer_choices(cursor, connection, question_id):
    """ 3. Insert three answer choices for one of the new questions."""
    choices = [(question_id, "option a", 1, 1),
               (question_id, "option b", 0, 0),
               (question_id, "option c", 0, -0)]
    sql_stmt = "INSERT INTO AnswerChoice (question_id, choice_text, choice_value, is_correct) VALUES (?, ?, ?, ?);"
    # For executemany() type=0
    return execute_insert_query(cursor, connection, sql=sql_stmt, values=choices, type=0)


if __name__ == '__main__':
    db_path_para_queries = Path(__file__).parent.parent.joinpath('data_db_activity', 'para_queries.db')
    con, cur = get_db_con(db_path_para_queries)

    # 1. Insert a new Quiz with quiz_name value "My first quiz"
    insert_id = insert_quiz(cur, con)
    print("\nInserted a new Quiz with id:")
    print(insert_id)

    # 2. Insert two new Questions for the Quiz you just entered.
    # text="text for question 1"
    # text="text for question 2"
    question_id = insert_questions(cur, con, insert_id)
    print(f"\nInsert two new Questions for the Quiz with id {insert_id}. Last inserted question id:")
    print(question_id)

    # 3. Insert three answer choices for one of the new questions.
    #  choice_text="option a", choice_value="1", is_correct="1"
    #  choice_text="option b", choice_value="0", is_correct="0"
    #  choice_text="option c", choice_value="0", is_correct="0"
    msg = insert_answer_choices(cur, con, question_id)
    print(f"\nInsert three answer choices for questions with id {question_id}. Result:")
    print(msg)

    # 4. An insert query that fails the validation constraint and raises and integrity error
    print("\nAn insert query that fails the validation constraint and raises and integrity error:")
    sql_stmt = "INSERT INTO QuizQuestion (quiz_id, question_id) VALUES (?, ?);"
    vals = (1000, 77)
    execute_insert_query(cur, con, sql=sql_stmt, values=vals, type=1)

    con.close()
