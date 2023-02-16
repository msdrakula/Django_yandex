import sqlite3


con = sqlite3.connect('db2.sqlite')
cur = con.cursor()


cur.executescript('''
CREATE TABLE IF NOT EXISTS original_names(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    original_name_id INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(original_name_id) REFERENCES original_names(id)
);
''')

con.commit()
con.close()

