

class Restoration:

    @staticmethod
    def health(character, value):
        from charaction.basic.basic_actions import Health
        Health.adding(character, value)
        if character.health >= character.max_health:
            character.health = character.max_health

    @staticmethod
    def psyche(character, value):
        from charaction.basic.basic_actions import Psyche
        Psyche.adding(character, value)
        if character.health >= character.max_health:
            character.health = character.max_health

    @staticmethod
    def mana(character, value):
        from charaction.basic.basic_actions import Mana
        Mana.adding(character, value)
        if character.health >= character.max_health:
            character.health = character.max_health

    @staticmethod
    def luck(character, value):
        from charaction.basic.basic_actions import Luck
        Luck.adding(character, value)

