

class Turn:

    def __init__(self, first_char, second_char):
        self.first_char = first_char
        self.second_char = second_char
        self.turn_now = self.first_char

    def do(self):
        from mechanics.action_choice import ActionChoice
        if self.turn_now.player:
            ActionChoice.do(self.turn_now)
        else:
            pass
        self.turn_now = self.second_char if self.turn_now == self.first_char else self.turn_now = self.first_char


