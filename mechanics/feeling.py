

class Feeling:

    @staticmethod
    def mana_cost(value):
        if value >= 65:
            return "огромное количество"
        elif 65 < value >= 45:
            return "много"
        elif 45 < value >= 25:
            return "немного"
        elif 25 > value:
            return "мало"

    @staticmethod
    def own_mana(value):
        if value >= 85:
            return "Вы чувствуете себя полным энергии"
        elif 85 < value >= 65:
            return "Вы чувствуете себя бодрым"
        elif 65 < value >= 45:
            return "Вы чувствуете себя усталым"
        elif 45 < value >= 25:
            return "Вы чувствуете себя сильно уставшим"
        elif 25 > value:
            return "Вы чувствуете себя истощенным"

    @staticmethod
    def own_health(value):
        if value >= 85:
            return "Вы чувствуете себя здоровым"
        elif 85 < value >= 65:
            return "Вы ранены"
        elif 65 < value >= 45:
            return "Вы сильно ранены"
        elif 45 < value >= 25:
            return "Вы в тяжелом состоянии"
        elif 25 > value:
            return "Вы при смерти"


