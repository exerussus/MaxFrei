

class ActionChoice:
    """Печатает список спеллов игроку и предоставляет сделать выбор. Возвращает класс способности."""

    @staticmethod
    def do(character):
        from mechanics.feeling import Feeling
        count = 0
        print(f"{Feeling.own_health(character.health)} {Feeling.own_mana(character.mana)}")

        for action in character.spells:
            count += 1
            print(f"{count}. {action.description} {Feeling.mana_cost(action.mana_cost)}")

        result = None
        key = True
        while key:
            if key:
                try:
                    choice = int(input("Выберите номер действия: "))
                except TypeError:
                    choice = ''
                if 0 < choice < len(character.spells):
                    result = character.spells[choice - 1]
                    key = False
                    break
                else:
                    print('Неверный номер действия...')

        return result
