

class Character:
    """Создает персонажа"""

    def __init__(self,
                 name='',
                 health=100,
                 mana=100,
                 psyche=100,
                 dark_magic_skill=15,
                 light_magic_skill=15,
                 character_class_id=1,
                 gender='',
                 player=False,
                 character_id=None):
        from data.sql_commander import select_spell_list
        from data.sql_commander import get_character, create_character

        if not character_id:
            char_info = get_character(create_character(name=name,
                                                       health=health,
                                                       mana=mana,
                                                       psyche=psyche,
                                                       dark_magic_skill=dark_magic_skill,
                                                       light_magic_skill=light_magic_skill,
                                                       character_class_id=character_class_id,
                                                       gender=gender,
                                                       player=player))
        else:
            char_info = get_character(character_id)

        self.character_id = char_info[0]
        self.gender = char_info[1]    # Пол персонажа
        self.name = char_info[2]      # Имя персонажа
        self.health = char_info[3]                                              # Текущее здоровье
        self.max_health = char_info[4]                                          # Максимальное здоровье
        self.psyche = char_info[5]                                              # Текущая психика
        self.max_psyche = char_info[6]                                          # Максимальная психика
        self.mana = char_info[7]                                                  # Текущая энергия
        self.max_mana = char_info[8]                                              # Максимальная энергия
        self.dark_magic_skill = char_info[9]                          # Ступень тёмной магии
        self.light_magic_skill = char_info[10]                        # Ступень светлой магии
        self.character_class = char_info[11]                            # Класс персонажа
        self.spells = select_spell_list(char_info[12])                        # Базовые умения персонажа согласно классу
        self.luck = char_info[13]                                                     # Удача
        self.alive = char_info[14]                                                 # Жив или мёртв
        self.player = char_info[15]                                              # Игровой ли персонаж
        self.under_stun = char_info[16]                                           # Под станом
        self.attack_stopped = char_info[17]
        self.defend_stopped = char_info[18]

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Пол: {"Мужчина" if self.gender == "male" else "Женщина"}\n' \
               f'Здоровье: {self.health} из {self.max_health}\n' \
               f'Психика: {self.psyche} из {self.max_psyche}\n' \
               f'Энергия: {self.mana} из {self.max_mana}\n' \
               f'Удача: {self.luck}\n' \
               f'Ступень Черной магии: {self.dark_magic_skill}\n' \
               f'Ступень Белой магии: {self.light_magic_skill}\n' \
               f'Класс: {self.character_class}\n' \
               f'Умения: {[spell.description for spell in self.spells]}'

