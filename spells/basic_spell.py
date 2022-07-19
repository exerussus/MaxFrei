

class BasicSpell:

    def __init__(self,
                 spell_id=0000,
                 name='',
                 spell_type='',
                 subtype='',
                 direction='',
                 value_health=0,
                 value_psyche=0,
                 value_mana=0,
                 count=0,
                 ):

        self.spell_id = spell_id          # идентификатор спелла
        self.name = name                  # Название
        self.spell_type = spell_type      # Тип спела (атака\защита)
        self.subtype = subtype            # Подтип спела (защита: абсолютная защита, щит, контрудар; атака: хз, хз, хз)
        self.direction = direction        # Направление спела (противник, на себя, может быть и оба, но хз пока)
        self.value_health = value_health  # Количество здоровья
        self.value_psyche = value_psyche  # Количество психики
        self.value_mana = value_mana      # Количество энергии
        self.count = count                # Количество зарядов (если это щит, к примеру), оно же, ходов

