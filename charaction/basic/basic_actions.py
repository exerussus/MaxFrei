

class Health:

    @staticmethod
    def decrease(character, value):
        character.health -= value

    @staticmethod
    def adding(character, value):
        character.health += value


class Psyche:

    @staticmethod
    def decrease(character, value):
        character.psyche -= value

    @staticmethod
    def adding(character, value):
        character.psyche += value


class Mana:

    @staticmethod
    def decrease(character, value):
        character.mana -= value

    @staticmethod
    def adding(character, value):
        character.mana += value


class Luck:

    @staticmethod
    def decrease(character, value):
        character.luck -= value

    @staticmethod
    def adding(character, value):
        character.luck += value

