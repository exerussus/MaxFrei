

class Turn:
    """Даёт возможность выбрать спелл через action_choice для человека и bot_choice боту"""

    def __init__(self, first_char, second_char):
        self.first_char = first_char
        self.second_char = second_char

    def do(self):
        from mechanics.action_choice import ActionChoice
        return ActionChoice.do(self.first_char), ActionChoice.do(self.second_char)



