import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
cur.execute('''
SELECT name 
FROM sqlite_master 
HERE type='table';
''')

cur.execute("""
SELECT name
FROM sqlite_master
WHERE type='table';
""")

table = cur.fetchall()[0][0] # Получите имя таблицы через атрибут курсора.


# Напишите SQL запрос в строке.
cur.execute(f'''
SELECT name, text
FROM {table};
''')
           


#for result in cur:
#    print(result)


con.commit()
con.close()


#SELECT name FROM sqlite_master WHERE type='table';




import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
cur.execute('''
SELECT name
FROM ice_cream
WHERE is_published=True AND is_published=True
''')


for result in cur:
    print(result)


con.commit()
con.close()


import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
cur.execute('''
SELECT *
FROM ice_cream
WHERE is_published=True 
ORDER BY text, name DESC
LIMIT 2 OFFSET 1;
''')

for result in cur:
    print(result[2:4])


con.commit()
con.close()