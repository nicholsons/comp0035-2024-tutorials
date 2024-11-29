"""Possible solutions to the activities in week 8 UPDATE queries.

"""

from pathlib import Path
import sqlite3


def get_db_con(db_path):
    """Returns a connection and cursor to the chinook database."""
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        cur.execute('PRAGMA foreign_keys = ON;')
        con.commit()
        # con.set_trace_callback(print)
        return con, cur
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
    db_path_para_queries = Path(__file__).parent.parent.joinpath('data_db_activity', 'para_queries.db')
    con, cur = get_db_con(db_path_para_queries)

    # Will only work if you have run the insert queries to set the values for the quiz etc!

    cur.execute("SELECT * FROM Quiz;")
    result = cur.fetchall()
    print("\nQuiz table before:")
    [print(row) for row in result]

    cur.execute("SELECT * FROM Question;")
    result = cur.fetchall()
    print("\nQuestion table before:")
    [print(row) for row in result]

    cur.execute("SELECT * FROM AnswerChoice;")
    result = cur.fetchall()
    print("\nAnswerChoice table before:")
    [print(row) for row in result]

    cur.execute("SELECT * FROM QuizQuestion;")
    result = cur.fetchall()
    print("\nQuizQuestion table before:")
    [print(row) for row in result]

    # 1. Delete the quiz
    cur.execute("DELETE FROM Quiz;")
    # 2. Delete the questions
    # cur.execute("DELETE FROM Question;")
    # 3. Delete the answer choices for the questions
    # Nothing needed! Due to the ON DELETE CASCADE rows is table are deleted when the question table rows are deleted!
    # The QuizQuestion rows are also deleted

    con.commit()

    cur.execute("SELECT * FROM Quiz;")
    result = cur.fetchall()
    print("\nQuiz table after:")
    [print(row) for row in result]

    cur.execute("SELECT * FROM Question;")
    result = cur.fetchall()
    print("\nQuestion table after:")
    [print(row) for row in result]

    cur.execute("SELECT * FROM AnswerChoice;")
    result = cur.fetchall()
    print("\nAnswerChoice table after:")
    [print(row) for row in result]

    cur.execute("SELECT * FROM QuizQuestion;")
    result = cur.fetchall()
    print("\nQuizQuestion table after:")
    [print(row) for row in result]

    con.close()
