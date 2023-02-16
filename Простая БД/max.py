import sqlite3


con = sqlite3.connect('db_new2.sqlite')
cur = con.cursor()

cur.execute('''
SELECT SUM(birthday_year)
FROM directors
''')

for result in cur:
    print(result)

con.close()