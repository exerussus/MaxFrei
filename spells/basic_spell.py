import random


class BasicSpell:
    from data.sql_commander import select_spell
    info = select_spell(0)

    def __init__(self,
                 caster,   # Применяющий
                 target,   # Цель заклинания
                 spell_id=info[0],
                 name=info[1],
                 spell_type=info[2],
                 subtype=info[3],  # instant, periodic,
                 special_type=info[4],
                 direction=info[5],
                 value_health_caster=info[6],
                 value_psyche_caster=info[7],
                 value_mana_caster=info[8],
                 value_health_target=info[9],
                 value_psyche_target=info[10],
                 value_mana_target=info[11],
                 light_magic=info[12],
                 dark_magic=info[13],
                 count=info[14],
                 stun_caster=info[15],
                 stun_target=info[16],
                 attack_stopper_caster=info[17],
                 defend_stopper_caster=info[18],
                 attack_stopper_target=info[19],
                 defend_stopper_target=info[20],
                 dispelling=info[21],
                 description=info[22]

                 ):

        self.caster = caster                              # Тот, кто кастует
        self.target = target                              # Тот, кто цель заклинания
        self.spell_id = spell_id                          # идентификатор спелла
        self.name = name                                  # Название
        self.spell_type = spell_type                      # Тип спела (атака\защита)
        self.subtype = subtype                            # Подтип спела (защита: абсолютная защита, щит, контрудар)
        self.special_type = special_type                  # Специальный тип
        self.light_magic_spell = light_magic              # Ступень магии
        self.dark_magic_spell = dark_magic                # Ступень магии
        self.direction = direction                        # Направление спела (противник, на себя, может быть и оба)
        self.value_health_caster = value_health_caster    # Количество здоровья применяющего
        self.value_psyche_caster = value_psyche_caster    # Количество психики применяющего
        self.value_mana_target = value_mana_target       # Количество энергии цели
        self.value_health_target = value_health_target    # Количество здоровья цели
        self.value_psyche_target = value_psyche_target    # Количество психики цели
        self.count = count                                # Количество ходов
        self.stun_caster = stun_caster                    # Пропуск хода применяющего
        self.stun_target = stun_target                    # Пропуск хода применяющего
        self.attack_stopper_caster = attack_stopper_caster       # Запрещает атаку кастеру
        self.defend_stopper_caster = defend_stopper_caster       # Запрещает защиту кастеру
        self.attack_stopper_target = attack_stopper_target       # Запрещает атаку кастеру
        self.defend_stopper_target = defend_stopper_target       # Запрещает защиту кастеру
        self.dispelling = dispelling                             # Можно ли развеять
        self.description = description                           # Описание

        # Логика для количества энергии цели
        if self.caster.dark_magic_skill >= self.dark_magic_spell:
            dark_cost = 0
        else:
            dark_cost = self.dark_magic_spell - self.caster.dark_magic_skill

        if self.caster.light_magic_skill >= self.light_magic_spell:
            light_cost = 0
        else:
            light_cost = self.light_magic_spell - self.caster.light_magic_skill
        all_cost = random.choice([value_mana_caster/5, -value_mana_caster/5]) + dark_cost + light_cost
        self.value_mana_caster = value_mana_caster - all_cost  # Кол-тво энергии кастера с учётом всех требований

    def do(self):
        self.caster.mana += self.value_mana_caster
        self.caster.health += self.value_health_caster   # Количество здоровья применяющего
        self.caster.psyche += self.value_psyche_caster   # Количество психики применяющего
        self.target.mana += self.value_mana_target       # Количество энергии цели
        self.target.health += self.value_health_target   # Количество здоровья цели
        self.target.psyche += self.value_psyche_target

        if self.stun_caster:
            self.caster.under_stun = True
        if self.stun_target:
            self.target.under_stun = True
        if self.attack_stopper_caster:
            self.caster.attack_stopped = True
        if self.defend_stopper_caster:
            self.caster.defend_stopped = True
        if self.attack_stopper_target:
            self.target.attack_stopped = True
        if self.defend_stopper_target:
            self.target.defend_stopped = True
        self.count -= 1

    def __str__(self):
        return self.description

