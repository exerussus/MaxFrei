

class Turn:

    def __init__(self, first_char, second_char):
        self.first_char = first_char
        self.second_char = second_char
        self.turn_now = self.first_char

    def do(self):

        spells = [spell for spell in self.turn_now.spells]


