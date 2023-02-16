import sqlite3


con = sqlite3.connect('db.sqlite')
cur = con.cursor()


movies = [
    (1, 'Безумные Мелодии Луни Тюнз', 2),
    (2, 'Весёлые мелодии', 2),
    (3, 'Кто подставил кролика Роджера', 3),
    (4, 'Хороший, плохой, злой', 3),
    (5, 'Последний киногерой', 3),
    (6, 'Она написала убийство', 4),
]


types = [
    (1, 'Мультфильм'),
    (2, 'Мультсериал'),
    (3, 'Фильм'),
    (4, 'Сериал'),
]



cur.executemany('INSERT INTO types VALUES(?, ?);', types)
cur.executemany('INSERT INTO movies VALUES(?, ?, ?);', movies)


con.commit()
con.close()