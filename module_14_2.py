import sqlite3 as sq

con = sq.connect('not_telegram.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
'''
            )

cur.execute(('''
DELETE FROM Users
WHERE id =6
'''))

cur.execute(('''
SELECT COUNT(*) FROM Users
'''))
tot1 = cur.fetchone()[0]
print(f'Всего записей: {tot1}')

cur.execute("SELECT SUM(balance) FROM Users")
tot2 = cur.fetchone()[0]
print(f'Сумма всех балансов: {tot2}')
print(f'Средний баланс: {tot2/tot1}')


con.commit()
con.close()
