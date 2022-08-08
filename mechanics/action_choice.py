

class ActionChoice:
    """Печатает список спеллов игроку и предоставляет сделать выбор. Возвращает класс способности и цель."""

    @staticmethod
    def do(character):
        from mechanics.feeling import Feeling
        count = 0
        print('')
        print(character.name)
        print(f"{Feeling.own_health(character.health)} {Feeling.own_mana(character.mana)}")
        print('')
        for action in character.spells:
            count += 1
            print(f"{count}. {action.name} {Feeling.mana_cost(action.mana_cost)}")

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
        target = None
        print('')
        if result.direction == 'target':

            key = True
            while key:
                if key:

                    print('1. На себя')
                    print('2. На противника')
                    choice = input("Выберите цель: ")

                    if choice == '1':
                        target = 'self'
                        key = False
                        break
                    elif choice == '2':
                        target = 'enemy'
                        key = False
                        break
                    else:
                        print('Неверный номер цели...')
        elif result.direction == 'enemy':
            target = 'enemy'
        else:
            target = 'self'
        return result, target
