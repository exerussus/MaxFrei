

class ActionChoice:

    @staticmethod
    def do(character):
        from mechanics.feeling import Feeling
        count = 0
        print(f"{Feeling.own_health(character.health)}")
        print(f"{Feeling.own_mana(character.mana)}")

        for action in character.spells:
            count += 1
            print(f"{count}. {action.name} {Feeling.mana_cost(action.value_mana_caster)}")

