import sqlite3


con = sqlite3.connect('db_new2.sqlite')
cur = con.cursor()

cur.execute('''
SELECT id, name, birthday_year
FROM directors
WHERE birthday_year > 1912;
''')

for result in cur:
    print(result)

con.close()