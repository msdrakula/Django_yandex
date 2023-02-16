import sqlite3

con = sqlite3.connect('db2.sqlite')
cur = con.cursor()

cur.execute('''
-- Вернуть поле name из таблицы movies и поле name из original_names
SELECT movies.name,
       original_names.name
-- ...из двух таблиц
FROM movies,
     original_names
-- Выводить только те значения полей, для которых верно условие
WHERE movies.original_name_id = original_names.id
''')

for result in cur:
    print(result)




con.close() 