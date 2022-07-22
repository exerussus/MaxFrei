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


def select_random_names(gender=None):
    db = sqlite3.connect('names_base.db')
    cursor = db.cursor()

    if not gender:
        import random
        gender = random.choice(['male', 'female'])

    # Получение данных из таблицы
    cursor.execute(f"""SELECT * FROM name 
                   where gender = "{gender}";""")
    names = cursor.fetchall()
    list_first_names = [name[0] for name in names]

    cursor.execute(f"""SELECT * FROM second_names;""")
    list_second_names = cursor.fetchall()

    cursor.execute(f"""SELECT * FROM order;""")
    orders = cursor.fetchall()

    return list_first_names, list_second_names, orders


def full_random_name():
    import random

    firsts, seconds, orders = select_random_names()
    first_name = random.choice(firsts)
    second_name = random.choice(seconds)
    order = random.choice(orders)
    return f"{first_name} {second_name} {order}"


full_random_name()

