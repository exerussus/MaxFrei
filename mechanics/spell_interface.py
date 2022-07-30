

class SpellInterface:

    def __init__(self, spell_id):
        from data.sql_commander import select_spell
        self.info = select_spell(spell_id)
        self.spell_id = spell_id  # идентификатор спелла
        self.name = self.info[1]  # Название
        self.spell_type = self.info[2]  # Тип спела (атака\защита)
        self.subtype = self.info[3]  # Подтип спела (защита: абсолютная защита, щит, контрудар)
        self.special_type = self.info[4]  # Специальный тип
        self.direction = self.info[5]  # Направление спела (противник, на себя, может быть и оба)
        self.value_health_caster = self.info[6]  # Количество здоровья применяющего
        self.value_psyche_caster = self.info[7]  # Количество психики применяющего
        self.value_mana_target = self.info[11]  # Количество энергии цели
        self.value_health_target = self.info[9]  # Количество здоровья цели
        self.value_psyche_target = self.info[10]  # Количество психики цели
        self.light_magic_spell = self.info[12]  # Ступень магии
        self.dark_magic_spell = self.info[13]  # Ступень магии
        self.stun_caster = self.info[15]  # Пропуск хода применяющего
        self.stun_target = self.info[16]  # Пропуск хода применяющего
        self.attack_stopper_caster = self.info[17]  # Запрещает атаку кастеру
        self.defend_stopper_caster = self.info[18]  # Запрещает защиту кастеру
        self.attack_stopper_target = self.info[19]  # Запрещает атаку кастеру
        self.defend_stopper_target = self.info[20]  # Запрещает защиту кастеру
        self.dispelling = self.info[21]  # Можно ли развеять
        self.description = self.info[22]  # Описание
        self.mana_cost = self.info[8]
        self.speed = self.info[23]

    def do(self, caster, target):
        from mechanics.basic_spell import BasicSpell
        return BasicSpell(caster, target, self.info)
