

class BasicSpell:

    def __init__(self,
                 caster,
                 target,
                 spell_id=1,
                 name='Огненная ладонь',
                 spell_type='attack',
                 subtype='',
                 direction='target',
                 value_health_caster=0,
                 value_psyche_caster=0,
                 value_mana_caster=0,
                 value_health_target=-15,
                 value_psyche_target=0,
                 value_mana_target=0,
                 light_magic=1,
                 dark_magic=1,
                 count=1,
                 stun=0,
                 attack_stopper=False,
                 defend_stopper=False,
                 ):

        self.caster = caster                             # Тот, кто кастует
        self.target = target                             # Тот, кто цель заклинания
        self.spell_id = spell_id                         # идентификатор спелла
        self.name = name                                 # Название
        self.spell_type = spell_type                     # Тип спела (атака\защита)
        self.subtype = subtype                           # Подтип спела (защита: абсолютная защита, щит, контрудар)
        self.light_magic = light_magic                   # Ступень магии
        self.dark_magic = dark_magic                     # Ступень магии
        self.direction = direction                       # Направление спела (противник, на себя, может быть и оба)
        self.value_health_caster = value_health_caster   # Количество здоровья применяющего
        self.value_psyche_caster = value_psyche_caster   # Количество психики применяющего
        self.value_mana_caster = value_mana_caster       # Количество энергии применяющего
        self.value_health_target = value_health_target   # Похищение здоровья цели
        self.value_psyche_target = value_psyche_target   # Похищение психики цели
        self.value_mana_target = value_mana_target       # Похищение энергии цели
        self.count = count                               # Количество ходов
        self.stun = stun                                 # Пропуск хода
        self.attack_stopper = attack_stopper             # Запрещает атаку
        self.defend_stopper = defend_stopper             # Запрещает защиту



    def do(self):
        pass
