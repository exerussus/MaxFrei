

class SpellRuler:

    def __init__(self, spell_list):
        self.spell_list = spell_list

    def cast(self, new_spell):
        self.spell_list.append(new_spell)

    def do(self):
        for s in self.spell_list:
            s.do()

