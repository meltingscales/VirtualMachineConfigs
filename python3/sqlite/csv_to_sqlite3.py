import sqlite3

connection = sqlite3.connect('my_cool_db.db')

connection.execute('''CREATE TABLE IF NOT EXISTS color_table (
    id      INTEGER PRIMARY KEY NOT NULL,
    color   TEXT,
    number  INTEGER,
    fpnum   FLOAT
);
''')
