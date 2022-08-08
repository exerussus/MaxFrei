
def battle_test():
    from charaction.character import Character
    from mechanics.battle_ground import BattleGround

    max_frei = Character(name='Макс Фрай')
    enemy = Character()
    battle = BattleGround(max_frei, enemy)

    battle.first_char.health -= 22
    battle.first_char.psyche += 2
    battle.second_char.health -= 22
    battle.second_char.psyche += 2

    print('\nВне баттла: ')
    for i in [max_frei, enemy]:
        print(f'{i.name} имеет {i.health} здоровья и {i.psyche} психики')

    print('\nВ баттле: ')
    for i in [battle.first_char, battle.second_char]:
        print(f'{i.name} имеет {i.health} здоровья и {i.psyche} психики')


def test_spell_casting():
    from spells.fire_hand import FireHand
    from charaction.character import Character

    my_hero = Character(name="Таранис", gender="male", dark_magic_skill=77, light_magic_skill=65)
    enemy = Character()
    test = FireHand(my_hero, enemy)
    print(test)
    print('\n')
    while True:
        print(test.do())
        print(f"Кастующий герой: здоровье - {my_hero.health}, а энергия - {my_hero.mana}")
        print(f"Герой-цель: здоровье - {enemy.health}, а энергия - {enemy.mana}")
        x = input("Next...")
        if x in ['No', 'no', 'NO', 'nO']:
            break


def sql_check():
    import sqlite3
    db = sqlite3.connect('data/data_base.db')
    cursor = db.cursor()

    cursor.execute(f""" """)
    return cursor.fetchall()


def class_check_new_character():
    from charaction.character import Character
    my_hero = Character(name="Таранис Джонс", gender='male')
    print(my_hero)


def check_character(character_id=None):

    from charaction.character import Character
    my_hero = Character(character_id=character_id)
    return my_hero


def check_select_spell_list(character_id=None):
    from charaction.character import Character

    my_hero = Character(character_id=character_id)
    return my_hero


def check_action_choice():
    from mechanics.action_choice import ActionChoice
    ActionChoice.do(check_select_spell_list(1))


def check_got_choice():
    from mechanics.bot_choice import BotChoice
    print(BotChoice.do(check_character(1)))


def checking_battle_ground():
    from charaction.character import Character
    from mechanics.battle_ground import BattleGround
    my_first_hero = Character(character_id=1)
    my_second_hero = Character(character_id=2)
    new_battle = BattleGround(my_first_hero, my_second_hero)
    new_battle.main()


checking_battle_ground()
