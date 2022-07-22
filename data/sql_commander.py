import sqlite3


def create_table():

    db = sqlite3.connect('names_base.db')
    cursor = db.cursor()

    # Создание таблицы
    cursor.execute('CREATE TABLE IF NOT EXISTS name(\n'
                'name VARCHAR PRIMARY KEY,\n'
                'gender VARCHAR);\n')
    db.commit()  # Сохранение изменений


def add_names():

    db = sqlite3.connect('names_base.db')
    cursor = db.cursor()
    # Добавление данных из нескольких кортежей
    users = [('Beth', 'female'), ('Ilya', 'male')]
    cursor.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", users)
    db.commit()


def full_random_name(gender):
    """Генерирует полное имя персонажа"""
    from random import choice
    db = sqlite3.connect('data/names_base.db')
    cursor = db.cursor()

    if not gender:

        gender = choice(['male', 'female'])

    # Получение данных из таблицы
    cursor.execute(f"""SELECT name FROM name where gender = "{gender}";""")
    # names = cursor.fetchall()
    # list_first_names = [name[0] for name in names]
    first_name = choice(cursor.fetchall())

    cursor.execute(f"""SELECT * FROM second_names;""")
    second_name = choice(cursor.fetchall())

    cursor.execute(f"""SELECT * FROM orders;""")
    order = choice(cursor.fetchall())

    return first_name, second_name, order



