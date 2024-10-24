import sqlite3 as sq

con = sq.connect('not_telegram.db')
cur = con.cursor()

# пришлось дропнуть для сброса primary-счетчика
# cur.execute('DROP TABLE IF EXISTS Users;')

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

users=cur.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

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
print(f'Средний баланс равен: {tot2/tot1}')


con.commit()
con.close()
