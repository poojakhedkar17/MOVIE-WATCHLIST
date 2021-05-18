import sqlite3

connection = sqlite3.connect("data.db",timeout=10)


def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (Content TEXT, Date TEXT);")


def add_entry(date, content):
    with connection:
        connection.execute("INSERT INTO entries VALUES (?, ?);", (content, date))


def fetch_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor
