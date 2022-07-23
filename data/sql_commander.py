import sqlite3


def create_spell_table():

    db = sqlite3.connect('data_base.db')
    cursor = db.cursor()

    # Создание таблицы
    cursor.execute('CREATE TABLE IF NOT EXISTS spell('
                   'spell_id INT PRIMARY KEY,'
                   'name VARCHAR,'
                   'spell_type VARCHAR,'
                   'sub_type VARCHAR,'
                   'special_type VARCHAR,'
                   'direction VARCHAR,'
                   'value_health_caster INT,'
                   'value_psyche_caster INT,'
                   'value_mana_caster INT,'
                   'value_health_target INT,'
                   'value_psyche_target INT,'
                   'value_mana_target INT,'
                   'light_magic INT,'
                   'dark_magic INT,'
                   'count INT,'
                   'stun_caster VARCHAR,'
                   'stun_target VARCHAR,'
                   'attack_stopper_caster VARCHAR,'
                   'defend_stopper_caster VARCHAR,'
                   'attack_stopper_target VARCHAR,'
                   'defend_stopper_target VARCHAR,'
                   'dispelling VARCHAR,'
                   'gender VARCHAR);')
    db.commit()  # Сохранение изменений


def create_character_table():

    db = sqlite3.connect('data_base.db')
    cursor = db.cursor()

    # Создание таблицы
    cursor.execute('CREATE TABLE IF NOT EXISTS character('
                   'character_id INT PRIMARY KEY,'
                   'gender VARCHAR,'
                   'name VARCHAR,'
                   'health INT,'
                   'max_health INT,'
                   'psyche INT,'
                   'max_psyche INT,'
                   'mana INT,'
                   'max_mana INT,'
                   'dark_magic_skill INT,'
                   'light_magic_skill INT,'
                   'character_class INT,'
                   'spells INT,'
                   'luck INT,'
                   'alive VARCHAR,'
                   'player VARCHAR,'
                   'under_stun VARCHAR,'
                   'attack_stopped VARCHAR,'
                   'defend_stopped VARCHAR);')
    db.commit()  # Сохранение изменений


def add_names():

    db = sqlite3.connect('data_base.db')
    cursor = db.cursor()
    # Добавление данных из нескольких кортежей
    users = [('Beth', 'female'), ('Ilya', 'male')]
    cursor.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", users)
    db.commit()


def full_random_name(gender):
    """Генерирует полное имя персонажа"""
    from random import choice
    db = sqlite3.connect('data/data_base.db')
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
    db = sqlite3.connect('data/data_base.db')
    cursor = db.cursor()
    cursor.execute(f"""SELECT * FROM spell where spell_id = "{spell_id}";""")
    return cursor.fetchall()[0]


def select_character(char_id):
    db = sqlite3.connect('data/data_base.db')
    cursor = db.cursor()
    cursor.execute(f"""SELECT * FROM spell where spell_id = "{char_id}";""")
    return cursor.fetchall()


def check_length_characters():
    db = sqlite3.connect('data/data_base.db')
    cursor = db.cursor()

    cursor.execute(f"""SELECT character_id FROM character;""")
    result = cursor.fetchall()
    return len(result)


def create_character(
                 name='',
                 health=100,
                 mana=100,
                 psyche=100,
                 dark_magic_skill=15,
                 light_magic_skill=15,
                 character_class_id=1,
                 gender='',
                 player=False):
    from random import choice
    from charaction.name_random import NameRandom

    db = sqlite3.connect('data/data_base.db')
    cursor = db.cursor()
    gender = gender if gender not in ['', None] else choice(['male', 'female'])
    name = NameRandom.choice(gender)
    spell_id = character_class_id
    # Добавление данных из кортежа
    new_char = (f'{check_length_characters()}', f'{gender}', f'{name}', f'{health}',
                f'{health}', f'{psyche}', f'{psyche}',
                f'{mana}', f'{mana}', f'{dark_magic_skill}',
                f'{light_magic_skill}', f'{character_class_id}', f'{spell_id}',
                f'{3}', f'{True}', f'{player}', f'{True}', f'{False}', f'{False}')
    cursor.execute("INSERT INTO character VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", new_char)
    db.commit()




