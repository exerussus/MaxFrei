

class Turn:

    def __init__(self, first_char, second_char):
        self.first_char = first_char
        self.second_char = second_char
        self.turn_now = self.first_char

    def do(self):

        spells = [spell for spell in self.turn_now.spells]

        if self.turn_now.player:
            count = 0
            for spell in spells:
                count += 1
                print(f"{count}. {spell} | {spell.value_mana_caster} энергии")  # НЕ ДОЛЖНО РАБОТАТЬ!
                # Экземпляр спелла ещё не создан, поэтому референс на value_mana_caster должен
                # вызвать ошибку. Варианты: создание класса при получении спелла, а потом делать
                # deepcopy при каждом касте, но нужно ещё думать

