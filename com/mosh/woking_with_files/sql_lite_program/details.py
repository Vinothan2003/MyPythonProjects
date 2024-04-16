import json
from pathlib import Path
import sqlite3

# person_details = json.loads(Path("details_data.json").read_text())
with sqlite3.connect("data.sqlite3") as connection:
    """
    Inserting into the database
    command = "INSERT INTO Details VALUES(?, ?, ?)"
    for details in person_details:
        connection.execute(command, tuple(details.values()))
    connection.commit()"""

    # Reading from the database
    command = "SELECT * FROM Details"
    # print(connection.execute(command)) --> get cursor object
    cursor = connection.execute(command)
    for row in cursor:
        print(row)
