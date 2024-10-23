import sqlite3 as sq

con = sq.connect('not_telegram.db')
cur = con.cursor()

# пришлось дропнуть для сброса primary-счетчика
cur.execute('DROP TABLE IF EXISTS Users;')

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

users = []
print('Заполняем таблицу 10-ю записями <for i in range(1, 11):>...')
for i in range(1, 11):
    username = f'User{i}'
    email = f'example{i}@gmail.com'
    age = i * 10
    balance = 1000

    cur.execute('''
    INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
    ''', (username, email, age, balance))

print('Обновляем баланс у каждого второго юзера <WHERE id%2 = 1;>...')
cur.execute('''
    UPDATE Users
    SET Balance = 500
    WHERE id%2 = 1;
''')

print('Удаляем каждую 3-ю запись <WHERE id%3=1;> в таблице начиная с 1-й...')
cur.execute('''
    DELETE FROM Users
    WHERE id%3=1;
''')

print('Выборка все пользователей, чей возраст не равен 60:')
cur.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age !=60;
''')
users=cur.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

#очистка базы для тестов
# cur.execute('''
#     DELETE FROM Users;
# ''')

con.commit()
con.close()
