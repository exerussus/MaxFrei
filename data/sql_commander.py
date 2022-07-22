import sqlite3


def create_table():

    db = sqlite3.connect('spells_base.db')
    cursor = db.cursor()

    # Создание таблицы
    cursor.execute('CREATE TABLE IF NOT EXISTS spell('
                   'spell_id VARCHAR PRIMARY KEY,'
                   'name VARCHAR,'
                   'spell_type VARCHAR,'
                   'sub_type VARCHAR,'
                   'special_type VARCHAR,'
                   'direction VARCHAR,'
                   'value_health_caster VARCHAR,'
                   'value_psyche_caster VARCHAR,'
                   'value_mana_caster VARCHAR,'
                   'value_health_target VARCHAR,'
                   'value_psyche_target VARCHAR,'
                   'value_mana_target VARCHAR,'
                   'light_magic VARCHAR,'
                   'dark_magic VARCHAR,'
                   'count VARCHAR,'
                   'stun_caster VARCHAR,'
                   'stun_target VARCHAR,'
                   'attack_stopper_caster VARCHAR,'
                   'defend_stopper_caster VARCHAR,'
                   'attack_stopper_target VARCHAR,'
                   'defend_stopper_target VARCHAR,'
                   'dispelling VARCHAR,'
                   'gender VARCHAR);')
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
    first_name = choice(cursor.fetchall())

    cursor.execute(f"""SELECT * FROM second_names;""")
    second_name = choice(cursor.fetchall())

    cursor.execute(f"""SELECT * FROM orders;""")
    order = choice(cursor.fetchall())

    return first_name, second_name, order


def select_spell(spell_id):
    db = sqlite3.connect('data/spells_base.db')
    cursor = db.cursor()
    cursor.execute(f"""SELECT * FROM spell where spell_id = "{spell_id}";""")
    return cursor.fetchall()


print(select_spell(1))

