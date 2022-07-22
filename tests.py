
# def battle_test():
#     from charaction.character import Character
#     from battle.battle_ground import BattleGround
#
#     max_frei = Character(name='Макс Фрай', character_class='Истинный маг')
#     enemy = Character()
#     battle = BattleGround(max_frei, enemy)
#
#     battle.first_char.health -= 22
#     battle.first_char.psyche += 2
#     battle.second_char.health -= 22
#     battle.second_char.psyche += 2
#
#     print('\nВне баттла: ')
#     for i in [max_frei, enemy]:
#         print(f'{i.name} имеет {i.health} здоровья и {i.psyche} психики')
#
#     print('\nВ баттле: ')
#     for i in [battle.first_char, battle.second_char]:
#         print(f'{i.name} имеет {i.health} здоровья и {i.psyche} психики')

# from charaction.character import Character
# char = Character(male="male")
# print(char)

# from data.sql_commander import select_spell
# print(select_spell(1))

from spells.fire_hand import FireHand
from charaction.character import Character

my_hero = Character(name="Таранис", male="male", dark_magic_skill=77, light_magic_skill=65)
enemy = Character()
test = FireHand(my_hero, enemy)
print(test)
