# 5. SQL UPDATE queries

## Databases used

[Chinook database](../../src/tutorialpkg/data_db_activity/chinook.db):

<img alt="ERD Chinook database" src="../img/erd-chinook.png" width=50%>

[Paralympics query database](../../src/tutorialpkg/data_db_activity/para_queries.db):

![ERD Paralmpics database for queries](../img/erd-para-queries.png)

## SQL UPDATE

Reference links:

- [SQLite UPDATE reference](https://www.sqlite.org/lang_update.html)
- [SQLite UPDATE tutorial](https://www.sqlitetutorial.net/sqlite-update/)

UPDATE is used to update values in existing rows in a table.

The general syntax is:

```sqlite
UPDATE table
SET column_1 = new_value_1,
    column_2 = new_value_2
WHERE
    search_condition 
```

You can also add ORDER BY and LIMIT if needed.

**Note** that if you do not specify a WHERE clause then all the rows the table will be updated!

## Chinook database UPDATE queries
This assumes you ran the insert queries
in [tutorial8_insert_queries.py](../../src/tutorialpkg/queries/tutorial8_insert_queries.py). Make sure you run
this at least once before you try to update or there will not be anything to update!

Open [tutorial8_update_queries.py](../../src/tutorialpkg/queries/tutorial8_update_queries.py) and view and run
the code.

There are 3 examples:

```python
# 1. Change the artist name from New Artist 1 to New Artist 100 for all instances
cursor.execute("UPDATE artists SET Name = 'New Artist 100' WHERE Name = 'New Artist 1';")
connection.commit()

# 2. Change the album title from New Album 1 to New Album 100 for all instances
cursor.execute("UPDATE albums SET Title = 'New Album 100' WHERE Title = 'New Album 1';")
connection.commit()

# 3. Change the ArtistId for the last album to be added to 3500
# Should raise an integrity error since the ArtistId 3500 does not exist in the artists table
try:
    last_album_id = cursor.execute('SELECT MAX(AlbumId) FROM albums;').fetchone()[0]
    cursor.execute('UPDATE albums SET ArtistId = 3500 WHERE AlbumId = ?;', (last_album_id,))
    connection.commit()
except sqlite3.IntegrityError as e:
    print(f"An integrity error occurred: {e}")
```
## Paralympics database UPDATE queries

Write your own code for the following:

1. Update the Quiz name from "My first quiz" to "My first quiz updated"
2. Update the question 'text' for all questions to the value: "the same question text for all questions"
3. Print all the rows from the Question table. Change the id of Quiz with quiz_id=1 to quiz_id=50. Now print all the
   rows from the Question table again. Why has the quiz_id in the Question table changed when you only changed the Quiz
   table?

[Next activity](8-6-delete.md)