

class FireHand:

    def __init__(self,
                 caster,   # Применяющий
                 target,   # Цель заклинания
                 ):
        from data.sql_commander import select_spell
        from random import choice
        info = select_spell(1)
        self.caster = caster  # Тот, кто кастует
        self.target = target  # Тот, кто цель заклинания
        self.spell_id = info[0]  # идентификатор спелла
        self.name = info[1]  # Название
        self.spell_type = info[2]  # Тип спела (атака\защита)
        self.subtype = info[3]  # Подтип спела (защита: абсолютная защита, щит, контрудар)
        self.special_type = info[4]  # Специальный тип
        self.direction = info[5]  # Направление спела (противник, на себя, может быть и оба)
        self.value_health_caster = info[6]  # Количество здоровья применяющего
        self.value_psyche_caster = info[7]  # Количество психики применяющего
        self.value_mana_target = info[11]  # Количество энергии цели
        self.value_health_target = info[9]  # Количество здоровья цели
        self.value_psyche_target = info[10]  # Количество психики цели
        self.light_magic_spell = info[12]  # Ступень магии
        self.dark_magic_spell = info[13]  # Ступень магии
        self.count = info[14]  # Количество ходов
        self.stun_caster = info[15]  # Пропуск хода применяющего
        self.stun_target = info[16]  # Пропуск хода применяющего
        self.attack_stopper_caster = info[17]  # Запрещает атаку кастеру
        self.defend_stopper_caster = info[18]  # Запрещает защиту кастеру
        self.attack_stopper_target = info[19]  # Запрещает атаку кастеру
        self.defend_stopper_target = info[20]  # Запрещает защиту кастеру
        self.dispelling = info[21]  # Можно ли развеять
        self.description = info[22]  # Описание

        # Логика для количества энергии цели
        if self.caster.dark_magic_skill >= self.dark_magic_spell:
            dark_cost = 0
        else:
            dark_cost = self.dark_magic_spell - self.caster.dark_magic_skill

        if self.caster.light_magic_skill >= self.light_magic_spell:
            light_cost = 0
        else:
            light_cost = self.light_magic_spell - self.caster.light_magic_skill
        all_cost = choice([info[8] / 5, -info[8] / 5]) + dark_cost + light_cost
        if all_cost < info[8] / 2:
            all_cost = info[8] / 2
        self.value_mana_caster = info[8] - all_cost  # Кол-тво энергии кастера с учётом всех требований

    def do(self):
        from random import choice
        self.caster.mana += self.value_mana_caster
        self.caster.health += self.value_health_caster  # Количество здоровья применяющего
        self.caster.psyche += self.value_psyche_caster  # Количество психики применяющего
        self.target.mana += self.value_mana_target  # Количество энергии цели
        self.target.health += self.value_health_target - choice([1, 2, 3, 4])  # Количество здоровья цели
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


