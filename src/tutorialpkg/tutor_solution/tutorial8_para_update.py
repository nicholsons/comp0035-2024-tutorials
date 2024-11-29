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

    # 1. Update the Quiz name from "My first quiz" to "My first quiz updated"
    cur.execute("SELECT * FROM Quiz;")
    result = cur.fetchall()
    print("\nBefore quiz_name update:")
    [print(row) for row in result]
    cur.execute("UPDATE Quiz SET quiz_name = 'My first quiz updated' WHERE quiz_name = 'My first quiz';")
    con.commit()
    cur.execute("SELECT * FROM Quiz;")
    result = cur.fetchall()
    print("\nAfter quiz_name update:")
    [print(row) for row in result]

    # 2. Update the question text for all questions to the value: "the same question text for all questions"
    cur.execute("SELECT * FROM Question;")
    result = cur.fetchall()
    print("\nBefore question update:")
    [print(row) for row in result]
    cur.execute("UPDATE Question SET question = 'the same question text for all questions';")
    con.commit()
    cur.execute("SELECT * FROM Question;")
    result = cur.fetchall()
    print("\nAfter question update:")
    [print(row) for row in result]

    # 3. Print all the rows from the QuizQuestion table.
    cur.execute("SELECT * FROM QuizQuestion;")
    result = cur.fetchall()
    print("\nAll rows in QuizQuestion table before quiz id:")
    [print(row) for row in result]

    # Change the id of Quiz with quiz_id=1 to quiz_id=50.
    cur.execute("UPDATE Quiz SET quiz_id = 50 WHERE quiz_id=1;")
    con.commit()

    # Now print all the rows from the Question table again.
    cur.execute("SELECT * FROM QuizQuestion;")
    result = cur.fetchall()
    print("\nAll rows in QuizQuestion table after quiz_id updated in Quiz:")
    [print(row) for row in result]

    # Why has the quiz_id in the Question table changed when you only changed the Quiz table?
    # Answer: There is an ON UPDATE CASCADE constraint on the ForeignKey in the QuizQuestion table, 
    # so when the Quiz.quiz_id changes, the QuiQuestion.quiz_id also changes.

    con.close()
