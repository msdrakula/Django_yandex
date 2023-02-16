import sqlite3

con = sqlite3.connect('db2.sqlite')
cur = con.cursor()

original_names = [
    (1, 'Last Action Hero'),
    (2, 'Murder, She Wrote'),
    (3, 'Looney Tunes'),
    (4, 'Il Buono, il brutto, il cattivo'),
    (5, 'Who Framed Roger Rabbit'),
    (6, 'Merrie Melodies')
]

movies = [
    (1, 'Безумные Мелодии Луни Тюнз', 3),
    (2, 'Весёлые мелодии', 6),
    (3, 'Кто подставил кролика Роджера', 5),
    (4, 'Хороший, плохой, злой', 4),
    (5, 'Последний киногерой', 1),
    (6, 'Она написала убийство', 2)
]

cur.executemany('INSERT INTO original_names VALUES(?, ?);', original_names)
cur.executemany('INSERT INTO movies VALUES(?, ?, ?);', movies)

con.commit()
con.close() 