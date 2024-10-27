import sqlite3


# Функция для инициализации базы данных
def initiate_db():
    # Подключаемся к базе данных (если она не существует, то создастся новая)
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # # дроп для обнуления таблицы
    # cursor.execute('DROP TABLE IF EXISTS Products;')

    # Создаем таблицу Products, если она еще не создана
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT NOT NULL,
                        price INTEGER NOT NULL
                    )''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        balance INTEGER NOT NULL
                    )''')
    conn.commit()

    # conn.close()


# функция добавления пользователя в базу
def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Users WHERE username=?", (username,))
    if cur.fetchone() is None:
        cur.execute(f'''
        INSERT INTO Users (username, email, age, balance)
        VALUES(?,?,?,?)
''', (username, email, age, 1000))  # Вставляем баланс как 1000)
    conn.commit()
    conn.close()


# Функция для получения всех продуктов
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Выполняем запрос на получение всех продуктов
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products


# Пример добавления продуктов (необходимо выполнить перед запуском бота)
def populate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Пример записи продуктов в базу данных
    products = [
        ('Product1', 'Витамин С', 100),
        ('Product2', 'Аскорбинка', 200),
        ('Product3', 'Дражже для похудения к чаю', 300),
        ('Product4', 'Витамин В', 400),
        ('Product5', 'Витамин B12', 500),
        ('Product6', 'Ревит', 600),
        ('Product7', 'Мультивитамин', 700)
    ]

    # Добавляем записи в таблицу
    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()


# Вызвать эту функцию один раз для заполнения базы данных
if __name__ == '__main__':
    initiate_db()
    populate_db()
# populate_db()
