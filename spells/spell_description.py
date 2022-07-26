
class DescriptionSpell:
    def __init__(self, info):
        self.spell_id = info[0]                          # идентификатор спелла
        self.name = info[1]                                 # Название
        self.spell_type = info[2]                      # Тип спела (атака\защита)
        self.subtype = info[3]                           # Подтип спела (защита: абсолютная защита, щит, контрудар)
        self.special_type = info[4]                  # Специальный тип
        self.direction = info[5]                        # Направление спела (противник, на себя, может быть и оба)
        self.value_health_caster = info[6]    # Количество здоровья применяющего
        self.value_psyche_caster = info[7]    # Количество психики применяющего
        self.value_mana_target = info[11]       # Количество энергии цели
        self.value_health_target = info[9]    # Количество здоровья цели
        self.value_mana_caster = info[8]
        self.value_psyche_target = info[10]    # Количество психики цели
        self.light_magic_spell = info[12]              # Ступень магии
        self.dark_magic_spell = info[13]                # Ступень магии
        self.count = info[14]                                # Количество ходов
        self.stun_caster = info[15]                    # Пропуск хода применяющего
        self.stun_target = info[16]                    # Пропуск хода применяющего
        self.attack_stopper_caster = info[17]       # Запрещает атаку кастеру
        self.defend_stopper_caster = info[18]       # Запрещает защиту кастеру
        self.attack_stopper_target = info[19]       # Запрещает атаку кастеру
        self.defend_stopper_target = info[20]       # Запрещает защиту кастеру
        self.dispelling = info[21]                             # Можно ли развеять
        self.description = info[22]                           # Описание

    def __str__(self):
        return f"{self.name}"
