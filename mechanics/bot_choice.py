

class BotChoice:
    """Рандомно выбирает спелл для бота. Потом сделаю поумнее"""

    @staticmethod
    def do(character):
        import random
        return random.choice(character.spells)
