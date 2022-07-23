

class NewCharacter:
    """Создает персонажа"""

    def __init__(self,
                 name='',
                 health=100,
                 mana=100,
                 psyche=100,
                 dark_magic_skill=15,
                 light_magic_skill=15,
                 character_class='Убийца',
                 gender='',
                 player=False):

        from charaction.name_random import NameRandom
        from random import choice
        from data.sql_commander import select_character

        info = select_character(0)
        self.character_id = info[0]
        self.gender = choice(['male', 'female']) if gender == '' or None else gender    # Пол персонажа
        self.name = NameRandom.choice(self.gender) if name == '' or None else name      # Имя персонажа
        self.health = health                                              # Текущее здоровье
        self.max_health = health                                          # Максимальное здоровье
        self.psyche = psyche                                              # Текущая психика
        self.max_psyche = psyche                                          # Максимальная психика
        self.mana = mana                                                  # Текущая энергия
        self.max_mana = mana                                              # Максимальная энергия
        self.dark_magic_skill = dark_magic_skill                          # Ступень тёмной магии
        self.light_magic_skill = light_magic_skill                        # Ступень светлой магии
        self.character_class = character_class                            # Класс персонажа
        self.spells = data_spells[character_class]                        # Базовые умения персонажа согласно классу
        self.luck = 3                                                     # Удача
        self.alive = True                                                 # Жив или мёртв
        self.player = player                                              # Игровой ли персонаж
        self.under_stun = False                                           # Под станом
        self.attack_stopped = False
        self.defend_stopped = False

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
               f'Умения: {[i for i in self.spells.keys()]}'

