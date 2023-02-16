import sqlite3


con = sqlite3.connect('db_new2.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY,
    name TEXT,
    birthday_year INTEGER
);

CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    release_year INTEGER
);



''')

con.commit()
con.close()