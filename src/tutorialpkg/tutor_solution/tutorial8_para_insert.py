"""Possible solutions to the activities in week 8 INSERT queries."""

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


if __name__ == '__main__':
    # All queries are in a single 'try/except' so as soon as one fails the block will stop executing
    try:
        db_path_para_queries = Path(__file__).parent.parent.joinpath('data_db_activity', 'para_queries.db')
        con, cur = get_db_con(db_path_para_queries)

        # Print the SQL to the terminal
        con.set_trace_callback(print)

        # 1. Insert a new Quiz with quiz_name value "My first quiz"
        print("\nQuestion 1: Insert a new Quiz with quiz_name value 'My first quiz'.")
        vals = ("My first quiz",)
        sql_stmt = "INSERT INTO Quiz (quiz_name) VALUES (?);"
        cur.execute(sql_stmt, vals)
        con.commit()
        quiz_id = cur.lastrowid
        print("\nInserted a new Quiz with id:")
        print(quiz_id)

        # 2. Insert two new Questions for the Quiz you just entered.
        print(f"\nQuestion 2: Insert two new Questions for the Quiz with id {quiz_id}.")
        q_text = [("text for question 1",), ("text for question 2",)]
        for qt in q_text:
            sql_ques = "INSERT INTO Question (question) VALUES (?);"
            cur.execute(sql_ques, qt)
            quest_id = cur.lastrowid
            qq_vals = (quiz_id, quest_id)
            sql_qq = "INSERT INTO QuizQuestion (quiz_id, question_id) VALUES (?, ?);"
            cur.execute(sql_qq, qq_vals)
            question_id = cur.lastrowid
            print(f'Question inserted with id: {question_id}')

        # 3. Insert three answer choices for one of the new questions.
        print("\nQuestion 3: Insert three answer choices for one of the new questions.")
        choices = [(question_id, "option a", 1, 1),
                   (question_id, "option b", 0, 0),
                   (question_id, "option c", 0, -0)]
        sql_stmt = "INSERT INTO AnswerChoice (question_id, choice_text, choice_value, is_correct) VALUES (?, ?, ?, ?);"
        cur.executemany(sql_stmt, choices)
        print(f"\nInserted three answer choices for questions with id {question_id}. Added to the Question table as:")
        cur.execute("SELECT * FROM AnswerChoice WHERE question_id = ?;", (question_id,))
        rows = cur.fetchall()
        [print(row) for row in rows]

        # 4. An insert query that fails the validation constraint and raises and integrity error]
        # Fail FK validation as no Quiz exists with an ID of 1000
        print("\nQuestion 4: An insert query that fails the validation constraint and raises and integrity error:")
        sql_stmt = "INSERT INTO QuizQuestion (quiz_id, question_id) VALUES (?, ?);"
        vals = (1000, 77)
        cur.execute(sql_stmt, vals)

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
