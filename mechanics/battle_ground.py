
class BattleGround:

    def __init__(self, first_char, second_char):

        self.first_char = first_char
        self.second_char = second_char
        self.spells = []
        self.loser = None

# ************************************ НАЧАЛО ЛОГИКИ ************************************ #

    def checking_defeat_everybody(self):
        """Условие поражения для всех сразу"""
        if self.first_char.player and self.second_char.player and self.first_char <= 0 >= self.second_char:
            self.loser = 'everybody'
            return self.loser

    def checking_defeat_first(self):
        """Условие поражения для второго персонажа"""
        if self.checking_defeat_everybody():
            return self.loser
        elif self.first_char.player:
            if self.first_char.health <= 0:
                self.loser = self.first_char
            return self.loser
        else:
            if self.first_char.health <= 0 < self.second_char.health:
                self.loser = self.first_char
            return self.loser

    def checking_defeat_second(self):
        """Условие поражения для первого персонажа"""
        if self.checking_defeat_everybody():
            return self.loser
        elif self.second_char.player:
            if self.first_char.health <= 0:
                self.loser = self.first_char
            return self.loser
        else:
            if self.second_char.health <= 0 < self.first_char.health:
                self.loser = self.second_char
            return self.loser

    def checking_luck(self):
        """Отнимает удачу у проигравшего и проверяет оставшееся количество. Если удача = 0 --> убивает персонажа"""
        if self.loser != 'everybody':
            if self.loser.player:
                self.loser.luck -= 1
                if self.loser.luck < 0:
                    self.loser.alive = False
        else:
            for i in [self.first_char, self.second_char]:
                i.luck -= 1
                if i.luck < 0:
                    i.alive = False

# ************************************* КОНЕЦ ЛОГИКИ ************************************ #

# ***************************** ТУТ НАЧИНАЕТСЯ САМОЕ ВАЖНОЕ ***************************** #

    def main(self):
        """Здесь кастуются спелы и проходят проверки. Работает, пока кто-нибудь не проиграет"""
        from mechanics.action_choice import ActionChoice

        while not self.loser:
            # Выбор спелла игроками
            first_set = ActionChoice.do(self.first_char)
            second_set = ActionChoice.do(self.second_char)

            # Проверка скорости
            if first_set[0].speed < second_set[0].speed:

                # Условия таргета для первого игрока
                target = self.first_char if first_set[1] == 'self' else self.second_char
                first_spell = first_set[0](self.first_char, target)

                # Условия таргета для второго игрока
                target = self.second_char if first_set[1] == 'self' else self.first_char
                second_spell = second_set[0](self.second_char, target)
            else:
                # Условия таргета для второго игрока
                target = self.second_char if first_set[1] == 'self' else self.first_char
                first_spell = second_set[0](self.second_char, target)

                # Условие для таргета первого игрока
                target = self.first_char if first_set[1] == 'self' else self.second_char
                second_spell = first_set[0](self.first_char, target)

            # Добавление спеллов в стэк спеллов
            self.spells.insert(0, second_spell)
            self.spells.insert(0, first_spell)

            spell_list_len = len(self.spells)
            cycle_count = 0
            for _ in range(spell_list_len):
                for spell in self.spells:
                    if spell.count > 0:
                        spell.do()
                        spell.count -= 1
                    else:

                        if self.checking_defeat_first() or self.checking_defeat_second():
                            break

        self.checking_luck()

# *************************** ТУТ ЗАКАНЧИВАЕТСЯ САМОЕ ВАЖНОЕ **************************** #

