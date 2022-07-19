

class BasicSpell:

    def __init__(self,
                 caster,
                 target,
                 spell_id=0000,
                 name='',
                 spell_type='',
                 subtype='',
                 direction='',
                 value_health=0,
                 value_psyche=0,
                 value_mana=0,
                 value_drain_health=0,
                 value_drain_psyche=0,
                 value_drain_mana=0,
                 count=1,
                 stun=0,
                 attack_stopper=False,
                 defend_stopper=False,
                 ):

        self.caster = caster                          # Тот, кто кастует
        self.target = target                          # Тот, кто цель заклинания
        self.spell_id = spell_id                      # идентификатор спелла
        self.name = name                              # Название
        self.spell_type = spell_type                  # Тип спела (атака\защита)
        self.subtype = subtype                        # Подтип спела (защита: абсолютная защита, щит, контрудар)
        self.direction = direction                    # Направление спела (противник, на себя, может быть и оба)
        self.value_health = value_health              # Количество здоровья
        self.value_psyche = value_psyche              # Количество психики
        self.value_mana = value_mana                  # Количество энергии
        self.value_drain_health = value_drain_health  # Похищение здоровья
        self.value_drain_psyche = value_drain_psyche  # Похищение психики
        self.value_drain_mana = value_drain_mana      # Похищение энергии
        self.count = count                            # Количество ходов
        self.stun = stun                              # Пропуск хода
        self.attack_stopper = attack_stopper          # Запрещает атаку
        self.defend_stopper = defend_stopper          # Запрещает защиту

    def do(self):
        pass
