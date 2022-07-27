

class BasicSpell:
    from data.sql_commander import select_spell
    from random import choice
    info = select_spell(0)

    spell_id = info[0]  # идентификатор спелла
    name = info[1]  # Название
    spell_type = info[2]  # Тип спела (атака\защита)
    subtype = info[3]  # Подтип спела (защита: абсолютная защита, щит, контрудар)
    special_type = info[4]  # Специальный тип
    direction = info[5]  # Направление спела (противник, на себя, может быть и оба)
    value_health_caster = info[6]  # Количество здоровья применяющего
    value_psyche_caster = info[7]  # Количество психики применяющего
    value_mana_target = info[11]  # Количество энергии цели
    value_health_target = info[9]  # Количество здоровья цели
    value_psyche_target = info[10]  # Количество психики цели
    light_magic_spell = info[12]  # Ступень магии
    dark_magic_spell = info[13]  # Ступень магии
    stun_caster = info[15]  # Пропуск хода применяющего
    stun_target = info[16]  # Пропуск хода применяющего
    attack_stopper_caster = info[17]  # Запрещает атаку кастеру
    defend_stopper_caster = info[18]  # Запрещает защиту кастеру
    attack_stopper_target = info[19]  # Запрещает атаку кастеру
    defend_stopper_target = info[20]  # Запрещает защиту кастеру
    dispelling = info[21]  # Можно ли развеять
    description = info[22]  # Описание
    mana_cost = info[8]

    def __init__(self,
                 caster,   # Применяющий
                 target,   # Цель заклинания
                 ):
        self.caster = caster  # Тот, кто кастует
        self.target = target  # Тот, кто цель заклинания
        self.count = BasicSpell.info[14]  # Количество ходов

        # Логика для количества энергии цели
        if self.caster.dark_magic_skill >= self.dark_magic_spell:
            dark_cost = 0
        else:
            dark_cost = self.dark_magic_spell - self.caster.dark_magic_skill

        if self.caster.light_magic_skill >= self.light_magic_spell:
            light_cost = 0
        else:
            light_cost = self.light_magic_spell - self.caster.light_magic_skill
        all_cost = BasicSpell.choice([BasicSpell.info[8] / 5, -BasicSpell.info[8] / 5]) + dark_cost + light_cost
        if all_cost < BasicSpell.info[8] / 2:
            all_cost = BasicSpell.info[8] / 2
        self.value_mana_caster = BasicSpell.info[8] - all_cost  # Кол-тво энергии кастера с учётом всех требований

    def do(self):
        self.caster.mana += self.value_mana_caster
        self.caster.health += BasicSpell.value_health_caster   # Количество здоровья применяющего
        self.caster.psyche += BasicSpell.value_psyche_caster   # Количество психики применяющего
        self.target.mana += BasicSpell.value_mana_target       # Количество энергии цели
        self.target.health += BasicSpell.value_health_target   # Количество здоровья цели
        self.target.psyche += BasicSpell.value_psyche_target

        if BasicSpell.stun_caster:
            self.caster.under_stun = True
        if BasicSpell.stun_target:
            self.target.under_stun = True
        if BasicSpell.attack_stopper_caster:
            self.caster.attack_stopped = True
        if BasicSpell.defend_stopper_caster:
            self.caster.defend_stopped = True
        if BasicSpell.attack_stopper_target:
            self.target.attack_stopped = True
        if BasicSpell.defend_stopper_target:
            self.target.defend_stopped = True
        self.count -= 1

    def __str__(self):
        return f"spell_id: {self.spell_id} \n" \
               f"name: {self.name} \n" \
               f"spell_type: {self.spell_type} \n" \
               f"subtype: {self.subtype} \n" \
               f"special_type: {self.special_type} \n" \
               f"light_magic_spell: {self.light_magic_spell} \n" \
               f"dark_magic_spell: {self.dark_magic_spell} \n" \
               f"direction: {self.direction} \n" \
               f"value_health_caster: {self.value_health_caster} \n" \
               f"value_psyche_caster: {self.value_psyche_caster} \n" \
               f"value_mana_caster: {self.value_mana_caster} \n" \
               f"value_health_target: {self.value_health_target} \n" \
               f"value_psyche_target: {self.value_psyche_target} \n" \
               f"value_mana_target: {self.value_mana_target} \n" \
               f"count: {self.count} \n" \
               f"stun_caster: {self.stun_caster} \n" \
               f"stun_target: {self.stun_target} \n" \
               f"attack_stopper_caster: {self.attack_stopper_caster} \n" \
               f"defend_stopper_caster: {self.defend_stopper_caster} \n" \
               f"attack_stopper_target: {self.attack_stopper_target} \n" \
               f"defend_stopper_target: {self.defend_stopper_target} \n" \
               f"dispelling: {self.dispelling} \n" \
               f"description: {self.description}"


